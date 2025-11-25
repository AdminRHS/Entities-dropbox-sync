# Entity Mapping Guide - Daily Reports v2.0

**Document Type:** Technical Guide
**Version:** 1.0
**Date:** 2025-11-19
**Purpose:** Instructions for mapping daily activities to TASK_MANAGERS entity hierarchy

---

## Overview

This guide explains how to map daily report activities to the TASK_MANAGERS entity hierarchy (PRT → MLT → TST → STP), enabling project/milestone tracking in department daily reports v2.0.

**Entity Hierarchy:**
```
PROJECT TEMPLATE (PRT-###)
  └── MILESTONE TEMPLATE (MLT-###)
      └── TASK TEMPLATE (TST-###)
          └── STEP TEMPLATE (STP-###)
```

---

## Entity Types

### PRT - Project Template
**Format:** PRT-### (e.g., PRT-001, PRT-007)
**Description:** High-level initiatives or programs spanning multiple milestones
**Examples:**
- PRT-001: AI Tutorial Research to Taxonomy Integration
- PRT-003: HR Automation Implementation
- PRT-007: System Analysis

### MLT - Milestone Template
**Format:** MLT-### (e.g., MLT-001, MLT-010)
**Description:** Major phases or deliverables within a project
**Examples:**
- MLT-001: Content Analysis (Phase 1 of PRT-001)
- MLT-002: Data Inventory (Phase 2 of PRT-007)
- MLT-010: CV Screening Setup (Phase 1 of PRT-003)

### TST - Task Template
**Format:** TST-### or Task-Template-### (e.g., TST-015, TST-055)
**Description:** Specific work units that contribute to milestones
**Structure:** ACTION + OBJECT + CONTEXT
**Examples:**
- TST-015: Extract Taxonomy from Tutorial Videos
- TST-055: Process Department Task Files
- TST-058: Extract Tasks from Daily Files

### STP - Step Template
**Format:** STP-### or Step-Template-### (e.g., STP-155, STP-201)
**Description:** Atomic procedural actions that compose tasks
**Structure:** ACTION + OBJECT + TOOL + RESPONSIBILITY
**Examples:**
- STP-155: Conduct Client Brand Discovery Session
- STP-201: Review Code Pull Request

---

## Mapping Process

### Step 1: Analyze Activity Description

**Extract Key Components:**
1. **Action Verb:** What was done? (e.g., Process, Extract, Create, Validate)
2. **Object/Target:** What was worked on? (e.g., Task Files, Taxonomy, CV Data)
3. **Context:** Additional details (e.g., from folders 04-11, using n8n, for AI department)

**Example Activity:**
> "Process AI department task files from folders 04-11"

**Extracted Components:**
- Action: Process
- Object: Task Files
- Context: AI department, folders 04-11

---

### Step 2: Match to Task Template (TST-###)

**Matching Algorithm:**

1. **Keyword Matching:**
   - Search Tasks_Master.csv for keywords from action + object
   - Look in columns: task_template_name, action, object, context

2. **Confidence Scoring:**
   - High (90-100%): Exact match on action + object
   - Medium (70-89%): Partial match, context differs
   - Low (<70%): Fuzzy match, manual review needed

3. **Department Filtering:**
   - Prioritize tasks from same department
   - Check task department field matches report department

**Example Mapping:**
```
Activity: "Process AI department task files from folders 04-11"
↓
Keywords: ["process", "task files", "AI department"]
↓
Search Tasks_Master.csv:
- TST-055: "Process Department Task Files"
  - action: "Process"
  - object: "Task Files"
  - department: "AID"
  - confidence: 95% ✅ HIGH MATCH
↓
Result: TST-055
```

**Fallback Strategy:**
If no match found (< 70% confidence):
- Check for similar tasks in same department
- Review recent tasks from department's project history
- Mark as "Operational/Maintenance" if truly not project-related
- Flag for manual entity assignment

---

### Step 3: Roll Up to Milestone (MLT-###)

**Lookup Process:**

1. **Find Parent Milestone:**
   - In Tasks_Master.csv, locate TST-### row
   - Read milestone_template_id or steps_template column
   - Extract MLT-### reference

2. **Verify Milestone Details:**
   - In Milestones_Master.csv, locate MLT-### row
   - Confirm milestone is Active or In Progress
   - Verify department alignment

**Example Rollup:**
```
TST-055: Process Department Task Files
↓
Read Tasks_Master.csv row for TST-055:
- milestone_template_id: MLT-002
↓
Lookup MLT-002 in Milestones_Master.csv:
- name: "Data Inventory"
- project_template_id: PRT-007
- status: "Active"
- department: "AID"
↓
Result: MLT-002 (Data Inventory)
```

---

### Step 4: Roll Up to Project (PRT-###)

**Lookup Process:**

1. **Find Parent Project:**
   - In Milestones_Master.csv, locate MLT-### row
   - Read project_template_id column
   - Extract PRT-### reference

2. **Verify Project Details:**
   - In Projects_Master.csv, locate PRT-### row
   - Confirm project is Active
   - Verify department involvement

**Example Rollup:**
```
MLT-002: Data Inventory
↓
Read Milestones_Master.csv row for MLT-002:
- project_template_id: PRT-007
↓
Lookup PRT-007 in Projects_Master.csv:
- name: "System Analysis"
- status: "Active"
- department: "AID"
↓
Result: PRT-007 (System Analysis)
```

---

### Step 5: Validate Entity Chain

**Validation Checklist:**
- [ ] TST-### exists in Tasks_Master.csv
- [ ] MLT-### exists in Milestones_Master.csv
- [ ] PRT-### exists in Projects_Master.csv
- [ ] TST belongs to MLT (check milestone_template_id)
- [ ] MLT belongs to PRT (check project_template_id)
- [ ] All entities have status "Active" or "In Progress"
- [ ] Department alignment correct

**Invalid Chain Handling:**
If validation fails:
1. Note error in report
2. Flag for manual review
3. Provide partial mapping if possible (e.g., TST-### without MLT/PRT)
4. Include confidence score

---

## Complete Mapping Example

### Example 1: AI Department Task Processing

**Activity Description:**
> "Process AI department task files from folders 04-11. Extracted 47 unique tasks, categorized by priority and status."

**Step 1: Analyze**
- Action: Process, Extract, Categorize
- Object: Task Files
- Context: AI department, folders 04-11, 47 tasks

**Step 2: Match Task**
- Search: "process task files"
- Best Match: TST-055: Process Department Task Files
- Confidence: 95%

**Step 3: Find Milestone**
- TST-055 → milestone_template_id: MLT-002
- MLT-002: Data Inventory

**Step 4: Find Project**
- MLT-002 → project_template_id: PRT-007
- PRT-007: System Analysis

**Step 5: Validate**
- ✅ TST-055 exists in Tasks_Master.csv
- ✅ MLT-002 exists in Milestones_Master.csv
- ✅ PRT-007 exists in Projects_Master.csv
- ✅ TST-055 belongs to MLT-002
- ✅ MLT-002 belongs to PRT-007
- ✅ All entities Active
- ✅ Department: AID

**Final Mapping:**
```markdown
#### Activity 1: Process AI department task files from folders 04-11
- **Status:** ✅ Completed
- **Entity Mapping:**
  - Task Template: TST-055: Process Department Task Files
  - Milestone: MLT-002: Data Inventory
  - Project: PRT-007: System Analysis
```

---

### Example 2: HR CV Scoring Algorithm

**Activity Description:**
> "Designed CV scoring algorithm for automated candidate evaluation. Collaborated with DEV team on integration specs."

**Step 1: Analyze**
- Action: Design, Develop
- Object: CV Scoring Algorithm
- Context: Automated evaluation, DEV collaboration

**Step 2: Match Task**
- Search: "scoring algorithm" OR "CV automation"
- Best Match: TST-048: Create Scoring Algorithm
- Confidence: 92%

**Step 3: Find Milestone**
- TST-048 → milestone_template_id: MLT-010
- MLT-010: CV Screening Setup

**Step 4: Find Project**
- MLT-010 → project_template_id: PRT-003
- PRT-003: HR Automation Implementation

**Step 5: Validate**
- ✅ All entities exist and active
- ✅ Chain valid: TST-048 → MLT-010 → PRT-003
- ✅ Department: HRM (with AID support)

**Final Mapping:**
```markdown
#### Activity 2: Design CV scoring algorithm
- **Status:** ✅ Completed
- **Entity Mapping:**
  - Task Template: TST-048: Create Scoring Algorithm
  - Milestone: MLT-010: CV Screening Setup
  - Project: PRT-003: HR Automation Implementation
```

---

### Example 3: Design Client Project

**Activity Description:**
> "Created logo concepts for client XYZ. Developed 5 variations using Figma and Midjourney."

**Step 1: Analyze**
- Action: Create, Design
- Object: Logo Concepts
- Context: Client XYZ, 5 variations, Figma, Midjourney

**Step 2: Match Task**
- Search: "logo" OR "create concepts"
- Best Match: TST-012: Create Logo Concepts
- Confidence: 88%

**Step 3: Find Milestone**
- TST-012 → milestone_template_id: MLT-009
- MLT-009: Behance Project Publishing

**Step 4: Find Project**
- MLT-009 → project_template_id: DGN-CLIENT-XYZ
- Note: Client projects may have custom PRT-### IDs

**Step 5: Validate**
- ✅ TST-012 exists
- ✅ MLT-009 exists
- ⚠️ PRT custom ID (not in standard range)
- ✅ Chain valid
- ✅ Department: DGN

**Final Mapping:**
```markdown
#### Activity 1: Create logo concepts for client XYZ
- **Status:** 🔄 In Progress
- **Entity Mapping:**
  - Task Template: TST-012: Create Logo Concepts
  - Milestone: MLT-009: Behance Project Publishing
  - Project: DGN-CLIENT-XYZ: Client Branding Project
```

---

## Department-Specific Mapping Examples

### AI Department (AID)

**Common Projects:**
- PRT-001: AI Tutorial Research
- PRT-006: Research to Taxonomy Pipeline
- PRT-007: System Analysis

**Common Tasks:**
- TST-015: Extract Taxonomy
- TST-055: Process Task Files
- TST-058: Extract from Daily Files

**Typical Activities:**
- Infrastructure configurations → Operational/Maintenance
- AI tool integrations → TST-specific or Operational
- Prompt engineering → PRT-001 or PRT-006
- Framework development → Operational/Technical Debt

---

### HR Department (HRM)

**Common Projects:**
- PRT-003: HR Automation Implementation

**Common Tasks:**
- TST-039: Setup n8n for CV Screening
- TST-048: Create Scoring Algorithm
- TST-053: CV Parser Development

**Typical Activities:**
- Candidate sourcing → Operational/Recruitment
- Interview scheduling → Operational/Recruitment
- System setup → PRT-003 tasks
- Employee onboarding → Operational/HR Operations

---

### Design Department (DGN)

**Common Projects:**
- PRT-008: VIDEO Production Workflow
- Client projects (DGN-CLIENT-###)

**Common Tasks:**
- TST-012: Create Logo Concepts
- TST-010: UI/UX Design
- TST-009: Design System Development

**Typical Activities:**
- Client design work → Client project PRT-###
- Internal design systems → TST-009 or Operational
- Video thumbnails → PRT-008 support
- Brand assets → Depends on initiative

---

### Development Department (DEV)

**Common Projects:**
- PRT-002: MCP Automation Stack
- PRT-003: HR Automation (Support role)

**Common Tasks:**
- TST-001: Parse HTML Data
- TST-042: Configure ATS Integration
- TST-045: Build CV Parser Workflow

**Typical Activities:**
- Feature development → PRT-specific tasks
- Bug fixes → Operational/Maintenance
- Integration work → Cross-project TST
- Testing/QA → Related to parent TST

---

### Finance Department (FNC)

**Common Projects:**
- Most work is Operational/Maintenance
- Occasional automation projects

**Common Activities:**
- Month-end closing → Operational/Routine
- Invoice processing → Operational/Routine
- Bank reconciliation → Operational/Routine
- System improvements → May map to automation PRT

**Note:** Finance has fewer project-mapped activities; focus on operational excellence

---

## Special Cases

### Case 1: Operational/Maintenance Activities

**When to Use:**
- Routine departmental operations
- Activities not tied to specific projects
- Business-as-usual work
- Administrative tasks

**Example:**
```markdown
#### Activity: Process daily email communications
- **Status:** ✅ Completed
- **Entity Mapping:** Operational/Maintenance (No project mapping)
- **Category:** Administrative Operations
```

---

### Case 2: Multi-Department Projects

**Approach:**
1. Identify lead department
2. Note supporting departments
3. Map to same PRT-### from all departments
4. Use Cross-Department Coordination section

**Example (PRT-003: HR Automation):**
- **HRM Report:** Shows as "Lead" role
- **DEV Report:** Shows as "Support" role
- **AID Report:** Shows as "Support" role
- All three map activities to PRT-003

---

### Case 3: Low Confidence Matches

**When Match Confidence < 70%:**

**Option A: Manual Assignment**
```markdown
#### Activity: [Description]
- **Entity Mapping:**
  - Manual Assignment: TST-###
  - Confidence: Low (Manual Review Recommended)
```

**Option B: Flag for Review**
```markdown
#### Activity: [Description]
- **Entity Mapping:**
  - Status: Pending Manual Review
  - Reason: No high-confidence task template match
  - Best Guess: TST-### (60% confidence)
```

**Option C: Operational Classification**
```markdown
#### Activity: [Description]
- **Entity Mapping:** Operational/Maintenance
- **Reason:** No applicable project or task template
```

---

### Case 4: Cross-Project Activities

**When Activity Contributes to Multiple Projects:**

**Approach:**
- List primary project in Activity section
- Note additional projects in Cross-Department Coordination
- Show contribution to each in Project Contributions section

**Example:**
```markdown
#### Activity: Design tutorial thumbnails
- **Entity Mapping:**
  - Task Template: TST-007: Create Video Thumbnails
  - Primary Project: PRT-008: VIDEO Production
  - Supporting: PRT-001: AI Tutorial Research (thumbnails for AI tutorials)
```

---

## Data Source Reference

### TASK_MANAGERS CSVs

**Location:** `C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS/DATA\`

**Files:**
1. **Projects_Master.csv**
   - Columns: project_template_id, name, department, status, duration, description, milestone_templates
   - Example: PRT-001, "AI Tutorial Research", AID, Active, "4-6 hours per cycle"

2. **Milestones_Master.csv**
   - Columns: milestone_template_id, name, category, department, estimated_hours, phase, dependencies, task_templates, expected_reports
   - Example: MLT-001, "Content Analysis", Analysis, AID, 8, 1, [], [TST-001, TST-002]

3. **Tasks_Master.csv**
   - Columns: task_template_id, task_template_name, action, object, context, department, estimated_duration, steps_template, tools_required, skills_required, checklist
   - Example: Task-Template-001, "Parse HTML Data", Parse, HTML Data, "using n8n", DEV, "60-90 minutes"

---

## Validation Rules

### Entity ID Format
- Must match pattern: XXX-### (e.g., PRT-001, MLT-042, TST-155)
- No leading zeros in numbers < 100
- Department code must match: PRT/MLT/TST/STP only

### Entity Status
- Must be: Active, In Progress, or Paused
- Blocked entities should be noted in Challenges section
- Completed entities should not appear in active work

### Department Alignment
- Task department should match or support report department
- Cross-department tasks acceptable with coordination note
- Misaligned departments require explanation

### Hierarchy Integrity
- TST must belong to MLT (verified via milestone_template_id)
- MLT must belong to PRT (verified via project_template_id)
- No orphaned entities (all must have valid parents)

---

## Tools and Utilities

### Recommended Workflow

**For AI Assistants:**
1. Load TASK_MANAGERS CSVs at start of report generation
2. Parse each activity description
3. Run keyword matching algorithm
4. Validate entity chain
5. Include confidence scores
6. Flag low-confidence matches

**For Manual Review:**
1. Check flagged activities
2. Verify entity IDs in master CSVs
3. Confirm department alignment
4. Update report with corrections

### Python Pseudo-Code

```python
def map_activity_to_entities(activity_description, department):
    # Step 1: Extract keywords
    keywords = extract_keywords(activity_description)

    # Step 2: Search Tasks_Master.csv
    tasks_df = load_csv('Tasks_Master.csv')
    matches = search_tasks(tasks_df, keywords, department)
    best_match = get_highest_confidence(matches)

    if best_match.confidence < 0.7:
        return {"status": "low_confidence", "task": best_match.id}

    # Step 3: Find milestone
    task_row = tasks_df[tasks_df['task_template_id'] == best_match.id]
    milestone_id = task_row['milestone_template_id'].values[0]

    # Step 4: Find project
    milestones_df = load_csv('Milestones_Master.csv')
    milestone_row = milestones_df[milestones_df['milestone_template_id'] == milestone_id]
    project_id = milestone_row['project_template_id'].values[0]

    # Step 5: Validate
    if validate_entity_chain(best_match.id, milestone_id, project_id):
        return {
            "task": best_match.id,
            "milestone": milestone_id,
            "project": project_id,
            "confidence": best_match.confidence
        }
    else:
        return {"status": "validation_failed"}
```

---

## Best Practices

### DO:
- ✅ Validate all entity IDs against master CSVs before including
- ✅ Include confidence scores for mappings
- ✅ Flag low-confidence matches for manual review
- ✅ Use "Operational/Maintenance" for non-project work
- ✅ Cross-reference with recent department activities
- ✅ Check entity status (Active/In Progress only)
- ✅ Note department role (Lead/Support/Contributor)

### DON'T:
- ❌ Include entity IDs that don't exist in master CSVs
- ❌ Force mappings when confidence is low (<70%)
- ❌ Map to Completed or Deprecated entities
- ❌ Ignore department misalignment without explanation
- ❌ Skip validation steps
- ❌ Assume hierarchy without verifying in CSVs
- ❌ Use placeholder or fake entity IDs

---

## Troubleshooting

### Issue 1: No Task Template Match Found

**Symptoms:** Activity description doesn't match any TST-###

**Solutions:**
1. Broaden keyword search (synonyms, related terms)
2. Check if activity is operational (not project-related)
3. Review recent tasks from same department
4. Flag for manual entity assignment
5. Use "Operational/Maintenance" if truly non-project

---

### Issue 2: Invalid Entity Chain

**Symptoms:** TST → MLT → PRT hierarchy breaks at some point

**Solutions:**
1. Verify each entity ID in respective CSV
2. Check milestone_template_id and project_template_id fields
3. Confirm entity status is Active
4. Report data integrity issue to TASK_MANAGERS maintainers

---

### Issue 3: Department Mismatch

**Symptoms:** Task department doesn't match report department

**Solutions:**
1. Check if it's a cross-department project (note in Section 5)
2. Verify department code in Tasks_Master.csv
3. Confirm department is Support/Contributor role
4. Flag if true mismatch (possible data error)

---

### Issue 4: Multiple Possible Matches

**Symptoms:** Several TST-### match with similar confidence

**Solutions:**
1. Use department filtering to narrow
2. Check context details for disambiguation
3. Review recent project history
4. Select most recent or active task
5. Flag for manual review if uncertain

---

## Version History

**v1.0** (2025-11-19)
- Initial guide creation
- Complete mapping process documentation
- Department-specific examples
- Validation rules
- Special cases handling

---

**Document Status:** Active
**Maintained By:** AI & Automation Department
**Review Schedule:** Monthly
**Next Review:** 2025-12-19