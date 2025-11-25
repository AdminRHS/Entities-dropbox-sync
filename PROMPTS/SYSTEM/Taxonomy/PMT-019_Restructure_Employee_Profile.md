# PROMPT: Restructure Employee Profile Schema to TASK_MANAGERS Format

## Objective
Transform Employee Profile Schema data (`ENTITIES/TALENTS/Employees/Employee_Profile_Schema.md`) into TASK_MANAGERS entity structures (Task Templates, Project Templates, Milestone Templates, Step Templates) following the established taxonomy and ID system.

---

## Source Data Structure

### Employee Profile Schema Fields
- **Core Profile**: ID, Name, Contact Info, Position (Profession, Department, Status)
- **Skills**: Array of skills (comma-separated)
- **Tools**: Array of tools (comma-separated)
- **Summary**: Employee bio/description
- **Work History**: Activities from daily.md files
- **Current Projects**: Projects from plans.md files
- **Tasks**: Task breakdowns from task.md files
- **Metrics**: Performance metrics, attendance data, risk assessment
- **Work Patterns**: Arrival/departure patterns, duration patterns

---

## Target TASK_MANAGERS Structures

### 1. Task Template Structure
```json
{
  "entity_type": "TASK_MANAGERS",
  "sub_entity": "Task_Template",
  "template_id": "Task-Template-XXX",
  "task_name": "[Action] [Object]",
  "action": "[Action verb]",
  "object": "[Object noun]",
  "context": "[Additional context]",
  "description": "[Full description]",
  "department": "[Department code]",
  "profession": "[Profession name]",
  "priority": "[Priority level]",
  "estimated_duration": "[Time estimate]",
  "status": "[Status]",
  "dependencies": [],
  "tools_required": [],
  "skills_required": [],
  "objects_used": [],
  "success_criteria": [],
  "responsibilities": {},
  "steps": [],
  "checklist": [],
  "tags": [],
  "owner": {
    "name": "[Employee Name]",
    "id": "[Employee ID]"
  }
}
```

### 2. Project Template Structure
```json
{
  "entity_type": "TASK_MANAGERS",
  "sub_entity": "Project_Template",
  "template_id": "Project-Template-XXX",
  "metadata": {
    "name": "[Project Name]",
    "description": "[Project Description]",
    "primary_department": "[Department]",
    "departments_involved": [],
    "project_type": "[Type]",
    "complexity": "[Level]",
    "estimated_duration": "[Time]"
  },
  "phases": [],
  "milestones": [],
  "task_sequence": [],
  "resource_requirements": {},
  "owner": {
    "name": "[Employee Name]",
    "id": "[Employee ID]"
  }
}
```

### 3. Milestone Template Structure
```json
{
  "milestone_template_id": "Milestone-Template-XXX",
  "name": "[Milestone Name]",
  "category": "[Category]",
  "department": "[Department]",
  "description": "[Description]",
  "estimated_hours": [Number],
  "phase": [Number],
  "task_templates": [],
  "expected_reports": []
}
```

### 4. Step Template Structure
```json
{
  "step_template_id": "Step-Template-XXX",
  "name": "[Step Name]",
  "action": "[Action verb]",
  "tool": "[Tool name or ID]",
  "responsibility": "[Profession]",
  "placement": "[Location]",
  "duration": "[Time]",
  "dependencies": [],
  "inputs": [],
  "outputs": [],
  "success_criteria": "[Criteria]",
  "related_task_template": "[Task Template ID]"
}
```

---

## Transformation Rules

### Rule 1: Task Template Generation from Work History

**Source**: `Employee.WorkHistory[]` (from daily.md files)

**Process**:
1. Extract activities from work history
2. Identify action + object pairs
3. Map to Task Template structure
4. Extract tools and skills used
5. Create steps from activity breakdown

**Example Mapping**:
```
Source: daily.md activity
"10:00 - Reviewed client requirements and created wireframe in Figma"

Extracted:
- Action: "Review", "Create"
- Object: "Client Requirements", "Wireframe"
- Tool: "Figma"
- Skill: "Wireframing", "Client Communication"
- Duration: "2 hours" (estimated from context)

Task Template:
{
  "action": "Create",
  "object": "Wireframe",
  "context": "based on client requirements",
  "tool": "Figma",
  "skills_required": ["Wireframing", "Client Communication"]
}
```

### Rule 2: Project Template Generation from Current Projects

**Source**: `Employee.CurrentProjects[]` (from plans.md files)

**Process**:
1. Extract project name and description
2. Identify project phases from plans.md
3. Map tasks to task templates
4. Create milestones from project phases
5. Extract dependencies and requirements

**Example Mapping**:
```
Source: plans.md
"File System Project rollout - Coordinate Design department file system implementation"

Extracted:
- Project Name: "File System Project Rollout"
- Department: "AI"
- Description: "Coordinate Design department file system implementation"
- Tasks: ["Coordinate", "Implement", "Document"]
- Phases: ["Planning", "Implementation", "Documentation"]

Project Template:
{
  "metadata": {
    "name": "File System Project Rollout",
    "primary_department": "AI",
    "departments_involved": ["AI", "Design"]
  },
  "phases": [
    {"phase_number": 1, "phase_name": "Planning"},
    {"phase_number": 2, "phase_name": "Implementation"},
    {"phase_number": 3, "phase_name": "Documentation"}
  ]
}
```

### Rule 3: Step Template Generation from Task Breakdowns

**Source**: `Employee.Tasks[]` (from task.md files)

**Process**:
1. Extract task steps from task.md
2. Map each step to Step Template structure
3. Extract action, tool, responsibility
4. Map dependencies between steps
5. Extract inputs/outputs

**Example Mapping**:
```
Source: task.md
"Step 1: Review task requirements and dependencies
 Tool: Documentation
 Responsibility: Project manager
 Duration: 15 minutes"

Step Template:
{
  "step_template_id": "Step-Template-XXX",
  "name": "Review task requirements and dependencies",
  "action": "Review",
  "tool": "Documentation",
  "responsibility": "Project manager",
  "duration": "15 minutes"
}
```

### Rule 4: Skills and Tools Mapping

**Source**: `Employee.Skills[]`, `Employee.Tools[]`

**Process**:
1. Map Skills to LIBRARIES taxonomy (SKL-###)
2. Map Tools to LIBRARIES taxonomy (TLS-###)
3. Include in Task Template `skills_required` and `tools_required`
4. Link to profession requirements

**Example Mapping**:
```
Source: Profile*.md
Skills: "Account Management, Agile, Data Processing"
Tools: "Asana, Jira, Miro, Monday, Notion"

Mapped:
{
  "skills_required": [
    "SKL-XXX (Account Management)",
    "SKL-YYY (Agile)",
    "SKL-ZZZ (Data Processing)"
  ],
  "tools_required": [
    "TLS-XXX (Asana)",
    "TLS-YYY (Jira)",
    "TLS-ZZZ (Miro)"
  ]
}
```

### Rule 5: Department and Profession Mapping

**Source**: `Employee.Position.Department`, `Employee.Position.Profession`

**Process**:
1. Map Department to LIBRARIES taxonomy (DPT-###)
2. Map Profession to LIBRARIES taxonomy (PRF-###)
3. Use in all template structures
4. Maintain consistency across templates

**Department Mapping**:
- AI → DPT-001 (AID)
- Design → DPT-005 (DGN)
- Dev → DPT-003 (DVL)
- LG → DPT-004 (LDG)
- Video → DPT-006 (VDO)

**Profession Mapping**:
- Project Manager → PRF-XXX
- Designer → PRF-XXX
- Developer → PRF-XXX
- Lead Generator → PRF-XXX

### Rule 6: Work Patterns to Task Patterns

**Source**: `Employee.WorkPatterns[]` (from attendance_analyzer)

**Process**:
1. Extract arrival/departure patterns
2. Map to task scheduling preferences
3. Create task templates with time-based constraints
4. Link to shift patterns

**Example Mapping**:
```
Source: Work Patterns
Arrival Pattern: "Early Bird" (7:00-9:00)
Duration Pattern: "Standard" (8 hours)

Task Template:
{
  "preferred_time": "Morning (7:00-9:00 start)",
  "estimated_duration": "8 hours",
  "work_pattern": "Standard Day"
}
```

### Rule 7: Metrics to Task Performance

**Source**: `Employee.Metrics[]`

**Process**:
1. Extract performance metrics
2. Map to task success criteria
3. Create performance-based task templates
4. Link to risk assessment

**Example Mapping**:
```
Source: Metrics
Activity Frequency: "High"
Completion Rate: 98%
Risk Category: "Normal"

Task Template:
{
  "performance_metrics": {
    "expected_completion_rate": "98%",
    "activity_level": "High",
    "risk_level": "Normal"
  }
}
```

---

## ID Generation Rules

### Task Template IDs
**Format**: `Task-Template-XXX` or `TEMPLATE-TASK-{DEPT}-XXX`

**Rules**:
- Sequential numbering within department
- Department prefix optional but recommended
- Example: `TEMPLATE-TASK-AI-001`, `Task-Template-001`

### Project Template IDs
**Format**: `Project-Template-XXX`

**Rules**:
- Sequential numbering
- Can include department prefix
- Example: `Project-Template-002`, `Project-Template-AI-001`

### Milestone Template IDs
**Format**: `Milestone-Template-XXX` or `MIL-PROJ-{PROJ}-XXX`

**Rules**:
- Sequential numbering
- Can link to project
- Example: `Milestone-Template-001`, `MIL-PROJ-DEV-001-001`

### Step Template IDs
**Format**: `Step-Template-XXX` or `STEP-TASK-{TASK}-XXX`

**Rules**:
- Sequential numbering
- Can link to task template
- Example: `Step-Template-001`, `STEP-TASK-AI-001-01`

---

## Transformation Workflow

### Phase 1: Data Extraction
1. Load Employee Profile Schema data
2. Extract core profile fields
3. Extract work history from daily.md files
4. Extract projects from plans.md files
5. Extract tasks from task.md files
6. Extract metrics and patterns

### Phase 2: Task Template Creation
1. For each work history activity:
   - Identify action + object pair
   - Extract tools and skills
   - Create Task Template
   - Generate Task Template ID
   - Link to employee owner

### Phase 3: Project Template Creation
1. For each current project:
   - Extract project metadata
   - Identify phases and milestones
   - Map tasks to task templates
   - Create Project Template
   - Generate Project Template ID

### Phase 4: Step Template Creation
1. For each task breakdown:
   - Extract individual steps
   - Map to Step Template structure
   - Link to parent Task Template
   - Generate Step Template ID

### Phase 5: Milestone Template Creation
1. For each project phase:
   - Extract milestone information
   - Link task templates
   - Create Milestone Template
   - Generate Milestone Template ID

### Phase 6: Taxonomy Integration
1. Map Skills to SKL-### codes
2. Map Tools to TLS-### codes
3. Map Departments to DPT-### codes
4. Map Professions to PRF-### codes
5. Map Actions to ACT-### codes
6. Map Objects to OBJ-### codes

### Phase 7: Cross-Referencing
1. Link Task Templates to Projects
2. Link Steps to Tasks
3. Link Milestones to Projects
4. Link Templates to Employees
5. Create relationship map

---

## Field Mapping Tables

### Employee Profile → Task Template

| Employee Profile Field | Task Template Field | Transformation |
|------------------------|---------------------|----------------|
| `WorkHistory[].activities` | `task_name` | Extract action + object |
| `WorkHistory[].tools_used` | `tools_required[]` | Map to TLS-### |
| `WorkHistory[].skills` | `skills_required[]` | Map to SKL-### |
| `Position.Profession` | `profession` | Map to PRF-### |
| `Position.Department` | `department` | Map to DPT-### |
| `Metrics.CompletionRate` | `performance_metrics.completion_rate` | Direct mapping |
| `WorkPatterns.ArrivalPattern` | `preferred_time` | Time-based mapping |
| `ID` | `owner.id` | Direct mapping |
| `Name` | `owner.name` | Direct mapping |

### Employee Profile → Project Template

| Employee Profile Field | Project Template Field | Transformation |
|------------------------|----------------------|----------------|
| `CurrentProjects[].name` | `metadata.name` | Direct mapping |
| `CurrentProjects[].description` | `metadata.description` | Direct mapping |
| `CurrentProjects[].phases` | `phases[]` | Extract phases |
| `CurrentProjects[].tasks` | `task_sequence[]` | Map to Task Templates |
| `Position.Department` | `metadata.primary_department` | Map to DPT-### |
| `WorkHistory[].projects` | `related_templates` | Link projects |

### Employee Profile → Step Template

| Employee Profile Field | Step Template Field | Transformation |
|------------------------|---------------------|----------------|
| `Tasks[].steps[].name` | `name` | Direct mapping |
| `Tasks[].steps[].action` | `action` | Extract action verb |
| `Tasks[].steps[].tool` | `tool` | Map to TLS-### |
| `Tasks[].steps[].responsibility` | `responsibility` | Map to PRF-### |
| `Tasks[].steps[].duration` | `duration` | Direct mapping |
| `Tasks[].steps[].dependencies` | `dependencies[]` | Link step IDs |

---

## Output Structure

### Directory Organization
```
ENTITIES/TASK_MANAGERS/
├── Task_Templates/
│   ├── By_Employee/
│   │   ├── EMP-37226/
│   │   │   ├── Task-Template-001_[Task_Name].json
│   │   │   └── Task-Template-002_[Task_Name].json
│   └── By_Department/
│       ├── AI/
│       ├── Design/
│       └── Dev/
├── Project_Templates/
│   ├── By_Employee/
│   │   └── EMP-37226/
│   └── By_Department/
├── Milestone_Templates/
│   └── By_Project/
└── Step_Templates/
    └── By_Task/
```

### File Naming Convention
- **Task Templates**: `Task-Template-{ID}_{Task_Name}.json`
- **Project Templates**: `Project-Template-{ID}_{Project_Name}.json`
- **Milestone Templates**: `Milestone-Template-{ID}_{Milestone_Name}.json`
- **Step Templates**: `Step-Template-{ID}_{Step_Name}.json`

---

## Validation Rules

1. **Required Fields**: All templates must have entity_type, sub_entity, template_id
2. **ID Uniqueness**: All template IDs must be unique across TASK_MANAGERS
3. **Taxonomy Compliance**: All Skills, Tools, Departments, Professions must map to LIBRARIES taxonomy
4. **Owner Reference**: All templates must reference employee owner (name + ID)
5. **Dependency Validity**: All dependencies must reference valid template IDs
6. **Step-Task Linking**: All Step Templates must link to valid Task Template
7. **Task-Project Linking**: All Task Templates in projects must exist
8. **Milestone-Project Linking**: All Milestones must link to valid Project Template

---

## Example Transformations

### Example 1: Work History Activity → Task Template

**Source** (from daily.md):
```
"10:00 - Processed video transcriptions using Google AI Studio, extracted taxonomy elements"
```

**Transformed Task Template**:
```json
{
  "entity_type": "TASK_MANAGERS",
  "sub_entity": "Task_Template",
  "template_id": "TEMPLATE-TASK-AI-001",
  "task_name": "Process Video Transcriptions",
  "action": "process",
  "object": "video transcriptions",
  "context": "with taxonomy extraction",
  "description": "Process video transcriptions to extract taxonomy elements and map them to library structure using Google AI Studio",
  "department": "AI",
  "profession": "Project manager",
  "estimated_duration": "4-6 hours",
  "status": "Active",
  "tools_required": [
    "TLS-XXX (Google AI Studio)",
    "TLS-YYY (Transcribe AI)"
  ],
  "skills_required": [
    "SKL-XXX (Video Processing)",
    "SKL-YYY (Taxonomy Extraction)"
  ],
  "owner": {
    "name": "Artemchuk Nikolay",
    "id": "37226"
  }
}
```

### Example 2: Current Project → Project Template

**Source** (from plans.md):
```
"File System Project rollout - Coordinate Design department file system implementation"
```

**Transformed Project Template**:
```json
{
  "entity_type": "TASK_MANAGERS",
  "sub_entity": "Project_Template",
  "template_id": "Project-Template-AI-001",
  "metadata": {
    "name": "File System Project Rollout",
    "description": "Coordinate Design department file system implementation",
    "primary_department": "AI",
    "departments_involved": ["AI", "Design"],
    "project_type": "Internal",
    "complexity": "High",
    "estimated_duration": "2-3 weeks"
  },
  "phases": [
    {
      "phase_number": 1,
      "phase_name": "Planning",
      "duration": "3-5 days"
    },
    {
      "phase_number": 2,
      "phase_name": "Implementation",
      "duration": "1-2 weeks"
    },
    {
      "phase_number": 3,
      "phase_name": "Documentation",
      "duration": "2-3 days"
    }
  ],
  "owner": {
    "name": "Artemchuk Nikolay",
    "id": "37226"
  }
}
```

### Example 3: Task Breakdown → Step Template

**Source** (from task.md):
```
"Step 1: Review task requirements and dependencies
 Tool: Documentation
 Responsibility: Project manager
 Duration: 15 minutes"
```

**Transformed Step Template**:
```json
{
  "step_template_id": "STEP-TASK-AI-001-01",
  "name": "Review task requirements and dependencies",
  "action": "review",
  "tool": "Documentation",
  "responsibility": "Project manager",
  "placement": "Task documentation",
  "duration": "15 minutes",
  "dependencies": [],
  "success_criteria": "All requirements understood, dependencies identified",
  "related_task_template": "TEMPLATE-TASK-AI-001"
}
```

---

## Integration with Existing TASK_MANAGERS

### Linking Strategy
1. **Employee Templates**: Create `By_Employee/` subdirectories
2. **Cross-Reference**: Link employee templates to existing templates
3. **Deduplication**: Check for existing templates before creating new ones
4. **Versioning**: Maintain version history for template updates

### Relationship Mapping
```
Employee (TALENTS)
  ├─→ Task Templates (TASK_MANAGERS)
  │   ├─→ Step Templates (TASK_MANAGERS)
  │   └─→ Skills/Tools (LIBRARIES)
  ├─→ Project Templates (TASK_MANAGERS)
  │   ├─→ Milestone Templates (TASK_MANAGERS)
  │   └─→ Task Templates (TASK_MANAGERS)
  └─→ Work Patterns → Task Scheduling Preferences
```

---

## Execution Checklist

### Pre-Transformation
- [ ] Load Employee Profile Schema data
- [ ] Verify LIBRARIES taxonomy mappings available
- [ ] Check existing TASK_MANAGERS templates for duplicates
- [ ] Prepare ID generation sequence

### Transformation Steps
- [ ] Extract work history activities
- [ ] Generate Task Templates from activities
- [ ] Extract current projects
- [ ] Generate Project Templates from projects
- [ ] Extract task breakdowns
- [ ] Generate Step Templates from tasks
- [ ] Extract project phases
- [ ] Generate Milestone Templates from phases
- [ ] Map Skills/Tools to LIBRARIES taxonomy
- [ ] Link all templates with cross-references

### Post-Transformation
- [ ] Validate all template structures
- [ ] Verify ID uniqueness
- [ ] Check taxonomy mappings
- [ ] Validate dependencies
- [ ] Generate relationship map
- [ ] Create index files
- [ ] Update TASK_MANAGERS listings

---

## Output Deliverables

1. **Task Templates**: JSON files in `Task_Templates/By_Employee/{Employee_ID}/`
2. **Project Templates**: JSON files in `Project_Templates/By_Employee/{Employee_ID}/`
3. **Milestone Templates**: JSON files in `Milestone_Templates/`
4. **Step Templates**: JSON files in `Step_Templates/By_Task/`
5. **Index File**: `Employee_Templates_Index.json` with all mappings
6. **Relationship Map**: `Employee_Templates_Relationships.md` with cross-references

---

## Notes

- **Preservation**: Original Employee Profile data remains unchanged
- **Bidirectional**: Templates can reference back to employee profiles
- **Incremental**: Can process employees one at a time
- **Extensible**: New employee data automatically generates new templates
- **Taxonomy Aligned**: All mappings follow LIBRARIES taxonomy structure
- **Validation**: All templates must pass validation before saving

---

**Created**: 2025-01-18
**Last Updated**: 2025-01-18
**Version**: 1.0
**Related Documents**: 
- `Employee_Profile_Schema.md`
- `PROMPT_Build_LIBRARIES_Taxonomy.md`
- `Task_Templates.md`

