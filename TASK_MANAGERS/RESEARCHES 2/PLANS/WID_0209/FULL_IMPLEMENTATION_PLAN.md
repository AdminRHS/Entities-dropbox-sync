# Implementation Plan: Google Sheets Task Manager with Visual Dashboards

**Plan ID:** cosmic-stirring-lollipop
**Created:** 2025-12-09
**Status:** Ready for Review

---

## Executive Summary

This plan transforms the Task Manager ecosystem from a Google Forms-based tracking system into a **visual, hierarchical dashboard** directly connected to Google Sheets, with daily notes as the primary input method and agent integration for automation.

**Key Shifts from Phase 1-3 Approach:**
- ❌ **NO** Google Forms for task submission
- ✅ **YES** Daily notes review as input method
- ✅ **YES** Visual dashboards with hierarchical display (projects → milestones → tasks → steps)
- ✅ **YES** "Music soundline" style progress visualization with expandable/collapsible sections
- ✅ **YES** Advanced UI: colors, dropdowns, conditional formatting
- ✅ **YES** Agent integration (AGT.01, AGT.02) reading/writing from sheets

---

## Phase 1: Google Sheets Connection & Data Migration

### 1.1 Verify Existing Infrastructure

**Location:** `C:\Users\Dell\Dropbox\ENTITIES_2.0\ASSETS\sheets_sync`

**Tasks:**
1. Read and verify `credentials.json` for service account authentication
2. Test connection using existing `simple_example.py` script
3. Confirm spreadsheet access: `1yLcjy9R5_BSOiIkHRmzygA0oUZguGh8fszglQFdFAz4`
4. Verify Python dependencies (google-api-python-client, oauth2client)

**Success Criteria:**
- Successfully read/write to target spreadsheet
- Service account has edit permissions
- No authentication errors

### 1.2 Design Sheet Structure (Hierarchical)

**NEW Architecture** (replacing 6-sheet flat structure with hierarchical):

#### Sheet 1: `Dashboard_Overview` (Main View)
**Purpose:** Executive summary with expandable hierarchy

**Columns (A-Z, AA-AH):**
```
A: Level (Project/Milestone/Task/Step)
B: Hierarchy_ID (PRJ-001, MIL-001-01, TSK-001-01-05, STP-001-01-05-03)
C: Parent_ID (references parent in hierarchy)
D: Indent_Level (0=Project, 1=Milestone, 2=Task, 3=Step)
E: Expand_Collapse (▼/▶ symbols, use Data Validation for dropdown)
F: Title
G: Description
H: Type (Dropdown: Recruitment, Lead Gen, Design, Dev, Sales, Video, Admin, Research, Other)
I: Department
J: Assigned_To
K: Status (Dropdown: Not Started, In Progress, Blocked, Review, Complete, Cancelled)
L: Priority (Dropdown: Critical, High, Medium, Low)
M: Due_Date
N: Start_Date
O: End_Date
P: Progress_Bar (visual: ████░░░░░░ 40%)
Q: Progress_Percent (calculated: tasks complete / total tasks)
R: Days_Open (formula: TODAY() - Start_Date)
S: Days_Until_Due (formula: Due_Date - TODAY())
T: Days_Overdue (formula: IF(Due_Date<TODAY() AND Status<>"Complete", TODAY()-Due_Date, ""))
U: Complexity (Dropdown: Routine, Moderate, Complex)
V: Automation_Potential (Dropdown: High, Medium, Low, None)
W: Agent_Assigned (Dropdown: AGT.01-Recruiter, AGT.02-LeadGen, Human, None)
X: Blockers
Y: Dependencies
Z: Notes
AA: Success_Criteria
AB: Tools_Required
AC: Created_Date
AD: Created_By
AE: Last_Updated
AF: Updated_By
AG: Estimated_Duration
AH: Actual_Duration
```

**Row Grouping Strategy:**
- Use Google Sheets native grouping (Data > Group rows) for expand/collapse
- Projects at indent level 0
- Milestones at indent level 1 (grouped under projects)
- Tasks at indent level 2 (grouped under milestones)
- Steps at indent level 3 (grouped under tasks)

**Visual Design:**
- Indent levels shown with increasing indentation in column F (Title)
- Background colors by level: Projects (dark blue), Milestones (medium blue), Tasks (light blue), Steps (white)
- Progress bars in column P using REPT() formula with Unicode blocks

#### Sheet 2: `Active_Tasks_Flat` (Agent View)
**Purpose:** Flat view for agent processing and assignment

**Columns:** Same 32-column structure from Phase 3 implementation
- Used by AGT.01 and AGT.02 for reading/writing
- No hierarchy, just task-level entries
- Synced with Dashboard_Overview via formulas

#### Sheet 3: `Completed_Archive`
**Purpose:** Historical record of completed tasks

**Columns:** Same as Active_Tasks_Flat
- Auto-populated when Dashboard_Overview status = "Complete"
- Read-only for reporting and analytics

#### Sheet 4: `Daily_Notes_Intake`
**Purpose:** Daily notes parsing and task extraction

**Columns:**
```
A: Note_Date
B: Note_Source (Daily Notes, Email, Slack, Meeting Notes)
C: Raw_Notes (full text)
D: Extracted_Tasks (parsed task list)
E: Processed (Yes/No checkbox)
F: Processed_By
G: Processed_Date
H: Created_Task_IDs (comma-separated list of Task IDs created)
```

**Workflow:**
1. User pastes daily notes into column C
2. Python script parses notes and extracts tasks into column D
3. User reviews extracted tasks and marks Processed = Yes
4. Script creates task entries in Dashboard_Overview and Active_Tasks_Flat

#### Sheet 5: `Agent_Activity_Log`
**Purpose:** Track agent actions and decisions

**Columns:**
```
A: Timestamp
B: Agent_ID (AGT.01, AGT.02)
C: Action (Task_Created, Task_Updated, Task_Completed, Email_Sent, etc.)
D: Task_ID
E: Details (JSON or text description)
F: Autonomy_Level (High/Medium/Low)
G: Approval_Required (Yes/No)
H: Approval_Status (Pending/Approved/Rejected)
```

#### Sheet 6: `Settings_Config`
**Purpose:** Configuration and lookup tables

**Sections:**
- Department list
- Employee capacity table
- Agent capabilities matrix
- Status/Priority definitions
- Color coding rules

### 1.3 Migrate Existing Task Data

**Source:** `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\`

**Data to migrate:**
1. **DISTRIBUTION_MASTER.csv** → Active_Tasks_Flat sheet
   - 96 task assignments across 9 departments

2. **Task Templates** (22 templates) → Reference library (new sheet: `Task_Templates_Library`)
   - Template_ID, Template_Name, Action, Object, Context, Steps, Checklist

3. **Project Templates** (3 templates) → Projects in Dashboard_Overview
   - Create initial project hierarchy

4. **Step Templates** (141 templates) → Reference library (new sheet: `Step_Templates_Library`)

**Migration Script:** Enhance `upload_task_manager_data.py`

```python
# Pseudocode structure
def migrate_task_data():
    # 1. Read DISTRIBUTION_MASTER.csv
    # 2. Parse PRJ, TSK, PRT files from TASK_MANAGERS
    # 3. Build hierarchy: Projects → Milestones → Tasks → Steps
    # 4. Write to Dashboard_Overview with correct Parent_IDs
    # 5. Write flat task list to Active_Tasks_Flat
    # 6. Create lookup tables in Settings_Config
```

**Success Criteria:**
- All 96 current tasks migrated
- Hierarchy correctly established with Parent_IDs
- No data loss
- All templates accessible in reference sheets

---

## Phase 2: Visual Dashboard Development

### 2.1 Implement Hierarchical Display

**Google Sheets Grouping Setup:**

1. **Install Apps Script** for dynamic grouping:

```javascript
function toggleRowGroup(row) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Dashboard_Overview");
  var indentLevel = sheet.getRange(row, 4).getValue(); // Column D: Indent_Level
  var symbol = sheet.getRange(row, 5).getValue(); // Column E: Expand_Collapse

  if (symbol == "▼") {
    // Collapse: hide child rows
    collapseChildren(sheet, row, indentLevel);
    sheet.getRange(row, 5).setValue("▶");
  } else {
    // Expand: show child rows
    expandChildren(sheet, row, indentLevel);
    sheet.getRange(row, 5).setValue("▼");
  }
}

function collapseChildren(sheet, parentRow, parentLevel) {
  var lastRow = sheet.getLastRow();
  var childRows = [];

  for (var i = parentRow + 1; i <= lastRow; i++) {
    var currentLevel = sheet.getRange(i, 4).getValue();
    if (currentLevel <= parentLevel) break; // Reached next parent
    childRows.push(i);
  }

  if (childRows.length > 0) {
    sheet.hideRows(childRows[0], childRows.length);
  }
}

function expandChildren(sheet, parentRow, parentLevel) {
  var lastRow = sheet.getLastRow();
  var childRows = [];

  for (var i = parentRow + 1; i <= lastRow; i++) {
    var currentLevel = sheet.getRange(i, 4).getValue();
    if (currentLevel <= parentLevel) break;
    if (currentLevel == parentLevel + 1) { // Only direct children
      childRows.push(i);
    }
  }

  if (childRows.length > 0) {
    sheet.showRows(childRows[0], childRows.length);
  }
}
```

2. **Add onClick trigger** to Expand_Collapse column:
   - Use Apps Script to attach `toggleRowGroup()` to column E clicks
   - Alternative: Use checkboxes in column E with onEdit trigger

### 2.2 Create "Music Soundline" Progress Visualization

**Progress Bar Formula (Column P):**

```excel
=IF(Q2="","",REPT("█",ROUND(Q2*20,0))&REPT("░",20-ROUND(Q2*20,0))&" "&TEXT(Q2,"0%"))
```

This creates: `████████░░░░░░░░░░░░ 40%`

**Progress Percent Calculation (Column Q):**

For Projects and Milestones (aggregates child completion):
```excel
=IF(A2="Project",
  COUNTIFS($C:$C,B2,$K:$K,"Complete")/COUNTIF($C:$C,B2),
  IF(A2="Milestone",
    COUNTIFS($C:$C,B2,$K:$K,"Complete")/COUNTIF($C:$C,B2),
    IF(K2="Complete",1,IF(K2="In Progress",0.5,0))
  )
)
```

**Timeline Visualization (NEW Sheet: `Timeline_Gantt`):**

Create a Gantt-chart style view:
- Rows: Tasks/Milestones
- Columns: Dates (dynamic date range)
- Cells: Colored bars showing duration
- Formula-based conditional formatting for bars

### 2.3 Conditional Formatting Rules

**Status-based Row Colors (Dashboard_Overview):**

| Status | Background Color | Text Color |
|--------|-----------------|------------|
| Not Started | Light gray (#f3f3f3) | Black |
| In Progress | Light blue (#cfe2f3) | Black |
| Blocked | Light red (#f4cccc) | Dark red |
| Review | Light yellow (#fff2cc) | Black |
| Complete | Light green (#d9ead3) | Dark green |
| Cancelled | Light gray (#cccccc) | Gray |

**Priority-based Text Colors (Column L):**

| Priority | Text Color | Bold |
|----------|------------|------|
| Critical | Red (#cc0000) | Yes |
| High | Orange (#ff6600) | Yes |
| Medium | Blue (#0000ff) | No |
| Low | Gray (#666666) | No |

**Overdue Highlighting (Column T):**

If Days_Overdue > 0: Background = Dark red (#cc0000), Text = White

**Apps Script for Conditional Formatting:**

```javascript
function applyConditionalFormatting() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Dashboard_Overview");
  var range = sheet.getDataRange();

  // Status-based row colors
  var statusRules = [
    {status: "In Progress", color: "#cfe2f3"},
    {status: "Blocked", color: "#f4cccc"},
    {status: "Complete", color: "#d9ead3"}
    // ... etc
  ];

  statusRules.forEach(function(rule) {
    var conditionalFormatRule = SpreadsheetApp.newConditionalFormatRule()
      .whenFormulaSatisfied('=$K1="' + rule.status + '"')
      .setBackground(rule.color)
      .setRanges([range])
      .build();
    var rules = sheet.getConditionalFormatRules();
    rules.push(conditionalFormatRule);
    sheet.setConditionalFormatRules(rules);
  });
}
```

### 2.4 Dropdown Menus via Data Validation

**Configure dropdowns for:**

1. **Status (Column K):**
   - Values: Not Started, In Progress, Blocked, Review, Complete, Cancelled
   - Source: Settings_Config sheet, range `StatusList`

2. **Priority (Column L):**
   - Values: Critical, High, Medium, Low
   - Source: Settings_Config sheet, range `PriorityList`

3. **Type (Column H):**
   - Values: Recruitment, Lead Gen, Design, Dev, Sales, Video, Admin, Research, Other
   - Source: Settings_Config sheet, range `TypeList`

4. **Assigned_To (Column J):**
   - Values: Employee names + AGT.01-Recruiter, AGT.02-LeadGen
   - Source: Settings_Config sheet, range `AssigneeList`

5. **Agent_Assigned (Column W):**
   - Values: AGT.01-Recruiter, AGT.02-LeadGen, Human, None
   - Source: Settings_Config sheet, range `AgentList`

**Setup Script:**

```javascript
function setupDataValidation() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Dashboard_Overview");
  var configSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Settings_Config");

  // Status dropdown (Column K)
  var statusRange = configSheet.getRange("StatusList");
  var statusRule = SpreadsheetApp.newDataValidation()
    .requireValueInRange(statusRange)
    .setAllowInvalid(false)
    .build();
  sheet.getRange("K2:K1000").setDataValidation(statusRule);

  // Repeat for other columns...
}
```

---

## Phase 3: Daily Notes Integration

### 3.1 Daily Notes Input Workflow

**Two-Option Approach** (user can choose preference):

#### Option A: Direct Paste into Google Sheets

**Process:**
1. User opens `Daily_Notes_Intake` sheet
2. Pastes raw notes into column C (Raw_Notes)
3. Enters date in column A, source in column B
4. Saves sheet
5. Python script (runs on schedule or manual trigger) parses notes
6. Script populates column D (Extracted_Tasks) with structured task list
7. User reviews and approves (marks Processed = Yes)
8. Script creates tasks in Dashboard_Overview

**Notes Format Example:**
```
2025-12-09 Daily Notes:

- Follow up with 5 old clients about re-engagement (SALES)
- Screen 3 new candidates for Python Developer role (RECRUITMENT) - URGENT
- Research 10 companies for lead gen campaign (LEAD GEN)
- Design social media graphics for Q1 campaign (DESIGN)
- Update CRM with last week's activities (ADMIN)

Blockers:
- Waiting for HR approval on salary range for Python role
```

**Parsing Logic (Python NLP):**

```python
import re
from datetime import datetime

def parse_daily_notes(raw_notes):
    """Extract tasks from freeform daily notes"""
    tasks = []

    # Regex patterns to identify tasks
    task_patterns = [
        r'[-•]\s*(.+?)(?:\(([A-Z\s]+)\))?(?:\s*-\s*(URGENT|HIGH|MEDIUM|LOW))?',
        r'TODO:\s*(.+)',
        r'Action:\s*(.+)'
    ]

    for pattern in task_patterns:
        matches = re.finditer(pattern, raw_notes, re.MULTILINE)
        for match in matches:
            task = {
                'title': match.group(1).strip(),
                'department': match.group(2).strip() if len(match.groups()) > 1 else 'General',
                'priority': match.group(3).strip() if len(match.groups()) > 2 else 'Medium',
                'source': 'Daily Notes',
                'created_date': datetime.now().strftime('%Y-%m-%d')
            }
            tasks.append(task)

    return tasks

def create_tasks_from_notes(sheet_service, spreadsheet_id, notes_row):
    """Read notes from Daily_Notes_Intake, parse, and create tasks"""
    # 1. Read raw notes from column C
    raw_notes = read_cell(sheet_service, spreadsheet_id, 'Daily_Notes_Intake', notes_row, 3)

    # 2. Parse notes
    extracted_tasks = parse_daily_notes(raw_notes)

    # 3. Write extracted tasks to column D for review
    write_cell(sheet_service, spreadsheet_id, 'Daily_Notes_Intake', notes_row, 4,
               '\n'.join([f"- {t['title']} ({t['department']}, {t['priority']})" for t in extracted_tasks]))

    # 4. Wait for user approval (Processed = Yes in column E)
    # (This would be checked in next script run)

    return extracted_tasks

def finalize_tasks(sheet_service, spreadsheet_id, notes_row, extracted_tasks):
    """Create approved tasks in Dashboard_Overview and Active_Tasks_Flat"""
    task_ids_created = []

    for task in extracted_tasks:
        # Generate Task ID
        task_id = generate_task_id()

        # Create row in Dashboard_Overview
        dashboard_row = [
            'Task',  # Level
            task_id,  # Hierarchy_ID
            '',  # Parent_ID (can be assigned later)
            2,  # Indent_Level (task level)
            '▼',  # Expand_Collapse
            task['title'],  # Title
            '',  # Description (empty for now)
            task['department'],  # Type
            task['department'],  # Department
            '',  # Assigned_To (to be assigned)
            'Not Started',  # Status
            task['priority'],  # Priority
            '',  # Due_Date (to be set)
            task['created_date'],  # Start_Date
            '',  # End_Date
            '',  # Progress_Bar
            0,  # Progress_Percent
            # ... fill remaining columns
        ]

        append_row(sheet_service, spreadsheet_id, 'Dashboard_Overview', dashboard_row)

        # Create row in Active_Tasks_Flat
        active_row = convert_to_flat_format(dashboard_row)
        append_row(sheet_service, spreadsheet_id, 'Active_Tasks_Flat', active_row)

        task_ids_created.append(task_id)

    # Update Daily_Notes_Intake with created Task IDs
    write_cell(sheet_service, spreadsheet_id, 'Daily_Notes_Intake', notes_row, 8,
               ', '.join(task_ids_created))

    return task_ids_created
```

#### Option B: Email-to-Sheets via Apps Script

**Process:**
1. User emails daily notes to dedicated Gmail address (e.g., taskmanager@yourdomain.com)
2. Apps Script monitors inbox for emails with subject: "Daily Notes"
3. Script extracts email body and writes to Daily_Notes_Intake sheet
4. Same parsing workflow as Option A

**Apps Script for Email Monitoring:**

```javascript
function processDailyNotesEmails() {
  var threads = GmailApp.search('subject:"Daily Notes" is:unread');
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Daily_Notes_Intake");

  threads.forEach(function(thread) {
    var messages = thread.getMessages();
    messages.forEach(function(message) {
      var body = message.getPlainBody();
      var date = message.getDate();

      sheet.appendRow([
        Utilities.formatDate(date, Session.getScriptTimeZone(), "yyyy-MM-dd"),
        "Email",
        body,
        "", // Extracted_Tasks (empty, will be filled by Python)
        "No", // Processed
        "",
        "",
        ""
      ]);

      message.markRead();
    });
  });
}
```

### 3.2 Task Assignment Logic from Notes

**Decision Tree for Auto-Assignment:**

```python
def assign_task_from_notes(task):
    """Determine assignee based on task content and department"""

    # Check if task matches AGT.01 capabilities (Recruitment)
    recruitment_keywords = ['candidate', 'screen', 'interview', 'hire', 'recruit', 'resume', 'cv']
    if any(keyword in task['title'].lower() for keyword in recruitment_keywords):
        if task['priority'] in ['Critical', 'High']:
            return 'AGT.01-Recruiter'  # High autonomy
        else:
            return 'AGT.01-Recruiter'

    # Check if task matches AGT.02 capabilities (Lead Gen)
    leadgen_keywords = ['email', 'outreach', 'lead', 'client', 'cold', 'follow-up', 'campaign']
    if any(keyword in task['title'].lower() for keyword in leadgen_keywords):
        return 'AGT.02-LeadGen'

    # Check department-based assignment
    if task['department'] == 'SALES':
        # Check employee capacity
        sales_team = get_employees_by_department('Sales')
        return assign_by_capacity(sales_team)

    elif task['department'] == 'DESIGN':
        design_team = get_employees_by_department('Design')
        return assign_by_capacity(design_team)

    # Default: unassigned
    return ''

def assign_by_capacity(employee_list):
    """Assign to employee with lowest current task load"""
    # Query Active_Tasks_Flat for current assignments
    # Return employee with fewest active tasks
    pass
```

---

## Phase 4: Agent Integration

### 4.1 Connect AGT.01 (Recruiter Agent) to Google Sheets

**Read Operations:**

AGT.01 needs to:
1. Read tasks assigned to "AGT.01-Recruiter" from Active_Tasks_Flat
2. Retrieve task details (candidates, job postings, interview schedules)
3. Check task dependencies and blockers

**Python Integration:**

```python
# In AGT.01's main loop
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

class RecruitmentAgent:
    def __init__(self):
        self.sheets_service = self.connect_to_sheets()
        self.spreadsheet_id = '1yLcjy9R5_BSOiIkHRmzygA0oUZguGh8fszglQFdFAz4'

    def connect_to_sheets(self):
        """Authenticate and connect to Google Sheets API"""
        scope = ['https://www.googleapis.com/auth/spreadsheets']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            'C:/Users/Dell/Dropbox/ENTITIES_2.0/ASSETS/sheets_sync/credentials.json',
            scope
        )
        service = build('sheets', 'v4', credentials=creds)
        return service

    def get_my_tasks(self):
        """Retrieve all tasks assigned to AGT.01"""
        result = self.sheets_service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range='Active_Tasks_Flat!A2:AF1000'
        ).execute()

        rows = result.get('values', [])
        my_tasks = []

        for row in rows:
            if len(row) > 9 and row[9] == 'AGT.01-Recruiter':  # Column J: Assigned_To
                task = {
                    'id': row[0],
                    'title': row[3],
                    'description': row[4],
                    'status': row[8],
                    'priority': row[7],
                    'due_date': row[10],
                    'dependencies': row[15] if len(row) > 15 else '',
                    'blockers': row[19] if len(row) > 19 else ''
                }
                my_tasks.append(task)

        return my_tasks

    def process_tasks(self):
        """Main agent loop - process assigned tasks"""
        tasks = self.get_my_tasks()

        for task in tasks:
            if task['status'] == 'Pending':
                # Determine capability needed
                if 'screen' in task['title'].lower() or 'candidate' in task['title'].lower():
                    self.screen_candidates(task)
                elif 'interview' in task['title'].lower():
                    self.coordinate_interview(task)
                # ... other capabilities

            elif task['status'] == 'In Progress':
                # Continue work on task
                self.continue_task(task)

    def screen_candidates(self, task):
        """Execute candidate screening capability"""
        # 1. Extract candidate info from task description or dependencies
        # 2. Run screening logic (resume parsing, keyword matching, etc.)
        # 3. Update task status and notes
        # 4. Log activity

        self.update_task_status(task['id'], 'In Progress')
        self.add_task_note(task['id'], 'Started candidate screening at ' + datetime.now().isoformat())
        self.log_activity('AGT.01', 'Task_Updated', task['id'], 'Started screening candidates')

        # ... screening logic ...

        self.update_task_status(task['id'], 'Complete')
        self.add_task_note(task['id'], 'Screening complete. 3 candidates qualified.')

    def update_task_status(self, task_id, new_status):
        """Update task status in Google Sheets"""
        # Find row with task_id
        row_index = self.find_task_row(task_id)

        # Update status column (Column I)
        self.sheets_service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheet_id,
            range=f'Active_Tasks_Flat!I{row_index}',
            valueInputOption='RAW',
            body={'values': [[new_status]]}
        ).execute()

        # Also update in Dashboard_Overview
        # ... similar update logic

    def add_task_note(self, task_id, note):
        """Append note to task's Notes column"""
        row_index = self.find_task_row(task_id)

        # Read existing notes
        existing_notes = self.sheets_service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range=f'Active_Tasks_Flat!U{row_index}'
        ).execute().get('values', [['']])[0][0]

        # Append new note with timestamp
        new_notes = existing_notes + '\n' + f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] {note}"

        # Write back
        self.sheets_service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheet_id,
            range=f'Active_Tasks_Flat!U{row_index}',
            valueInputOption='RAW',
            body={'values': [[new_notes]]}
        ).execute()

    def log_activity(self, agent_id, action, task_id, details):
        """Write to Agent_Activity_Log sheet"""
        log_row = [
            datetime.now().isoformat(),
            agent_id,
            action,
            task_id,
            details,
            'High',  # Autonomy level for this action
            'No',  # Approval required
            'N/A'  # Approval status
        ]

        self.sheets_service.spreadsheets().values().append(
            spreadsheetId=self.spreadsheet_id,
            range='Agent_Activity_Log!A:H',
            valueInputOption='RAW',
            body={'values': [log_row]}
        ).execute()
```

### 4.2 Connect AGT.02 (Lead Gen Agent) to Google Sheets

**Similar structure as AGT.01, with lead gen-specific capabilities:**

```python
class LeadGenAgent:
    def __init__(self):
        self.sheets_service = self.connect_to_sheets()
        self.spreadsheet_id = '1yLcjy9R5_BSOiIkHRmzygA0oUZguGh8fszglQFdFAz4'

    def process_tasks(self):
        """Main agent loop - process assigned tasks"""
        tasks = self.get_my_tasks()  # Tasks assigned to AGT.02-LeadGen

        for task in tasks:
            if 'email' in task['title'].lower() and 'old client' in task['title'].lower():
                self.send_reengagement_emails(task)
            elif 'research' in task['title'].lower():
                self.research_companies(task)
            elif 'campaign' in task['title'].lower():
                self.run_email_campaign(task)

    def send_reengagement_emails(self, task):
        """Execute old client re-engagement workflow"""
        # This maps to TASK-TEMPLATE-002 from Task_Templates.md

        # 1. Export old client list from CRM
        clients = self.export_old_clients()

        # 2. Research each company
        for client in clients:
            research_notes = self.research_company(client)

            # 3. Generate personalized email
            email_content = self.generate_email(client, research_notes)

            # 4. Send email
            self.send_email(client['email'], email_content)

            # 5. Log in CRM and update task
            self.log_crm_activity(client, 'Email sent')
            self.add_task_note(task['id'], f"Email sent to {client['name']}")

        # 6. Update task progress
        progress = len(clients) / 50  # Target: 50 emails
        self.update_task_progress(task['id'], progress)

        if len(clients) >= 50:
            self.update_task_status(task['id'], 'Complete')
```

### 4.3 Agent Decision Authority & Approval Workflow

**Based on AGT.01 and AGT.02 AGENT.md specifications:**

**AGT.01 Approval Requirements:**
- **High Autonomy (no approval):** Candidate screening, CRM updates, analytics
- **Medium Autonomy (notify after):** Interview coordination
- **Low Autonomy (approve before):** Offer management, salary negotiations

**AGT.02 Approval Requirements:**
- **High Autonomy (no approval):** Cold emails, campaign automation, response tracking, contact scraping
- **Medium Autonomy (notify after):** Company research reports

**Implementation in Agent Code:**

```python
def execute_task_with_approval(self, task, capability):
    """Check if approval needed before executing"""
    autonomy_level = self.get_autonomy_level(capability)

    if autonomy_level == 'Low':
        # Request approval first
        approval_request_id = self.request_approval(task, capability)

        # Write to Agent_Activity_Log
        self.log_activity(self.agent_id, 'Approval_Requested', task['id'],
                         f"Requesting approval for {capability}")

        # Wait for approval (check periodically)
        while True:
            approval_status = self.check_approval_status(approval_request_id)
            if approval_status == 'Approved':
                # Execute task
                self.execute_capability(task, capability)
                break
            elif approval_status == 'Rejected':
                # Mark task as blocked
                self.update_task_status(task['id'], 'Blocked')
                self.add_task_note(task['id'], 'Approval rejected. Awaiting guidance.')
                break
            time.sleep(300)  # Check every 5 minutes

    elif autonomy_level == 'Medium':
        # Execute and notify after
        self.execute_capability(task, capability)
        self.notify_completion(task, capability)

    else:  # High autonomy
        # Execute without approval
        self.execute_capability(task, capability)
```

**Approval Interface in Google Sheets:**

Add new sheet: `Approval_Queue`

**Columns:**
```
A: Request_ID
B: Timestamp
C: Agent_ID
D: Task_ID
E: Task_Title
F: Capability
G: Action_Details
H: Approval_Status (Dropdown: Pending, Approved, Rejected)
I: Approved_By
J: Approval_Date
K: Comments
```

**User workflow:**
1. Agent writes approval request to Approval_Queue
2. User receives email notification (via Apps Script trigger)
3. User reviews request in Approval_Queue sheet
4. User sets Approval_Status to "Approved" or "Rejected"
5. Agent checks Approval_Queue periodically and proceeds accordingly

---

## Phase 5: Advanced Features & Polish

### 5.1 Additional Dashboard Enhancements

**Feature 1: Dependency Visualization**

Add new column: `Dependency_Status`
- Formula checks if all dependencies (column Y) are complete
- Shows "🔓 Ready" (green) or "🔒 Blocked" (red)

```excel
=IF(Y2="","🔓 Ready",
  IF(COUNTIF(Active_Tasks_Flat!A:A,Y2)=0,"⚠️ Missing Dependency",
    IF(VLOOKUP(Y2,Active_Tasks_Flat!A:K,9,FALSE)="Complete","🔓 Ready","🔒 Blocked")))
```

**Feature 2: Workload Heatmap**

Create new sheet: `Team_Capacity_Heatmap`
- Rows: Team members
- Columns: Task counts by status
- Conditional formatting: Red (overloaded) to Green (available)

**Feature 3: Sprint Planning View**

Create new sheet: `Sprint_Dashboard`
- Filter tasks by date range (current week/sprint)
- Show only tasks due within sprint
- Group by assignee with progress rollups

### 5.2 Automation Triggers

**Apps Script Triggers:**

1. **onEdit Trigger** - Auto-update Last_Updated and Updated_By columns
```javascript
function onEdit(e) {
  var sheet = e.source.getActiveSheet();
  if (sheet.getName() == "Dashboard_Overview" || sheet.getName() == "Active_Tasks_Flat") {
    var row = e.range.getRow();
    var col = e.range.getColumn();

    // Update Last_Updated (Column AE) and Updated_By (Column AF)
    sheet.getRange(row, 31).setValue(new Date());  // Column AE
    sheet.getRange(row, 32).setValue(Session.getActiveUser().getEmail());  // Column AF
  }
}
```

2. **Time-based Trigger** - Daily overdue check and notifications
```javascript
function checkOverdueTasks() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Active_Tasks_Flat");
  var data = sheet.getDataRange().getValues();
  var today = new Date();

  var overdueNotifications = [];

  for (var i = 1; i < data.length; i++) {
    var dueDate = new Date(data[i][10]);  // Column K: Due_Date
    var status = data[i][8];  // Column I: Status
    var assignee = data[i][9];  // Column J: Assigned_To
    var title = data[i][3];  // Column D: Task_Title

    if (status != "Complete" && status != "Cancelled" && dueDate < today) {
      overdueNotifications.push({
        assignee: assignee,
        task: title,
        dueDate: Utilities.formatDate(dueDate, Session.getScriptTimeZone(), "yyyy-MM-dd"),
        daysOverdue: Math.floor((today - dueDate) / (1000 * 60 * 60 * 24))
      });
    }
  }

  // Send email notifications
  sendOverdueNotifications(overdueNotifications);
}
```

3. **onChange Trigger** - Sync Dashboard_Overview ↔ Active_Tasks_Flat
```javascript
function syncSheets(e) {
  // When Dashboard_Overview is edited, update corresponding row in Active_Tasks_Flat
  // and vice versa

  // Implementation depends on maintaining Task_ID as primary key
}
```

### 5.3 Mobile Optimization

**Google Sheets Mobile App considerations:**

1. **Freeze panes:** Freeze columns A-F (hierarchy info) for horizontal scrolling
2. **Hide technical columns:** Hide columns like Hierarchy_ID, Parent_ID, Indent_Level for cleaner mobile view
3. **Simplified mobile view:** Create new sheet `Mobile_View` with essential columns only:
   - Title, Status, Priority, Due_Date, Assigned_To, Progress_Bar

4. **Quick-action buttons:** Add buttons in sheet for common actions:
   - "Mark Complete" button (runs Apps Script)
   - "Add Note" button (opens dialog)
   - "Request Help" button (creates support task)

---

## Implementation Timeline & Milestones

### Milestone 1: Foundation Setup (Days 1-2)
- ✅ Verify Google Sheets API connection
- ✅ Create 6-sheet structure in target spreadsheet
- ✅ Migrate existing task data from DISTRIBUTION_MASTER.csv
- ✅ Set up Settings_Config sheet with lookup tables

**Success Criteria:**
- All sheets created with correct column structure
- Existing 96 tasks migrated successfully
- Connection test successful

### Milestone 2: Visual Dashboard (Days 3-4)
- ✅ Implement hierarchical display with grouping
- ✅ Add progress bar formulas
- ✅ Configure conditional formatting rules
- ✅ Set up data validation dropdowns
- ✅ Create Apps Script for expand/collapse functionality

**Success Criteria:**
- Hierarchy displays correctly with indentation
- Progress bars show visual representation
- Color coding works for status/priority
- Expand/collapse works smoothly

### Milestone 3: Daily Notes Integration (Days 5-6)
- ✅ Set up Daily_Notes_Intake sheet
- ✅ Build Python NLP parser for note extraction
- ✅ Implement task creation from parsed notes
- ✅ Create email-to-sheets workflow (optional)
- ✅ Test end-to-end workflow

**Success Criteria:**
- Daily notes successfully parsed into tasks
- User can review and approve extracted tasks
- Tasks created in Dashboard_Overview with correct hierarchy
- Assignment logic works correctly

### Milestone 4: Agent Integration (Days 7-9)
- ✅ Connect AGT.01 to Google Sheets (read/write)
- ✅ Connect AGT.02 to Google Sheets (read/write)
- ✅ Implement approval workflow for low-autonomy actions
- ✅ Set up Agent_Activity_Log tracking
- ✅ Test agent task execution end-to-end

**Success Criteria:**
- AGT.01 successfully processes recruitment tasks
- AGT.02 successfully processes lead gen tasks
- Approval requests work correctly
- Activity logging captures all agent actions
- No data corruption or conflicts

### Milestone 5: Advanced Features (Days 10-12)
- ✅ Add dependency visualization
- ✅ Create team capacity heatmap
- ✅ Build sprint planning view
- ✅ Set up automation triggers (onEdit, time-based, onChange)
- ✅ Optimize for mobile viewing
- ✅ Create Timeline_Gantt sheet

**Success Criteria:**
- All advanced features functional
- Automation triggers work reliably
- Mobile view is usable
- Performance is acceptable (<3 second load time)

### Milestone 6: Testing & Documentation (Days 13-14)
- ✅ End-to-end testing of all workflows
- ✅ User acceptance testing
- ✅ Create user guide documentation
- ✅ Create admin/maintenance documentation
- ✅ Train users on new system

**Success Criteria:**
- All workflows tested and working
- Users can complete common tasks without assistance
- Documentation complete and accessible
- Known issues documented with workarounds

---

## Technical Specifications Summary

### Google Sheets Structure

**Total Sheets: 10**
1. Dashboard_Overview (main hierarchical view, 34 columns)
2. Active_Tasks_Flat (agent processing view, 32 columns)
3. Completed_Archive (historical record, 32 columns)
4. Daily_Notes_Intake (daily notes input, 8 columns)
5. Agent_Activity_Log (agent tracking, 8 columns)
6. Settings_Config (configuration, variable columns)
7. Approval_Queue (agent approvals, 11 columns)
8. Task_Templates_Library (22 templates, variable columns)
9. Step_Templates_Library (141 templates, variable columns)
10. Timeline_Gantt (visual timeline, dynamic columns)

### Python Scripts Required

**Location:** `C:\Users\Dell\Dropbox\ENTITIES_2.0\ASSETS\sheets_sync\`

1. **enhanced_upload_task_manager_data.py** - Migrate existing data
2. **daily_notes_parser.py** - Parse daily notes into tasks
3. **agent_agt01_main.py** - AGT.01 main processing loop
4. **agent_agt02_main.py** - AGT.02 main processing loop
5. **sync_sheets.py** - Sync Dashboard_Overview ↔ Active_Tasks_Flat
6. **task_assignment_logic.py** - Auto-assign tasks based on rules
7. **capacity_balancer.py** - Balance workload across team

### Google Apps Scripts Required

**Location:** Script editor in target Google Spreadsheet

1. **onEditTrigger.gs** - Auto-update timestamps and user
2. **toggleRowGroup.gs** - Expand/collapse hierarchy
3. **applyConditionalFormatting.gs** - Set up color rules
4. **setupDataValidation.gs** - Configure dropdowns
5. **checkOverdueTasks.gs** - Daily overdue notifications
6. **processDailyNotesEmails.gs** - Email-to-sheets workflow
7. **syncSheets.gs** - Bidirectional sheet sync

### Key Formulas

**Progress Bar (Column P):**
```excel
=IF(Q2="","",REPT("█",ROUND(Q2*20,0))&REPT("░",20-ROUND(Q2*20,0))&" "&TEXT(Q2,"0%"))
```

**Progress Percent - Projects/Milestones (Column Q):**
```excel
=IF(A2="Project",
  COUNTIFS($C:$C,B2,$K:$K,"Complete")/COUNTIF($C:$C,B2),
  IF(A2="Milestone",
    COUNTIFS($C:$C,B2,$K:$K,"Complete")/COUNTIF($C:$C,B2),
    IF(K2="Complete",1,IF(K2="In Progress",0.5,0))
  )
)
```

**Days Open (Column R):**
```excel
=IF(N2="","",IF(K2="Complete",O2-N2,TODAY()-N2))
```

**Days Until Due (Column S):**
```excel
=IF(M2="","",M2-TODAY())
```

**Days Overdue (Column T):**
```excel
=IF(AND(M2<TODAY(),K2<>"Complete",K2<>"Cancelled"),TODAY()-M2,"")
```

**Dependency Status:**
```excel
=IF(Y2="","🔓 Ready",
  IF(COUNTIF(Active_Tasks_Flat!A:A,Y2)=0,"⚠️ Missing",
    IF(VLOOKUP(Y2,Active_Tasks_Flat!A:K,9,FALSE)="Complete","🔓 Ready","🔒 Blocked")))
```

### API Credentials

**Service Account:** `sheet-sync@claude-sheets-480621.iam.gserviceaccount.com`
**Project ID:** `claude-sheets-480621`
**Spreadsheet ID:** `1yLcjy9R5_BSOiIkHRmzygA0oUZguGh8fszglQFdFAz4`
**Credentials File:** `C:\Users\Dell\Dropbox\ENTITIES_2.0\ASSETS\sheets_sync\credentials.json`

---

## Risk Assessment & Mitigation

### Risk 1: Google Sheets Performance with Large Datasets

**Risk:** 1000+ tasks may cause slow loading and formula recalculation

**Mitigation:**
- Use QUERY() function instead of complex nested formulas where possible
- Implement pagination in Dashboard_Overview (show only active projects/current sprint)
- Archive completed tasks regularly to Completed_Archive sheet
- Consider moving to Google Sheets API with external processing for very large datasets

### Risk 2: Concurrent Editing Conflicts (Human + Agents)

**Risk:** Agent updates may overwrite human edits or vice versa

**Mitigation:**
- Implement row-level locking via Apps Script (lock row when agent is processing)
- Use Last_Updated and Updated_By columns to track changes
- Agent reads data → checks Last_Updated → only writes if unchanged → otherwise logs conflict
- Conflict resolution: Human edits always win, agent retries later

**Code Example:**
```python
def safe_update_task(task_id, new_values):
    """Update task only if not modified since last read"""
    # 1. Read current row and Last_Updated timestamp
    current_row = read_task_row(task_id)
    current_timestamp = current_row['last_updated']

    # 2. Compare with timestamp from when we read the task initially
    if current_timestamp != self.task_read_timestamp[task_id]:
        # Someone else modified the task
        self.log_conflict(task_id, 'Task modified by another user during processing')
        return False  # Don't update, retry later

    # 3. Safe to update
    write_task_row(task_id, new_values)
    return True
```

### Risk 3: Daily Notes Parsing Accuracy

**Risk:** NLP parser may misinterpret notes or miss tasks

**Mitigation:**
- Always show extracted tasks in Daily_Notes_Intake sheet for user review
- Require user approval before creating tasks (Processed = Yes)
- Implement feedback loop: user can correct parsing errors, system learns
- Provide structured notes template to improve parsing accuracy

**Structured Notes Template:**
```
Date: 2025-12-09

TASKS:
- [DEPT] Task description [PRIORITY]
- [SALES] Follow up with 5 old clients [HIGH]
- [RECRUITMENT] Screen 3 Python candidates [URGENT]

BLOCKERS:
- Waiting for HR approval on salary range

NOTES:
- General notes that won't be parsed as tasks
```

### Risk 4: Agent Over-Automation

**Risk:** Agents may execute tasks incorrectly without sufficient oversight

**Mitigation:**
- Strict enforcement of autonomy levels (Low = always approve first)
- Comprehensive activity logging in Agent_Activity_Log
- Daily review of agent actions by human supervisor
- "Undo" functionality for agent actions within 24 hours
- Weekly audit reports showing all agent-completed tasks

### Risk 5: Data Loss or Corruption

**Risk:** Formula errors, script bugs, or user mistakes could corrupt data

**Mitigation:**
- Enable Google Sheets version history (automatic, 30-day retention)
- Daily automated backups to separate spreadsheet (via Apps Script)
- Backup to CSV files in Dropbox (via Python script, scheduled)
- Read-only reference sheets (templates, settings) protected from edits
- Comprehensive data validation rules to prevent invalid entries

**Backup Script:**
```javascript
function dailyBackup() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var backupFolder = DriveApp.getFolderById('BACKUP_FOLDER_ID');
  var timestamp = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), "yyyyMMdd_HHmmss");
  var backupName = "TaskManager_Backup_" + timestamp;

  ss.copy(backupName);
  var backupFile = DriveApp.getFilesByName(backupName).next();
  backupFile.moveTo(backupFolder);
}
```

---

## Open Questions for User Decision

While this plan provides a comprehensive implementation approach, the following decisions should be finalized based on user preference:

### Question 1: Daily Notes Format

**Option A:** Freeform text with NLP parsing (more flexible, less structured)
**Option B:** Structured template format (more reliable parsing, less flexible)
**Option C:** Hybrid - freeform with optional structured markers

**Recommendation:** Option C - allows flexibility while improving parsing accuracy

### Question 2: Hierarchical Display Depth

**Option A:** Always show all 4 levels (Projects → Milestones → Tasks → Steps)
**Option B:** Default collapse to Project level, expand on demand
**Option C:** Smart collapse - show only active/in-progress items expanded

**Recommendation:** Option C - reduces visual clutter while highlighting active work

### Question 3: Agent Autonomy Level for Initial Deployment

**Option A:** Conservative - all agent actions require approval initially
**Option B:** Standard - follow autonomy levels from AGENT.md specifications
**Option C:** Aggressive - high autonomy for all agents, review after 30 days

**Recommendation:** Option A for first 2 weeks, then transition to Option B after validation

### Question 4: Daily Notes Input Method

**Option A:** Direct paste into Google Sheets (Daily_Notes_Intake sheet)
**Option B:** Email to dedicated address, auto-import to sheets
**Option C:** Both options available, user chooses per day

**Recommendation:** Option C - maximum flexibility

### Question 5: Mobile vs. Desktop Priority

**Option A:** Optimize for desktop first, mobile is secondary
**Option B:** Equal priority - ensure excellent experience on both
**Option C:** Mobile-first - prioritize mobile usability

**Recommendation:** Option B - most users will use both depending on context

---

## Success Metrics

### Quantitative Metrics (30-day evaluation)

1. **Task Processing Efficiency:**
   - Time from task creation to assignment: < 5 minutes (automated)
   - Time from daily notes to tasks in system: < 10 minutes (with user review)

2. **Agent Performance:**
   - AGT.01 task completion rate: > 80% without human intervention
   - AGT.02 task completion rate: > 85% without human intervention
   - Agent accuracy (correctly completed tasks): > 95%

3. **User Adoption:**
   - Daily active users (viewing dashboard): 100% of team
   - Daily notes submission rate: > 90% of working days
   - User-reported errors or issues: < 5 per week

4. **System Reliability:**
   - Uptime (sheets accessible): > 99.9%
   - Data sync errors: < 1% of transactions
   - Formula calculation errors: 0%

### Qualitative Metrics (user feedback)

1. **Usability:**
   - Users can find task information within 30 seconds
   - Users can update task status without training
   - Visual hierarchy is clear and intuitive

2. **Value Delivered:**
   - Users spend less time on task management admin
   - Task visibility has improved (no "lost" tasks)
   - Team workload is more balanced

3. **Agent Trust:**
   - Users trust agent-completed tasks
   - Users feel agents augment (not replace) their work
   - Users understand when to involve agents vs. do manually

---

## Next Steps After Plan Approval

1. **User Review & Feedback** (This step)
   - Review this plan
   - Provide decisions on open questions
   - Approve to proceed or request modifications

2. **Environment Setup** (30 minutes)
   - Create backup of target spreadsheet
   - Set up development spreadsheet for testing
   - Install required Python libraries

3. **Phase 1 Execution** (Days 1-2)
   - Begin implementation following Milestone 1 tasks
   - Daily check-ins to report progress

4. **Iterative Development** (Days 3-14)
   - Complete Milestones 2-6
   - User testing at end of each milestone
   - Adjustments based on feedback

5. **Go-Live** (Day 15)
   - Final user training
   - Switch from development to production spreadsheet
   - Monitor closely for first week

---

**Plan Status:** ✅ Ready for User Review and Approval

**Estimated Total Implementation Time:** 14 days (with 1 developer + user collaboration)

**Estimated Effort:** ~80-100 hours (development + testing + documentation)

---

*This plan was created based on:*
- Existing task manager documentation in `ENTITIES/TASK_MANAGERS/`
- AGT.01 and AGT.02 agent specifications
- Phase 1-3 deliverables (task_ecosystem_analysis.md, daily_task_workflow.md, task_manager_implementation.md)
- Existing Google Sheets integration infrastructure at `ENTITIES_2.0/ASSETS/sheets_sync/`
- User's stated requirements for visual dashboards with hierarchical display and daily notes integration
