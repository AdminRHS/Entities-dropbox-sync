# Entity Mapping Guide v2.1

**Version:** 2.1 | **Date:** 2025-11-19 | **Status:** Active

---

## Overview

Map daily activities to TASK_MANAGERS entity hierarchy for project/milestone tracking in department reports.

**v2.1 Updates:**
- ✅ Token-efficient format: `{ISO-###}_{Name}`
- ✅ Corrected STT (was STP)
- ✅ Updated CSV paths
- ✅ Removed MKT

---

## Entity Types

### PRT - Project Template
**Format:** `PRT-###_{Name}`
**Examples:** PRT-001_AI_Tutorial_Research, PRT-007_System_Analysis

### MLT - Milestone Template
**Format:** `MLT-###_{Name}`
**Examples:** MLT-001_Content_Analysis, MLT-002_Data_Inventory

### TST - Task Template
**Format:** `TST-###_{Name}`
**Examples:** TST-055_Process_Department_Task_Files, TST-058_Extract_Tasks_Daily_Files

### STT - Step Template
**Format:** `STT-###_{Name}`
**Examples:** STT-155_Conduct_Client_Brand_Discovery, STT-201_Review_Code_Pull_Request

---

## Mapping Process (5 Steps)

### Step 1: Analyze Activity

**Extract:**
- Action verb (Process, Extract, Create, Validate)
- Object/target (Task Files, Taxonomy, CV Data)
- Context (AI department, folders 04-11)

**Example:**
```
Activity: "Process AI department task files from folders 04-11"
→ Action: Process
→ Object: Task Files
→ Context: AI department, folders 04-11
```

---

### Step 2: Match to Task (TST-###)

**Algorithm:**
1. Keyword search in Tasks_Master.csv
2. Match action + object
3. Filter by department
4. Score confidence (High >90%, Medium 70-89%, Low <70%)

**Example:**
```
Activity: "Process AI department task files from folders 04-11"
↓ Keywords: ["process", "task files", "AI department"]
↓ Search Tasks_Master.csv
→ Match: TST-055_Process_Department_Task_Files (95% confidence)
```

---

### Step 3: Roll Up to Milestone (MLT-###)

**Lookup:**
1. Find TST-### row in Tasks_Master.csv
2. Read milestone_template_id column
3. Lookup MLT-### in Milestones_Master.csv

**Example:**
```
TST-055_Process_Department_Task_Files
↓ Tasks_Master.csv: milestone_template_id = MLT-002
→ MLT-002_Data_Inventory
```

---

### Step 4: Roll Up to Project (PRT-###)

**Lookup:**
1. Find MLT-### row in Milestones_Master.csv
2. Read project_template_id column
3. Lookup PRT-### in Projects_Master.csv

**Example:**
```
MLT-002_Data_Inventory
↓ Milestones_Master.csv: project_template_id = PRT-007
→ PRT-007_System_Analysis
```

---

### Step 5: Validate Chain

**Checklist:**
- ✅ TST-### exists
- ✅ MLT-### exists
- ✅ PRT-### exists
- ✅ TST belongs to MLT
- ✅ MLT belongs to PRT
- ✅ Status = Active/In Progress
- ✅ Department alignment correct

---

## Complete Example

### Activity: "Process AI department task files from folders 04-11"

**Step 1:** Analyze
- Action: Process
- Object: Task Files
- Context: AI dept, folders 04-11

**Step 2:** Match Task
- Search: "process task files"
- Match: TST-055_Process_Department_Task_Files
- Confidence: 95%

**Step 3:** Find Milestone
- TST-055 → MLT-002_Data_Inventory

**Step 4:** Find Project
- MLT-002 → PRT-007_System_Analysis

**Step 5:** Validate
- ✅ All entities exist
- ✅ Chain valid
- ✅ Department: AID
- ✅ Status: Active

**Result:**
```markdown
#### Activity 1: Process AI department task files
- **Entity:** TST-055_Process_Department_Task_Files → MLT-002_Data_Inventory → PRT-007_System_Analysis
```

---

## Department-Specific Mapping

### AI Department (AID)
**Common Projects:** PRT-001_AI_Tutorial_Research, PRT-006_Research_Taxonomy_Pipeline, PRT-007_System_Analysis

**Common Tasks:** TST-015_Extract_Taxonomy, TST-055_Process_Task_Files, TST-058_Extract_Daily_Files

**Activity Patterns:**
- Infrastructure configs → Operational/Maintenance
- Tool integrations → TST-specific or Operational
- Prompt engineering → PRT-001 or PRT-006
- Framework development → Operational/Technical Debt

---

### HR Department (HRM)
**Common Projects:** PRT-003_HR_Automation

**Common Tasks:** TST-039_Setup_n8n_CV_Screening, TST-048_Create_Scoring_Algorithm, TST-053_CV_Parser_Development

**Activity Patterns:**
- Candidate sourcing → Operational/Recruitment
- Interview scheduling → Operational/Recruitment
- System setup → PRT-003 tasks
- Employee onboarding → Operational/HR Operations

---

### Design Department (DGN)
**Common Projects:** PRT-008_VIDEO_Production, Client projects (DGN-CLIENT-###)

**Common Tasks:** TST-012_Create_Logo_Concepts, TST-010_UI_UX_Design, TST-009_Design_System_Development

**Activity Patterns:**
- Client design work → Client project PRT-###
- Internal design systems → TST-009 or Operational
- Video thumbnails → PRT-008 support
- Brand assets → Depends on initiative

---

### Development Department (DEV)
**Common Projects:** PRT-002_MCP_Automation_Stack, PRT-003_HR_Automation (Support)

**Common Tasks:** TST-001_AI_Powered_HTML_Parsing, TST-042_Configure_ATS_Integration, TST-045_Build_CV_Parser_Workflow

**Activity Patterns:**
- Feature development → PRT-specific tasks
- Bug fixes → Operational/Maintenance
- Integration work → Cross-project TST
- Testing/QA → Related to parent TST

---

### Finance Department (FNC)
**Common Activities:** Mostly Operational/Maintenance

**Patterns:**
- Month-end closing → Operational/Routine
- Invoice processing → Operational/Routine
- Bank reconciliation → Operational/Routine
- System improvements → May map to automation PRT

**Note:** Finance has fewer project-mapped activities; focus on operational excellence.

---

## Special Cases

### Case 1: Operational/Maintenance
**When:** Routine department operations, not project-related

**Example:**
```markdown
#### Activity: Process daily email communications
- **Entity:** Operational/Maintenance (No project mapping)
- **Category:** Administrative Operations
```

---

### Case 2: Multi-Department Projects
**Example (PRT-003_HR_Automation):**
- HRM Report: Role = Lead
- DEV Report: Role = Support
- AID Report: Role = Support
- All map to same PRT-003

---

### Case 3: Low Confidence Match (<70%)
**Options:**

**A. Manual Assignment:**
```markdown
- **Entity:** TST-###_{Name} (Manual Assignment)
- **Confidence:** Low - Review Recommended
```

**B. Flag for Review:**
```markdown
- **Entity:** Pending Manual Review
- **Reason:** No high-confidence match
- **Best Guess:** TST-### (60%)
```

**C. Operational:**
```markdown
- **Entity:** Operational/Maintenance
- **Reason:** No applicable project/task
```

---

### Case 4: Cross-Project Activities
**When activity contributes to multiple projects:**

```markdown
#### Activity: Design tutorial thumbnails
- **Primary:** TST-007_Create_Video_Thumbnails → PRT-008_VIDEO_Production
- **Supporting:** PRT-001_AI_Tutorial_Research (thumbnails for AI tutorials)
```

---

## Data Sources

### Master CSV Files

**Locations:**
```
ENTITIES/TASK_MANAGERS/Project_Templates/Project_Templates_Master_List.csv
ENTITIES/TASK_MANAGERS/Milestone_Templates/Milestone_Templates_Master_List.csv
ENTITIES/TASK_MANAGERS/Task_Templates/Task_Templates_Master_List.csv
ENTITIES/TASK_MANAGERS/Step_Templates/Taxonomy/Step_Templates_Master_List.csv
```

**Columns:**
```csv
New_ID, Entity_Type, Current_ID, Name, Description, Department, File_Path, Status
```

**Example (Tasks):**
```csv
TST-001,Task_Template,Task-Template-001,AI Powered HTML Parsing,Parse HTML data using AI...,AID,...,Active
```

**Our Usage:**
- New_ID → TST-001
- Name → AI_Powered_HTML_Parsing
- Department → AID
- Status → Active

**Format:** `TST-001_AI_Powered_HTML_Parsing`

---

## Validation Rules

### Entity ID Format
- Must match: `{ISO-###}_{Name_With_Underscores}`
- ISO codes: PRT, MLT, TST, STT only
- No leading zeros
- Underscores in names (not spaces)

### Entity Status
- Must be: Active, In Progress, or Paused
- Blocked → note in Challenges
- Completed → don't include in active work

### Department Alignment
- Task department should match or support report department
- Cross-department tasks require coordination note
- Misaligned departments need explanation

### Hierarchy Integrity
- TST must belong to MLT (via milestone_template_id)
- MLT must belong to PRT (via project_template_id)
- No orphaned entities

---

## Pseudo-Code

```python
def map_activity_to_entities(activity_desc, department):
    # Step 1: Extract keywords
    keywords = extract_keywords(activity_desc)

    # Step 2: Search Tasks CSV
    tasks_df = load_csv('Task_Templates_Master_List.csv')
    matches = search_tasks(tasks_df, keywords, department)
    best = get_highest_confidence(matches)

    if best.confidence < 0.7:
        return {"status": "low_confidence", "task": best.id}

    # Step 3: Find milestone
    task_row = tasks_df[tasks_df['New_ID'] == best.id]
    milestone_id = task_row['milestone_template_id'].values[0]

    # Step 4: Find project
    milestones_df = load_csv('Milestone_Templates_Master_List.csv')
    milestone_row = milestones_df[milestones_df['New_ID'] == milestone_id]
    project_id = milestone_row['project_template_id'].values[0]

    # Step 5: Validate
    if validate_chain(best.id, milestone_id, project_id):
        # Format as: TST-###_Name
        task_name = task_row['Name'].replace(' ', '_')
        milestone_name = milestone_row['Name'].replace(' ', '_')
        project_name = project_row['Name'].replace(' ', '_')

        return {
            "task": f"{best.id}_{task_name}",
            "milestone": f"{milestone_id}_{milestone_name}",
            "project": f"{project_id}_{project_name}",
            "confidence": best.confidence
        }
    else:
        return {"status": "validation_failed"}
```

---

## Best Practices

### DO:
- ✅ Use token-efficient format: `TST-###_{Name}`
- ✅ Validate all IDs against master CSVs
- ✅ Include confidence scores
- ✅ Flag low-confidence (<70%) for review
- ✅ Use "Operational/Maintenance" for non-project work
- ✅ Check entity status (Active/In Progress)

### DON'T:
- ❌ Use verbose format: `TST-001: Full Name With Spaces`
- ❌ Include non-existent entity IDs
- ❌ Force mappings at low confidence
- ❌ Map to Completed/Deprecated entities
- ❌ Skip validation
- ❌ Use placeholder/fake IDs

---

## Troubleshooting

### No Task Match
**Solutions:**
1. Broaden keywords (synonyms)
2. Check if operational (not project)
3. Review recent dept tasks
4. Flag for manual assignment
5. Use Operational/Maintenance

### Invalid Chain
**Solutions:**
1. Verify each ID in CSV
2. Check milestone_template_id / project_template_id fields
3. Confirm status = Active
4. Report data integrity issue

### Department Mismatch
**Solutions:**
1. Check if cross-dept project (note in Section 5)
2. Verify dept code in CSV
3. Confirm Support/Contributor role
4. Flag if true mismatch

### Multiple Matches
**Solutions:**
1. Use department filtering
2. Check context for disambiguation
3. Review recent project history
4. Select most recent/active
5. Flag for review if uncertain

---

## Version History

**v2.1** (2025-11-19)
- Token-efficient format
- Corrected STT
- Updated CSV paths
- Removed MKT

**v1.0** (2025-11-19)
- Initial guide

---

**Status:** Active
**Maintained By:** AI & Automation
**Review:** Monthly