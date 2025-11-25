# Employee Profile Schema - Complete Data Structure Taxonomy

## Objective
Create a comprehensive schema documenting all data sources available in employee folders within Nov25 departments, mapping them to structured fields that can populate employee profiles in the TALENTS system.

## Schema Structure Overview

### Core Profile Fields (From Profile*.md Files)

| Field | Type | Required | Source | Description |
|-------|------|----------|--------|-------------|
| ID | Number | Yes | Profile*.md | Employee ID from CRM system |
| Name | String | Yes | Profile*.md | Full employee name |
| Age | Number | Optional | Profile*.md | Employee age |
| Country | String | Optional | Profile*.md | Country of residence |
| Start Date | Date | Optional | Profile*.md | Employment start date (MM/DD/YYYY) |
| Personal Email | String | Optional | Profile*.md | Personal email address |
| Work Email | String | Optional | Profile*.md | Work email address |
| Discord ID | String | Optional | Profile*.md | Discord user ID |
| Phone | String | Optional | Profile*.md | Phone number |
| Telegram | String | Optional | Profile*.md | Telegram username |
| Profession | String | Yes | Profile*.md | Job role/profession |
| Shift | String | Optional | Profile*.md | Work shift (Day/Night) |
| Rate | Number | Optional | Profile*.md | Hourly rate multiplier |
| Status | String | Yes | Profile*.md | Employment status (Available, Work, Project, Fired, LEFT, etc.) |
| Skills | Array | Optional | Profile*.md | Comma-separated skills list |
| Tools | Array | Optional | Profile*.md | Comma-separated tools list |
| Summary | Text | Optional | Profile*.md | Employee summary/bio |

---

## Extended Data Sources Taxonomy

### 1. Daily Work Logs (daily.md)

**Location Pattern**: `Nov25/{Department}/{Employee Name}/{DD}/daily.md` or `Week_X/{DD}/daily.md`

**Data Fields Extractable**:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| Work Activities | Array | Timestamped activities throughout the day | "10:00 - Reviewed client requirements" |
| Meeting Transcripts | Text | Whisper Flow transcripts from calls/meetings | Full conversation transcripts |
| Outcomes | Array | Results and deliverables from activities | "Completed design mockup" |
| Time Tracking | Object | Time spent on different activities | {activity: "Design", duration: "2h"} |
| Collaboration Notes | Text | Notes about working with team members | "Worked with John on API integration" |
| Blockers | Array | Issues encountered during work | "Waiting for client feedback" |
| Tools Used | Array | Tools utilized during the day | ["Figma", "Notion", "Slack"] |
| Projects Worked On | Array | Projects or tasks worked on | ["Project Alpha", "Bug Fixes"] |

**Mapping to Schema**:
- **Skills**: Extract tools/technologies mentioned → update Skills array
- **Tools**: Extract tools used → update Tools array
- **Work History**: Aggregate activities → create work history timeline
- **Performance Metrics**: Calculate activity frequency, completion rates

---

### 2. Strategic Plans (plans.md)

**Location Pattern**: `Nov25/{Department}/{Employee Name}/{DD}/plans.md`

**Data Fields Extractable**:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| Strategic Goals | Array | High-level objectives | "Improve client communication" |
| Prioritized Actions | Array | Prioritized action items | ["Task 1", "Task 2"] |
| Expected Outcomes | Array | Anticipated results | "Complete API integration" |
| Dependencies | Array | Blocking items or prerequisites | ["Client approval", "Design assets"] |
| Cross-Department Items | Array | Items requiring other departments | ["Need Dev support for API"] |
| Timeline | Object | Expected completion dates | {task: "Design", deadline: "2025-01-20"} |
| Risk Factors | Array | Potential blockers or risks | ["Tight deadline", "Unclear requirements"] |

**Mapping to Schema**:
- **Current Projects**: Extract active projects → populate Projects field
- **Responsibilities**: Extract primary responsibilities → update Summary
- **Collaboration Patterns**: Identify cross-department work → track relationships

---

### 3. Task Breakdowns (task.md)

**Location Pattern**: `Nov25/{Department}/{Employee Name}/{DD}/task.md`

**Data Fields Extractable**:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| Action Items | Array | Specific tasks to complete | ["Create wireframe", "Update documentation"] |
| Task Steps | Array | Detailed step-by-step instructions | ["Step 1: Research", "Step 2: Design"] |
| Resources | Array | Links and reference materials | ["https://example.com/guide"] |
| Dependencies | Array | Task dependencies | ["Task A must complete first"] |
| Owner/Assignee | String | Task owner information | "Assigned to: John Doe" |
| Status | String | Task completion status | "In Progress", "Completed", "Blocked" |
| Priority | String | Task priority level | "High", "Medium", "Low" |
| Related Projects | Array | Associated projects | ["Project Alpha"] |
| Tools Required | Array | Tools needed for task | ["Figma", "Notion"] |

**Mapping to Schema**:
- **Skills**: Extract skills demonstrated in tasks → update Skills
- **Tools**: Extract tools used → update Tools
- **Work Patterns**: Analyze task complexity and types → performance insights
- **Task Templates**: Identify recurring task patterns → create templates

---

### 4. Workflow Documentation (README.md)

**Location Pattern**: `Nov25/{Department}/{Employee Name}/README.md`

**Data Fields Extractable**:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| Workflow Guides | Text | Department-specific processes | "Daily Workflow Guide" |
| Onboarding Info | Text | Employee onboarding documentation | Setup instructions |
| Tool Configurations | Object | Tool setup and configuration | {VS Code: "extensions.json"} |
| Best Practices | Array | Documented best practices | ["Always use templates", "Update daily.md"] |
| Yellow Card System | Object | Quality control metrics | {yellow_cards: 0, max: 3} |
| Folder Structure | Object | Expected folder organization | {daily: "DD/daily.md"} |

**Mapping to Schema**:
- **Onboarding Date**: Extract from workflow documentation
- **Workflow Compliance**: Track adherence to documented processes
- **Tool Proficiency**: Document tool setup and usage

---

### 5. Additional Notes (notes.md)

**Location Pattern**: `Nov25/{Department}/{Employee Name}/notes.md`

**Data Fields Extractable**:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| Personal Notes | Text | Employee's personal notes | "Remember to check X" |
| Learning Notes | Text | Notes from learning/training | "New technique learned" |
| Reference Information | Text | Reference materials or links | "See: example.com" |
| Reminders | Array | Important reminders | ["Follow up with client"] |

**Mapping to Schema**:
- **Learning & Development**: Extract learning notes → track growth
- **Personal Preferences**: Extract preferences → customize workflows

---

### 6. Structured Data (JSON Files)

**Location Pattern**: `Nov25/{Department}/{Employee Name}/**/*.json`

**Data Types Found**:

#### 6.1 Task Templates (TEMPLATE-TASK-*.json)

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| Task ID | String | Unique task identifier | "TEMPLATE-TASK-AI-001" |
| Task Name | String | Task name/title | "Process Video Transcriptions" |
| Description | Text | Task description | "Process video transcriptions with taxonomy extraction" |
| Department | String | Associated department | "AI" |
| Actions | Array | Actions involved | ["Process", "Extract", "Analyze"] |
| Objects | Array | Objects worked with | ["Video", "Transcription", "Taxonomy"] |
| Tools | Array | Tools used | ["Claude", "Cursor", "n8n"] |
| Dependencies | Array | Task dependencies | ["TASK-002"] |
| Status | String | Task status | "Completed", "In Progress" |

**Mapping to Schema**:
- **Skills**: Extract from Actions and Tools → update Skills
- **Tools**: Extract Tools array → update Tools
- **Work Patterns**: Analyze task types → identify expertise areas

#### 6.2 Employee Exports (employees_filtered_for_talent.json)

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| Employee Data | Object | Complete employee record | Full CRM export |
| Filter Criteria | Object | Filtering parameters | {status: "Available"} |
| Summary Stats | Object | Aggregate statistics | {total: 19, matched: 19} |

**Mapping to Schema**:
- **Complete Profile**: Use as source of truth for core fields
- **Status Updates**: Track status changes over time
- **Department Assignment**: Verify department associations

---

### 7. Folder Structure Analysis

**Patterns Identified**:

| Pattern | Description | Data Extractable |
|---------|-------------|------------------|
| `{DD}/` | Daily folders (e.g., 15/, 17/, 18/) | Work frequency, activity patterns |
| `Week_X/` | Weekly organization | Weekly work patterns, project timelines |
| `Dropbox guid/` | Special guides/documentation | Onboarding materials, process docs |
| `Tasks/` | Task-specific folders | Task organization, project structure |

**Metrics Extractable**:
- **Work Frequency**: Count of daily folders → activity level
- **Consistency**: Regularity of folder creation → reliability metric
- **Organization Level**: Folder structure quality → organizational skills
- **Project Duration**: Week_X folders → project engagement length

**Mapping to Schema**:
- **Activity Metrics**: Calculate work frequency and consistency
- **Organization Score**: Assess folder structure quality
- **Project Engagement**: Track project participation

---

### 8. Overview Nov25 Analysis Files

**Location**: `Nov25/AI/Overview Nov25/{Department}_Department_Deep_Analysis.md`

**Data Fields Extractable**:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| Employee Reviews | Object | Performance reviews | {rating: 5, feedback: "Excellent"} |
| Team Composition | Object | Team structure | {size: 3, roles: ["PM", "PE"]} |
| Workload Assessment | String | Workload level | "VERY HIGH", "MODERATE" |
| Primary Responsibilities | Array | Main job responsibilities | ["Project management", "Coordination"] |
| Current Projects | Array | Active projects | ["File System Project", "CRM Migration"] |
| Skills Assessment | Object | Skills evaluation | {technical: 5, soft: 4} |
| Performance Metrics | Object | Quantitative metrics | {tasks_completed: 50, quality: 95%} |
| Department Role | String | Role in department | "Department Lead", "Team Member" |

**Mapping to Schema**:
- **Performance Data**: Extract reviews and metrics → performance tracking
- **Role & Responsibilities**: Update Position and Summary fields
- **Workload**: Track workload levels → capacity planning
- **Skills Validation**: Cross-reference Skills field with assessments

---

## Complete Schema Field Mapping

### Core Profile (Profile*.md)
```
ID → Employee.ID
Name → Employee.Name
Age → Employee.Age
Country → Employee.Country
Start Date → Employee.StartDate
Contact Information → Employee.Contacts.*
Position → Employee.Position.*
Skills → Employee.Skills[]
Tools → Employee.Tools[]
Summary → Employee.Summary
```

### Extended Data (daily.md, plans.md, task.md)
```
Work Activities → Employee.WorkHistory[]
Meeting Transcripts → Employee.Meetings[]
Current Projects → Employee.Projects[]
Task Patterns → Employee.TaskTemplates[]
Collaboration → Employee.Collaborations[]
Performance Metrics → Employee.Metrics{}
```

### Documentation (README.md, notes.md)
```
Workflow Compliance → Employee.Compliance{}
Onboarding Info → Employee.Onboarding{}
Learning Notes → Employee.Learning[]
Tool Configurations → Employee.ToolConfigs{}
```

### Structured Data (JSON)
```
Task Templates → Employee.TaskTemplates[]
Employee Exports → Employee.CRMData{}
Filter Criteria → Employee.Filters{}
```

### Folder Structure
```
Work Frequency → Employee.Metrics.ActivityFrequency
Organization Score → Employee.Metrics.OrganizationScore
Project Engagement → Employee.Projects[]
```

### Analysis Files (Overview Nov25)
```
Performance Reviews → Employee.Reviews[]
Workload → Employee.Metrics.Workload
Role Assessment → Employee.Position.Role
Skills Validation → Employee.Skills.Validated[]
```

---

## Data Source Priority Matrix

| Priority | Source | Use Case | Update Frequency |
|----------|--------|----------|------------------|
| **P0** | Profile*.md | Core employee data | On creation/update |
| **P1** | daily.md | Work activities, skills, tools | Daily |
| **P1** | Overview Nov25 | Performance reviews, role | Monthly/Quarterly |
| **P2** | plans.md | Current projects, goals | Weekly |
| **P2** | task.md | Task patterns, skills | Weekly |
| **P3** | README.md | Workflow compliance | On change |
| **P3** | notes.md | Learning, preferences | As needed |
| **P4** | JSON files | Structured data, templates | On creation |
| **P4** | Folder structure | Activity metrics | Monthly |

---

## Data Extraction Rules

### Rule 1: Skills Extraction
- **Source**: Profile*.md Skills field, daily.md activities, task.md tools, JSON task templates
- **Method**: Merge all sources, deduplicate, maintain comma-separated format
- **Update**: Add new skills from daily.md and task.md activities

### Rule 2: Tools Extraction
- **Source**: Profile*.md Tools field, daily.md tools used, task.md tools required, JSON templates
- **Method**: Merge all sources, deduplicate, categorize by type
- **Update**: Add new tools from daily work logs

### Rule 3: Status Updates
- **Source**: Profile*.md Status field, Overview Nov25 analysis, folder location (Left/)
- **Method**: Check folder path for "Left/" or "LEFT/" → set Status to "LEFT"
- **Update**: Automatic on folder detection, manual on profile update

### Rule 4: Work History
- **Source**: daily.md files aggregated chronologically
- **Method**: Extract activities, outcomes, projects from all daily.md files
- **Update**: Append new entries daily

### Rule 5: Performance Metrics
- **Source**: Overview Nov25 analysis files, daily.md consistency, folder structure
- **Method**: Calculate activity frequency, completion rates, organization scores
- **Update**: Recalculate monthly

---

## Schema Validation Rules

1. **ID Uniqueness**: Employee ID must be unique across all profiles
2. **Required Fields**: ID, Name, Profession, Status are mandatory
3. **Date Format**: Start Date must be MM/DD/YYYY format
4. **Status Values**: Must be one of: Available, Work, Project, Part Time, On Leave, Fired, LEFT
5. **Skills Format**: Comma-separated list, no duplicates
6. **Tools Format**: Comma-separated list, no duplicates
7. **Email Validation**: Email fields must contain "@" symbol if not "Not specified"
8. **Phone Format**: Phone numbers should be numeric strings
9. **Discord ID**: Must be numeric string if not "Not specified"
10. **Rate**: Must be numeric (typically 0.5, 0.75, or 1.0)

---

## Department-Specific Data Patterns

### AI Department
- **Common Files**: daily.md, plans.md, task.md, README.md, JSON task templates
- **Special Patterns**: Overview Nov25 analysis files, automation workflows
- **Tools**: Claude, ChatGPT, Cursor, n8n, Python scripts
- **Skills**: Prompt engineering, automation, project management

### Design Department
- **Common Files**: daily.md, plans.md, task.md, README.md
- **Special Patterns**: Design deliverables, portfolio links
- **Tools**: Figma, Adobe Suite, Canva, design systems
- **Skills**: UI/UX design, graphic design, illustration

### Dev Department
- **Common Files**: daily.md, plans.md, task.md, notes.md, README.md
- **Special Patterns**: Code repositories, technical documentation
- **Tools**: VS Code, Cursor, Git, development frameworks
- **Skills**: Programming languages, frameworks, development methodologies

### LG (Lead Generation) Department
- **Common Files**: daily.md, plans.md, task.md, README.md
- **Special Patterns**: Lead tracking, outreach metrics
- **Tools**: CRM systems, email tools, LinkedIn, research tools
- **Skills**: Lead generation, outreach, research, communication

### Video Department
- **Common Files**: daily.md, plans.md, task.md, README.md
- **Special Patterns**: Video project folders, editing workflows
- **Tools**: Video editing software, transcription tools, content platforms
- **Skills**: Video editing, content creation, post-production

---

## Integration Points

### LIBRARIES Taxonomy Integration
- **Professions**: Map Employee.Profession → PRF-### (Professions taxonomy)
- **Tools**: Map Employee.Tools[] → TLS-### (Tools taxonomy)
- **Skills**: Map Employee.Skills[] → SKL-### (Skills taxonomy)
- **Departments**: Map Employee.Department → DPT-### (Departments taxonomy)
- **Statuses**: Map Employee.Status → STS-### (Statuses taxonomy)

### TASK_MANAGERS Integration
- **Task Templates**: Link Employee.TaskTemplates[] → TSK-### (Task templates)
- **Projects**: Link Employee.Projects[] → PRJ-### (Projects)
- **Actions**: Extract from tasks → ACT-### (Actions taxonomy)

### Cross-Entity Relationships
```
Employee (TALENTS)
  ├─ Profession → PRF-### (LIBRARIES)
  ├─ Department → DPT-### (LIBRARIES)
  ├─ Tools → TLS-### (LIBRARIES)
  ├─ Skills → SKL-### (LIBRARIES)
  ├─ Projects → PRJ-### (TASK_MANAGERS)
  └─ Tasks → TSK-### (TASK_MANAGERS)
```

---

## Data Collection Workflow

### Step 1: Profile Collection
1. Scan `Nov25/{Department}/` for all `Profile*.md` files
2. Extract core profile data (ID, Name, Contact, Position, Skills, Tools, Summary)
3. Map to schema fields
4. Validate required fields

### Step 2: Extended Data Collection
1. For each employee folder, scan for:
   - `daily.md` files in dated folders
   - `plans.md` files
   - `task.md` files
   - `README.md` files
   - `notes.md` files
   - `*.json` files
2. Extract relevant data according to field mapping
3. Aggregate and merge with core profile data

### Step 3: Analysis Integration
1. Check `Nov25/AI/Overview Nov25/` for department analysis files
2. Extract employee-specific reviews and metrics
3. Cross-reference with profile data
4. Update performance metrics

### Step 4: Folder Structure Analysis
1. Analyze folder structure patterns
2. Calculate activity metrics
3. Assess organization quality
4. Track project engagement

### Step 5: Schema Population
1. Merge all data sources
2. Apply validation rules
3. Deduplicate arrays (Skills, Tools)
4. Generate complete employee profile
5. Store in `ENTITIES/TALENTS/Employees/profiles/`

---

## Output Schema Format

### Complete Employee Profile Structure

```json
{
  "id": 37226,
  "name": "Artemchuk Nikolay",
  "age": 33,
  "country": "Ukraine",
  "start_date": "8/19/2025",
  "contacts": {
    "personal_email": "artemchuknn@gmail.com",
    "work_email": "Not specified",
    "discord_id": "910144676881903646",
    "phone": "380954035391",
    "telegram": "@twinklelilsta"
  },
  "position": {
    "profession": "project manager",
    "shift": "Day",
    "rate": 1,
    "status": "Work",
    "department": "AI",
    "role": "Department Lead"
  },
  "skills": [
    "Account Management",
    "Agile",
    "Data Processing",
    "Kanban",
    "project management",
    "SCRUM",
    "Waterfall"
  ],
  "tools": [
    "Asana",
    "CMS",
    "CRM",
    "Elementor",
    "Facebook",
    "Figma",
    "Google Data Studio",
    "Google My Business",
    "Instagram",
    "Jira",
    "LinkedIn",
    "Meistertask",
    "Miro",
    "Monday",
    "Notion",
    "Slack",
    "Trello",
    "wordpress"
  ],
  "summary": "Deep expert-level knowledge...",
  "work_history": [
    {
      "date": "2025-01-18",
      "activities": ["..."],
      "outcomes": ["..."],
      "projects": ["..."]
    }
  ],
  "current_projects": [
    "File System Project rollout",
    "LG Department strategic evaluation"
  ],
  "metrics": {
    "activity_frequency": "High",
    "workload": "VERY HIGH",
    "organization_score": 95,
    "completion_rate": 98
  },
  "reviews": [
    {
      "date": "2025-11-16",
      "rating": 5,
      "feedback": "Excellent performance"
    }
  ],
  "source_files": {
    "profile": "Nov25/AI/Artemchuk Nikolay/Profile Project manager, Lead generator Artemchuk Nikolay.md",
    "daily_logs": ["Nov25/AI/Artemchuk Nikolay/18/daily.md", "..."],
    "analysis": "Nov25/AI/Overview Nov25/AI_Department_Deep_Analysis.md"
  }
}
```

---

## Notes

- **Schema is extensible**: New data sources can be added following the same taxonomy pattern
- **Data priority**: Core profile data (Profile*.md) takes precedence, extended data supplements
- **Automation ready**: Schema designed for automated data extraction and population
- **Taxonomy aligned**: Follows LIBRARIES taxonomy structure for cross-entity relationships
- **Validation enforced**: All data must pass validation rules before schema population
- **Source tracking**: All fields maintain reference to source file for traceability

