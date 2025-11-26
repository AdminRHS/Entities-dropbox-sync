# PMT-070: Daily Report Entity Mapping v2.1

**Prompt ID:** PMT-070
**Version:** 2.1
**Department:** Utilities
**Category:** Daily Report Entity Mapping
**Date:** 2025-11-19
**Status:** Active

---

## Purpose

Map daily activity descriptions from department reports to TASK_MANAGERS entity hierarchy using token-efficient format.

**Input:** Activity descriptions from daily work
**Output:** Entity mappings in format `TST-###_Name → MLT-###_Name → PRT-###_Name`

---

## Token-Efficient Format ⚡

**Pattern:** `{ISO-###}_{Name_With_Underscores}`

**Examples:**
- `PRT-001_AI_Tutorial_Research`
- `MLT-002_Data_Inventory`
- `TST-055_Process_Department_Task_Files`
- `STT-155_Conduct_Client_Brand_Discovery`

**Benefits:** 60% token reduction for batch processing

---

## Data Sources

### CSV Master Files

**Locations:**
```
ENTITIES/TASK_MANAGERS/Project_Templates/Project_Templates_Master_List.csv
ENTITIES/TASK_MANAGERS/Milestone_Templates/Milestone_Templates_Master_List.csv
ENTITIES/TASK_MANAGERS/Task_Templates/Task_Templates_Master_List.csv
ENTITIES/TASK_MANAGERS/Step_Templates/Taxonomy/Step_Templates_Master_List.csv
```

**Schema:**
```csv
New_ID, Entity_Type, Current_ID, Name, Description, Department, File_Path, Status
```

**Usage:**
- Extract `New_ID` (e.g., TST-001)
- Extract `Name` (e.g., AI Powered HTML Parsing)
- Format as: `TST-001_AI_Powered_HTML_Parsing`

---

## 5-Step Mapping Process

### Step 1: Analyze Activity

**Extract Components:**
- **Action Verb:** Process, Extract, Create, Validate, Configure, Review
- **Object/Target:** Task Files, Taxonomy, CV Data, Reports, Code
- **Context:** Department, folders, systems, tools

**Example:**
```
Activity: "Process AI department task files from folders 04-11"

Analysis:
→ Action: Process
→ Object: Task Files
→ Context: AI department, folders 04-11
```

---

### Step 2: Match to Task Template (TST-###)

**Algorithm:**

1. **Extract Keywords:** Remove stop words, identify key terms
2. **Search Tasks CSV:** Match against Name and Description columns
3. **Score Confidence:**
   - High: >90% (action + object + context match)
   - Medium: 70-89% (action + object match)
   - Low: <70% (partial match only)
4. **Filter by Department:** Prioritize dept-matching tasks
5. **Return Best Match:** Highest confidence with entity details

**Confidence Scoring:**
```python
confidence = (
    keyword_matches * 0.4 +
    action_match * 0.3 +
    department_match * 0.2 +
    context_match * 0.1
)
```

**Example:**
```
Activity: "Process AI department task files from folders 04-11"

Keywords: ["process", "task files", "AI department"]
Search: Task_Templates_Master_List.csv

Match Found:
→ TST-055_Process_Department_Task_Files
→ Confidence: 95%
→ Department: AID
→ Status: Active
```

---

### Step 3: Roll Up to Milestone (MLT-###)

**Lookup Process:**

1. Find TST-### row in `Task_Templates_Master_List.csv`
2. Read `milestone_template_id` column value
3. Lookup MLT-### in `Milestone_Templates_Master_List.csv`
4. Extract milestone Name field
5. Format as: `MLT-###_Name`

**Example:**
```
TST-055_Process_Department_Task_Files
↓
Task CSV Row: milestone_template_id = MLT-002
↓
Milestone CSV Row: Name = "Data Inventory"
↓
Result: MLT-002_Data_Inventory
```

---

### Step 4: Roll Up to Project (PRT-###)

**Lookup Process:**

1. Find MLT-### row in `Milestone_Templates_Master_List.csv`
2. Read `project_template_id` column value
3. Lookup PRT-### in `Project_Templates_Master_List.csv`
4. Extract project Name field
5. Format as: `PRT-###_Name`

**Example:**
```
MLT-002_Data_Inventory
↓
Milestone CSV Row: project_template_id = PRT-007
↓
Project CSV Row: Name = "System Analysis"
↓
Result: PRT-007_System_Analysis
```

---

### Step 5: Validate Entity Chain

**Validation Checklist:**

- ✅ TST-### exists in Tasks CSV
- ✅ MLT-### exists in Milestones CSV
- ✅ PRT-### exists in Projects CSV
- ✅ TST belongs to MLT (via milestone_template_id)
- ✅ MLT belongs to PRT (via project_template_id)
- ✅ All entities Status = Active or In Progress
- ✅ Department alignment correct (or explained)

**If Validation Fails:**
- Flag for manual review
- Provide best-guess with low confidence
- Suggest "Operational/Maintenance" if non-project work

---

## Complete Mapping Example

### Input Activity:
```
"Process AI department task files from folders 04-11"
```

### Step-by-Step Mapping:

**Step 1: Analyze**
```
Action: Process
Object: Task Files
Context: AI department, folders 04-11
```

**Step 2: Match Task**
```
Keywords: ["process", "task files", "AI department"]
Search Tasks CSV
→ Match: TST-055
→ Name: Process Department Task Files
→ Confidence: 95%
→ Department: AID
→ Status: Active
```

**Step 3: Find Milestone**
```
TST-055 → milestone_template_id = MLT-002
MLT-002 → Name: Data Inventory
```

**Step 4: Find Project**
```
MLT-002 → project_template_id = PRT-007
PRT-007 → Name: System Analysis
```

**Step 5: Validate**
```
✅ TST-055 exists
✅ MLT-002 exists
✅ PRT-007 exists
✅ TST-055 belongs to MLT-002
✅ MLT-002 belongs to PRT-007
✅ All entities Active
✅ Department: AID matches report
```

### Output Format:
```markdown
**Entity:** TST-055_Process_Department_Task_Files → MLT-002_Data_Inventory → PRT-007_System_Analysis
```

---

## Department-Specific Patterns

### AI Department (AID)

**Common Projects:**
- PRT-001_AI_Tutorial_Research
- PRT-006_Research_Taxonomy_Pipeline
- PRT-007_System_Analysis

**Common Tasks:**
- TST-015_Extract_Taxonomy_Tutorial_Videos
- TST-055_Process_Department_Task_Files
- TST-058_Extract_Tasks_Daily_Files

**Activity Patterns:**
- Infrastructure configs → Operational/Maintenance
- Tool integrations → TST-specific or Operational
- Prompt engineering → PRT-001 or PRT-006
- Framework development → Operational/Technical Debt

---

### HR Department (HRM)

**Common Projects:**
- PRT-003_HR_Automation

**Common Tasks:**
- TST-039_Setup_n8n_CV_Screening
- TST-048_Create_Scoring_Algorithm
- TST-053_CV_Parser_Development

**Activity Patterns:**
- Candidate sourcing → Operational/Recruitment
- Interview scheduling → Operational/Recruitment
- System setup → PRT-003 tasks
- Employee onboarding → Operational/HR_Operations

---

### Design Department (DGN)

**Common Projects:**
- PRT-008_VIDEO_Production
- Client projects: DGN-CLIENT-###

**Common Tasks:**
- TST-012_Create_Logo_Concepts
- TST-010_UI_UX_Design
- TST-009_Design_System_Development

**Activity Patterns:**
- Client design work → Client project PRT-###
- Internal design systems → TST-009 or Operational
- Video thumbnails → PRT-008 support
- Brand assets → Depends on initiative

---

### Development Department (DEV)

**Common Projects:**
- PRT-002_MCP_Automation_Stack
- PRT-003_HR_Automation (Support)

**Common Tasks:**
- TST-001_AI_Powered_HTML_Parsing
- TST-042_Configure_ATS_Integration
- TST-045_Build_CV_Parser_Workflow

**Activity Patterns:**
- Feature development → PRT-specific tasks
- Bug fixes → Operational/Maintenance
- Integration work → Cross-project TST
- Testing/QA → Related to parent TST

---

### Finance Department (FIN)

**Common Activities:** Mostly Operational/Maintenance

**Patterns:**
- Month-end closing → Operational/Routine
- Invoice processing → Operational/Routine
- Bank reconciliation → Operational/Routine
- System improvements → May map to automation PRT

**Note:** Finance has fewer project-mapped activities; focus on operational excellence.

---

## Special Cases

### Case 1: Operational/Maintenance Work

**When:** Routine department operations not tied to specific projects

**Output Format:**
```markdown
**Entity:** Operational/Maintenance (No project mapping)
**Category:** Administrative Operations
```

**Examples:**
- Daily email communications
- Routine administrative tasks
- General department maintenance
- Standard operating procedures

---

### Case 2: Multi-Department Projects

**When:** Multiple departments contribute to same project

**Output Format:**
```markdown
**Entity:** TST-###_Name → MLT-###_Name → PRT-###_Name
**Role:** Lead | Support | Contributor
**Departments:** AID (Lead), DEV (Support), HRM (Support)
```

**Example:**
```markdown
**Entity:** TST-042_Configure_ATS_Integration → MLT-010_CV_Screening_Setup → PRT-003_HR_Automation
**Role:** Support (Development)
**Lead Department:** HRM
```

---

### Case 3: Low Confidence Match (<70%)

**Option A - Manual Assignment:**
```markdown
**Entity:** TST-###_Name (Manual Assignment - Review Recommended)
**Confidence:** 65%
```

**Option B - Flag for Review:**
```markdown
**Entity:** Pending Manual Review
**Reason:** No high-confidence match found
**Best Guess:** TST-### (60%)
```

**Option C - Operational:**
```markdown
**Entity:** Operational/Maintenance
**Reason:** No applicable project/task mapping
```

---

### Case 4: Cross-Project Activities

**When:** Single activity contributes to multiple projects

**Output Format:**
```markdown
**Primary Entity:** TST-###_Name → MLT-###_Name → PRT-###_Name
**Supporting:** PRT-###_Name (context/role)
```

**Example:**
```markdown
**Primary Entity:** TST-007_Create_Video_Thumbnails → MLT-004_Video_Asset_Creation → PRT-008_VIDEO_Production
**Supporting:** PRT-001_AI_Tutorial_Research (thumbnails for AI tutorials)
```

---

## Output Format for Daily Reports

### Single Activity Mapping

```markdown
#### Activity 1: [Activity Description]
- **Entity:** TST-###_Name → MLT-###_Name → PRT-###_Name
- **Confidence:** [High/Medium/Low] (95%)
- **Time:** [Hours]
- **Status:** [In Progress/Completed/Blocked]
```

### Multiple Activity Summary

```markdown
## Section 4: Task Sequences and Entity Mapping

### AI Department Activities (Nov 19, 2025)

#### Activity 1: Process department task files
- **Entity:** TST-055_Process_Department_Task_Files → MLT-002_Data_Inventory → PRT-007_System_Analysis
- **Time:** 2.5 hours
- **Status:** Completed

#### Activity 2: Extract taxonomy from tutorial videos
- **Entity:** TST-015_Extract_Taxonomy_Tutorial_Videos → MLT-001_Content_Analysis → PRT-001_AI_Tutorial_Research
- **Time:** 3 hours
- **Status:** In Progress

#### Activity 3: Daily administrative tasks
- **Entity:** Operational/Maintenance
- **Time:** 0.5 hours
- **Status:** Completed
```

---

## Validation Rules

### Entity ID Format
- **Pattern:** `{ISO-###}_{Name_With_Underscores}`
- **ISO Codes:** PRT, MLT, TST, STT only
- **No Leading Zeros:** TST-001 (not TST-0001)
- **Underscores in Names:** Process_Task_Files (not Process Task Files)

### Entity Status
- **Must Be:** Active, In Progress, or Paused
- **Blocked:** Note in Challenges section
- **Completed:** Don't include in active work mappings

### Department Alignment
- Task department should match report department OR
- Cross-department tasks require coordination note
- Misaligned departments need explanation

### Hierarchy Integrity
- TST must belong to MLT (via milestone_template_id)
- MLT must belong to PRT (via project_template_id)
- No orphaned entities (all must validate upward)

---

## Error Handling

### No Task Match Found

**Actions:**
1. Broaden keyword search (use synonyms)
2. Check if operational work (not project-based)
3. Review recent department tasks for context
4. Flag for manual assignment
5. Default to Operational/Maintenance if appropriate

**Output:**
```markdown
**Entity:** Pending Manual Review
**Reason:** No confident match found (best: 45%)
**Keywords Searched:** [process, files, automation]
**Recommendation:** Review Task_Templates_Master_List.csv for department
```

---

### Invalid Entity Chain

**Actions:**
1. Verify each ID exists in respective CSV
2. Check milestone_template_id and project_template_id fields
3. Confirm Status = Active or In Progress
4. Report data integrity issue to system admin

**Output:**
```markdown
**Entity:** TST-###_Name (VALIDATION FAILED)
**Issue:** Milestone MLT-### not found in Milestones CSV
**Action Required:** Data integrity check needed
```

---

### Department Mismatch

**Actions:**
1. Check if cross-department project (valid)
2. Verify department code in CSV
3. Confirm Support/Contributor role if valid
4. Flag if true mismatch (task assigned to wrong dept)

**Output:**
```markdown
**Entity:** TST-###_Name → MLT-###_Name → PRT-###_Name
**Note:** Cross-department project (Task Dept: DEV, Report Dept: HRM)
**Role:** Support (Development support for HR Automation)
```

---

### Multiple High-Confidence Matches

**Actions:**
1. Use department filtering to narrow
2. Check activity context for disambiguation
3. Review recent project history for department
4. Select most recent/currently active
5. Flag for review if still uncertain

**Output:**
```markdown
**Entity:** TST-###_Name (Selected from 2 matches)
**Alternative:** TST-###_Name (89% confidence)
**Selection Criteria:** Department match + recent activity
```

---

## Pseudo-Code Implementation

```python
def map_activity_to_entities(activity_desc, department, date):
    """
    Map activity description to TASK_MANAGERS entity hierarchy

    Args:
        activity_desc: Description of work performed
        department: Department code (AID, HRM, DEV, etc.)
        date: Activity date (for context)

    Returns:
        dict with task, milestone, project in token-efficient format
    """

    # Step 1: Extract keywords
    keywords = extract_keywords(activity_desc)
    action = extract_action_verb(activity_desc)
    obj = extract_object(activity_desc)
    context = extract_context(activity_desc)

    # Step 2: Search Tasks CSV
    tasks_df = load_csv('Task_Templates_Master_List.csv')
    matches = search_tasks(
        df=tasks_df,
        keywords=keywords,
        action=action,
        object=obj,
        department=department
    )

    # Score and rank matches
    scored_matches = score_confidence(matches, activity_desc, department)
    best_match = get_highest_confidence(scored_matches)

    # Check confidence threshold
    if best_match.confidence < 0.7:
        return {
            "status": "low_confidence",
            "task_id": best_match.id,
            "confidence": best_match.confidence,
            "recommendation": "manual_review"
        }

    # Step 3: Find milestone
    task_row = tasks_df[tasks_df['New_ID'] == best_match.id].iloc[0]
    milestone_id = task_row['milestone_template_id']

    milestones_df = load_csv('Milestone_Templates_Master_List.csv')
    milestone_row = milestones_df[milestones_df['New_ID'] == milestone_id].iloc[0]

    # Step 4: Find project
    project_id = milestone_row['project_template_id']

    projects_df = load_csv('Project_Templates_Master_List.csv')
    project_row = projects_df[projects_df['New_ID'] == project_id].iloc[0]

    # Step 5: Validate chain
    validation = validate_chain(
        task_id=best_match.id,
        milestone_id=milestone_id,
        project_id=project_id,
        department=department
    )

    if not validation.success:
        return {
            "status": "validation_failed",
            "issue": validation.error,
            "task_id": best_match.id
        }

    # Format entities with token-efficient pattern
    task_name = task_row['Name'].replace(' ', '_')
    milestone_name = milestone_row['Name'].replace(' ', '_')
    project_name = project_row['Name'].replace(' ', '_')

    return {
        "status": "success",
        "task": f"{best_match.id}_{task_name}",
        "milestone": f"{milestone_id}_{milestone_name}",
        "project": f"{project_id}_{project_name}",
        "confidence": best_match.confidence,
        "department_alignment": check_department_alignment(
            task_dept=task_row['Department'],
            report_dept=department
        )
    }


def extract_keywords(text):
    """Extract meaningful keywords, remove stop words"""
    stop_words = ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for']
    words = text.lower().split()
    return [w for w in words if w not in stop_words and len(w) > 2]


def extract_action_verb(text):
    """Extract primary action verb from activity description"""
    action_verbs = [
        'process', 'extract', 'create', 'build', 'configure', 'setup',
        'review', 'analyze', 'design', 'develop', 'implement', 'test',
        'validate', 'update', 'fix', 'deploy', 'monitor', 'optimize'
    ]
    words = text.lower().split()
    for verb in action_verbs:
        if verb in words:
            return verb
    return None


def score_confidence(matches, activity_desc, department):
    """Score matches based on keyword overlap, dept match, context"""
    scored = []
    keywords = set(extract_keywords(activity_desc))

    for match in matches:
        task_keywords = set(extract_keywords(match['Name'] + ' ' + match['Description']))

        keyword_overlap = len(keywords & task_keywords) / max(len(keywords), 1)
        dept_match = 1.0 if match['Department'] == department else 0.5
        status_active = 1.0 if match['Status'] in ['Active', 'In Progress'] else 0.0

        confidence = (
            keyword_overlap * 0.5 +
            dept_match * 0.3 +
            status_active * 0.2
        )

        scored.append({
            'id': match['New_ID'],
            'name': match['Name'],
            'confidence': confidence,
            'department': match['Department']
        })

    return sorted(scored, key=lambda x: x['confidence'], reverse=True)


def validate_chain(task_id, milestone_id, project_id, department):
    """Validate entity chain integrity"""

    # Check all entities exist
    tasks_df = load_csv('Task_Templates_Master_List.csv')
    milestones_df = load_csv('Milestone_Templates_Master_List.csv')
    projects_df = load_csv('Project_Templates_Master_List.csv')

    if task_id not in tasks_df['New_ID'].values:
        return {"success": False, "error": f"Task {task_id} not found"}

    if milestone_id not in milestones_df['New_ID'].values:
        return {"success": False, "error": f"Milestone {milestone_id} not found"}

    if project_id not in projects_df['New_ID'].values:
        return {"success": False, "error": f"Project {project_id} not found"}

    # Verify hierarchy links
    task_row = tasks_df[tasks_df['New_ID'] == task_id].iloc[0]
    if task_row['milestone_template_id'] != milestone_id:
        return {"success": False, "error": "Task does not belong to Milestone"}

    milestone_row = milestones_df[milestones_df['New_ID'] == milestone_id].iloc[0]
    if milestone_row['project_template_id'] != project_id:
        return {"success": False, "error": "Milestone does not belong to Project"}

    # Check status
    if task_row['Status'] not in ['Active', 'In Progress', 'Paused']:
        return {"success": False, "error": f"Task status invalid: {task_row['Status']}"}

    return {"success": True}
```

---

## Usage in Daily Reports

### Integration with PMT-032 (Daily Report Collection)

**Step 1:** Load TASK_MANAGERS CSV data
```python
tasks = load_csv('Task_Templates_Master_List.csv')
milestones = load_csv('Milestone_Templates_Master_List.csv')
projects = load_csv('Project_Templates_Master_List.csv')
```

**Step 2:** For each activity in daily report
```python
for activity in department_activities:
    mapping = map_activity_to_entities(
        activity_desc=activity.description,
        department=activity.department,
        date=activity.date
    )
    activity.entity_mapping = mapping
```

**Step 3:** Include entity mappings in report output
```markdown
#### Activity: {activity.description}
- **Entity:** {mapping.task} → {mapping.milestone} → {mapping.project}
- **Confidence:** {mapping.confidence}%
```

---

## Best Practices

### DO:
- ✅ Use token-efficient format: `TST-###_Name`
- ✅ Validate all entity IDs against master CSVs before output
- ✅ Include confidence scores for transparency
- ✅ Flag low-confidence (<70%) matches for review
- ✅ Use "Operational/Maintenance" for non-project work
- ✅ Check entity Status (Active/In Progress only)
- ✅ Provide department alignment notes for cross-dept projects
- ✅ Document reasoning for manual assignments

### DON'T:
- ❌ Use verbose format: `TST-001: Full Name With Colons`
- ❌ Include non-existent entity IDs
- ❌ Force mappings at low confidence without flagging
- ❌ Map to Completed/Deprecated entities
- ❌ Skip validation steps
- ❌ Use placeholder or fake IDs
- ❌ Include department letters in entity names
- ❌ Assume operational work must map to projects

---

## Quality Checklist

Before outputting entity mapping, verify:

- [ ] Entity format matches: `{ISO-###}_{Name_With_Underscores}`
- [ ] Task ID exists in Task_Templates_Master_List.csv
- [ ] Milestone ID exists in Milestone_Templates_Master_List.csv
- [ ] Project ID exists in Project_Templates_Master_List.csv
- [ ] Task belongs to Milestone (milestone_template_id correct)
- [ ] Milestone belongs to Project (project_template_id correct)
- [ ] All entities Status = Active or In Progress
- [ ] Confidence score ≥70% OR flagged for review
- [ ] Department alignment explained if cross-dept
- [ ] No department letters in entity names
- [ ] Underscores (not spaces) in names

---

## Version History

**v2.1** (2025-11-19)
- Initial version for daily report entity mapping
- Token-efficient format throughout
- 5-step mapping process
- Department-specific patterns
- Error handling and validation
- Pseudo-code implementation

---

**Status:** Active
**Maintained By:** AI & Automation Department
**Review Cycle:** Monthly
**Next Review:** 2025-12-19

---

## Related Documents

- [REPORT_OUTPUT_SCHEMA_v2.1.md](../../DEPARTMENTS/Daily_Reports/REPORT_OUTPUT_SCHEMA_v2.1.md)
- [ENTITY_MAPPING_GUIDE_v2.1.md](../../DEPARTMENTS/Daily_Reports/ENTITY_MAPPING_GUIDE_v2.1.md)
- [IMPLEMENTATION_PLAN_v2.1.md](../../DEPARTMENTS/Daily_Reports/IMPLEMENTATION_PLAN_v2.1.md)
- [PMT-032_Daily_Report_Collection.md](PMT-032_Daily_Report_Collection.md)

---

**End of Prompt**
