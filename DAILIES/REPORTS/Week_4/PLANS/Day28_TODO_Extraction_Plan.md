# Day 28 Employee Updates Extraction Plan

## Overview
Extract Day 28 (November 28, 2025) employee updates from TODO_EXTRACTION structured markdown files and consolidate them into a CSV format, organized by Department and Employee.

## Source Data
- **Location:** `C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\TODO_EXTRACTION\`
- **Files:** 16 employee TODO files organized by department subdirectories
- **Format:** Structured markdown files (`*_TODO_Day28_STRUCTURED.md`)
- **Departments:** Development, Lead_Generation, Finance, Design, Executive, HR, Human_Resources, Sales, Video_Production, AI_Automation

## Output Specification
- **Format:** CSV file
- **Location:** `C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\CONSOLIDATED\Day28_TODO_Consolidated.csv`
- **Organization:** By Department and Employee with task-level details

## Analysis Approach (MAIN_PROMPT v7.2)

### Entity Extraction (Task-First Bottom-Up)

Following MAIN_PROMPT v7.2 workflow:

1. **Extract TST-### (Task Templates)** - Individual work units from Day 28 tasks
2. **Break into STT-### (Step Templates)** - 5-30 minute actions within tasks (if granular)
3. **Group into MLT-### (Milestone Templates)** - Related tasks forming project phases
4. **Map to PRT-### (Project Templates)** - Check PRT-001 to PRT-009 or propose new
5. **Link TOL-### (Tools)** - Software/platforms used
6. **Reference GDS-### (Guides)** - Classification guides used

### CSV Outputs

**1. Employee Overview CSV (8 columns)**

| Column | Description | Example |
|--------|-------------|---------|
| Department | Department name | Development, Finance, Design |
| Employee_Name | Full employee name | Skichko Artem, Burda Anna |
| Employee_ID | Department code + number | DEV-002, LGN-001 |
| Role | Job title/position | Frontend Developer, Finance Manager |
| Active_Projects | Comma-separated PRT IDs | PRT-005, PRT-001 |
| Tasks_Count | Number of TST extracted | 3, 5, 2 |
| Key_Work_Day26 | Main achievement from Day 26 | Interactive video player implementation |
| Day28_Focus | Summary of Day 28 work | Media Library Update, 3 tasks identified |

**2. Task Extraction CSV (12 columns)**

| Column | Description | Example |
|--------|-------------|---------|
| Employee_ID | Employee identifier | DEV-002 |
| Employee_Name | Employee name | Skichko Artem |
| Department | Department code | DEV |
| TST_ID | Task template ID | TST-010 |
| Task_Name | Task description | Video Player Polish & Testing |
| Status | Task status emoji → text | New, In_Progress, Complete |
| Priority | Priority emoji → text | Critical, Medium, Low |
| Est_Hours | Estimated time (decimal) | 2.0, 0.75 |
| Project_ID | Mapped PRT | PRT-005 |
| Milestone_ID | Mapped MLT | MLT-006 |
| Tools_Used | TOL IDs | TOL-007, TOL-150 |
| Guide_Ref | GDS reference | GDS-011 |

## Implementation Approach

### 1. Python Script: `day28_todo_extraction.py`

**Core Components:**
- `EmployeeUpdate` dataclass: Structure for employee overview
- `Day28TodoExtractor` class: Main extraction engine
- File discovery: Recursively find all `*Day28_STRUCTURED.md` files
- Header parsing: Extract employee/department metadata
- Projects extraction: Extract active projects from PROJECTS OVERVIEW section
- Data sources parsing: Extract Day 26 key work and Day 28 focus
- CSV export: Write consolidated overview (NO detailed task blocks)

### 2. Data Extraction Strategy (MAIN_PROMPT v7.2 Workflow)

**Step 1: Extract Tasks (Task-First Approach)**

Parse `## 📋 TASKS FOR DAY 28` section:

```regex
#### \[([A-Z]+-[A-Z]+-\d+)\](.+?)\n
\*\*Priority:\*\*(.+?)\n
\*\*Project:\*\*(.+?)\n
\*\*Taxonomy Code:\*\*(.+?)\n
\*\*Status:\*\*(.+?)\n
\*\*Estimated Time:\*\*(.+?)\n
\*\*Description:\*\*(.+?)(?=\*\*|####|\Z)
```

Create TST-### for each task block

**Step 2: Bottom-Up Classification**

- Break tasks into STT-### if subtasks present
- Group related tasks into MLT-###
- Map to existing PRT-001 to PRT-009 (check PROJECTS OVERVIEW)
- Use GDS-011 decision tree

**Step 3: Enrich & Link**

- Extract TOL-### references from task descriptions
- Link to GDS-### guides used
- Validate against master CSVs

**Step 4: Extract Context**

```regex
## Employee: (.+?) \(([A-Z]+-\d+)\)
## Department: (.+?) \(([A-Z]+)\)
## Role: (.+?)
### Day 26.+?\n- \*\*Key Work:\*\* (.+?)\n
## 🎯 PROJECTS OVERVIEW → Extract PROJ-XXX-NNN IDs
```

### 3. Normalization Rules

**Text Cleaning:**
- Remove markdown symbols (#, **, ##) from extracted text
- Limit field lengths (Key_Work_Day26: 200 chars, Day28_Focus: 200 chars)
- Escape special characters for CSV compatibility
- Remove emoji prefixes (🎯, 📊, 📋, etc.)

**Project List Formatting:**
- Extract all PROJ-XXX-NNN identifiers
- Join with comma separator
- Example: "PROJ-DEV-005, PROJ-DEV-001, PROJ-LGN-001"

**Multi-line Content:**
- Collapse to single line with spaces
- Preserve key information only
- Remove bullet points and checkboxes

### 4. Handling File Structure Variations

**All files follow similar structure:**
1. Header (Employee, Department, Role)
2. DATA SOURCES ANALYSIS (Day 26, 27, 28)
3. PROJECTS OVERVIEW (Active Projects)
4. TASKS FOR DAY 28 section (SKIP THIS - not needed)

**Extraction Focus:**
- Parse header consistently across all files
- Extract project list from PROJECTS OVERVIEW
- Get Day 26 "Key Work" summary
- Get Day 28 "Content" or focus area
- Capture any warning notes (⚠️) in Notes field

**Handle Missing Sections:**
- If no Day 26 data → "No data available"
- If no projects listed → Empty string
- If Day 28 unclear → Extract from TODO section title or notes

### 5. Data Quality & Validation

**Validation Checks:**
- Missing employee name → Extract from filename
- Missing department → Extract from directory path
- Missing role → Set to "Not specified"
- Missing projects → Empty string
- Missing Day 26/28 data → Set to "No data available"

**Quality Metrics:**
- Total employees extracted (expect 16)
- Employees by department
- Employees with projects listed
- Employees with Day 26 data
- Missing data counts

### 6. Output Structure

```
C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\
└── CONSOLIDATED/                          [NEW DIRECTORY]
    ├── Day28_TODO_Consolidated.csv        [MAIN OUTPUT]
    ├── Day28_TODO_Summary.json            [Statistics]
    ├── Day28_TODO_Extraction_Report.md    [Summary report]
    └── extraction_log.txt                 [Debug/error log]
```

## Implementation Steps

### Step 1: Setup Environment
- Create `CONSOLIDATED` output directory
- Initialize Python script with required imports
- Define TodoTask dataclass
- Create Day28TodoExtractor class structure

### Step 2: Build Core Extraction
- Implement file discovery (`rglob("*Day28_STRUCTURED.md")`)
- Build header parser with regex
- Build projects section parser
- Build data sources section parser (Day 26, Day 28)
- Extract notes/warnings
- Test on single file (Skichko_Artem)

### Step 3: Add Normalization
- Implement text cleaning (remove markdown, emojis)
- Implement project list extraction and formatting
- Add multi-line content collapsing
- Limit field lengths
- Test on diverse files (Finance, Design, Executive)

### Step 4: Handle Variations
- Handle missing sections (Day 26, Day 27, Day 28 data)
- Extract notes and warnings
- Handle different project naming patterns
- Handle missing/optional fields
- Test on all 16 files

### Step 5: Export & Reporting
- Implement CSV export with proper encoding
- Generate summary statistics JSON
- Create extraction log with warnings/errors
- Create markdown summary report
- Validate output quality

### Step 6: Testing & Validation
- Run full extraction on all 16 files
- Verify CSV structure and data quality
- Check for encoding issues
- Validate normalized values
- Review extraction log for errors

## Expected Output

**CSV File Contents:**
- 16 rows (1 per employee)
- 8 columns populated
- Clean text without markdown/emojis
- Proper CSV escaping for special characters

**Summary Statistics:**
- Total employees: 16
- Employees by department breakdown
- Employees with active projects
- Employees with Day 26 data
- Extraction timestamp

## Critical Files to Read

1. **Development/Skichko_Artem_TODO_Day28_STRUCTURED.md**
   - Multiple active projects
   - Day 26 data available
   - Use for testing complete extraction

2. **Finance/Ponomarova_Kateryna_TODO_Day28_STRUCTURED.md**
   - Critical operations focus
   - Use for testing finance-specific content

3. **Lead_Generation/Burda_Anna_TODO_Day28_STRUCTURED.md**
   - Cross-department projects
   - Use for testing project extraction

## Success Criteria

- [ ] All 16 employee TODO files successfully parsed
- [ ] CSV file contains 16 employee rows (1 per employee)
- [ ] All 8 columns properly populated
- [ ] Clean text without markdown symbols or emojis
- [ ] No encoding errors in CSV output
- [ ] Summary statistics generated and accurate
- [ ] Extraction log documents any warnings/errors
- [ ] Manual spot-check confirms employee data accuracy

## Key Design Decisions

**Why CSV over JSON:**
- User specified CSV format
- Easy to open in Excel/Google Sheets for analysis
- Flat structure suitable for task data
- Enables filtering, sorting, pivot tables

**Why Single Consolidated File:**
- Easier cross-department analysis
- Single source of truth
- Can be filtered by department in Excel/Sheets
- Simpler to maintain and version

**Why Normalize Emojis:**
- CSV compatibility
- Consistent sorting/filtering
- Machine-readable for analytics
- Universal interpretation

**Why Limit Text Fields:**
- Prevent CSV cell overflow
- Maintain readability
- Force concise summaries
- Full details remain in source markdown files
