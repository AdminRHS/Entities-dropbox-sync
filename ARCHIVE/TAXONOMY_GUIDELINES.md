**Version:** 1.0  
**Last Updated:** November 25, 2025  
**Purpose:** Clear guidelines for using taxonomy fields and connecting entities in TASK_MANAGERS templates

---

## 📋 Overview

This document defines how taxonomy fields from the LIBRARIES entity are used in TASK_MANAGERS templates and how entities connect to each other. These guidelines ensure consistency and proper relationships between entities in the file-based system.

---

## 🗂️ Core Taxonomy Fields

### Primary Taxonomy Fields

These fields form the core identity of tasks, steps, and checklists by connecting to LIBRARIES entity:

| Field Name | Library Source | Required | Description |
|------------|----------------|----------|-------------|
| **action** | `Libs 25/Actions/actions.json` | ✅ Yes | Verb describing what action is performed |
| **object** | `Libs 25/Objects/objects.json` | ✅ Yes | Business entity or object being acted upon |
| **tool** | `Libs 25/Tools/tools.json` | ⚠️ Conditional | Tool/platform used for execution |
| **profession** | `Libs 25/Professions/professions.json` | ⚠️ Conditional | Role/profession that performs the task |
| **department** | Derived from profession or explicit | ⚠️ Conditional | Department context (HR, Sales, LG, etc.) |

### Secondary Taxonomy Fields

These fields provide additional classification and context:

| Field Name | Source | Required | Description |
|------------|--------|----------|-------------|
| **task_template_type** | System-defined categories | ⚠️ Conditional | Type/category of Task Template |
| **frequency** | System-defined | ⚠️ Optional | How often task occurs (One-time, Daily, Weekly, Monthly, As-needed) |
| **status** | System-defined | ✅ Yes | Current status (Template, Active, Deprecated, etc.) |

---

## 🔗 Entity Connections

### TASK_MANAGERS ↔ LIBRARIES

**Connection Pattern:**
TASK_MANAGERS templates reference values from LIBRARIES entity to define their taxonomy.

**How It Works:**
1. Task Templates use **action** and **object** from LIBRARIES to form task identity
2. Step Templates inherit or specify their own **action** and **object**
3. Checklist Items may reference **action**, **object**, or **tool** for context

**Example:**
```json
{
  "template_id": "TASK-TEMPLATE-001",
  "task_name": "Create Job Posting",
  
  "taxonomy": {
    "action": "Create",                    // From LIBRARIES/Actions
    "object": "Job Posting",               // From LIBRARIES/Objects
    "tool": "Notion",                      // From LIBRARIES/Tools
    "profession": "HR Manager",            // From LIBRARIES/Professions
    "department": "HR"                     // Derived or explicit
  }
}
```

### TASK_MANAGERS ↔ TALENTS

**Connection Pattern:**
Task Templates specify which professions can perform them, linking to TALENTS entity.

**How It Works:**
1. Task Templates list **profession** requirements
2. Tasks can be assigned to employees matching those professions
3. Step Templates may specify profession-specific instructions

**Example:**
```json
{
  "template_id": "TASK-TEMPLATE-001",
  "taxonomy": {
    "action": "Create",
    "object": "Job Posting",
    "profession": "HR Manager",           // Links to TALENTS with this profession
    "department": "HR"
  },
  "responsibilities": [
    "Creating Job Posting"                // Action + Object combination (added to responsibilities library)
  ]
}
```

**Note:** Each unique action + object combination from Task Templates should be added to the responsibilities library (`Libs 25/Responsibilities/responsibilities.json`) with the appropriate profession and department.

**Format for Responsibilities Library Entry:**
```json
{
  "Responsibilities": "Creating Job Posting",    // Action (gerund form from Processes field) + Object
  "Objects": "Job Posting",                      // Object name (from objects.json)
  "Professions": "hr manager",                   // Profession (from professions.json, lowercase)
  "Departments": "managers"                      // Department (from departments, lowercase)
}
```

**Process for Adding Responsibilities:**
1. Extract `action` and `object` from Task Template taxonomy
2. Find the action in `actions.json` and use the `Processes` field (gerund form)
3. Combine: `Processes` + `Object` = Responsibility (e.g., "Creating" + "Job Posting" = "Creating Job Posting")
4. Add entry to `Libs 25/Responsibilities/responsibilities.json` with matching profession and department from the template

### TASK_MANAGERS ↔ JOBS

**Connection Pattern:**
Task Templates related to recruitment connect to JOBS entity.

**How It Works:**
1. Job posting creation tasks reference JOBS entity
2. Tasks may create or update job postings
3. Job-related workflows use Task Templates

**Example:**
```json
{
  "template_id": "TASK-TEMPLATE-001",
  "task_name": "Create Job Posting for [Position]",
  "taxonomy": {
    "action": "Create",
    "object": "Job Posting",              // Links to JOBS entity
    "context": "for [Position]"
  },
  "relationships": {
    "related_entities": ["JOBS"]          // Explicit entity connection
  }
}
```

### TASK_MANAGERS ↔ BUSINESSES

**Connection Pattern:**
Client-related tasks connect to BUSINESSES entity.

**How It Works:**
1. Client onboarding tasks reference BUSINESSES
2. Sales tasks link to client records
3. Workflows may trigger business-related tasks

**Example:**
```json
{
  "template_id": "TASK-TEMPLATE-002",
  "task_name": "Send Follow-up Email to Old Clients",
  "taxonomy": {
    "action": "Send",
    "object": "Follow-up Email",
    "context": "to Old Clients"            // Links to BUSINESSES entity
  },
  "relationships": {
    "related_entities": ["BUSINESSES"]   // Explicit entity connection
  }
}
```

---

## 📚 Library Reference Guidelines

### Using Library Values

**In JSON Templates:**
- ✅ **Use Exact Names**: Always use the exact string name from library files
- ✅ **Case-Sensitive**: Match exact capitalization from library
- ✅ **Human-Readable**: Names make templates readable and maintainable

**Example:**
```json
{
  "taxonomy": {
    "action": "create",           // ✅ Exact name from actions.json
    "object": "Job Posting",     // ✅ Exact name from objects.json
    "tool": "Notion",            // ✅ Exact name from tools.json
    "profession": "hr manager"   // ✅ Exact name from professions.json
  }
}
```

### Library File Locations

| Taxonomy Field | Library File Path | Structure |
|----------------|-------------------|-----------|
| **action** | `Nov25/Libs 25/Actions/actions.json` | Array of objects with "Actions", "Processes", "Results", "Departments", "Professions" |
| **object** | `Nov25/Libs 25/Objects/objects.json` | Array of objects with "Objects", "Object Types", "Professions", "Departments" |
| **tool** | `Nov25/Libs 25/Tools/tools.json` | Array of objects with "Tools", "Tasks", "Professions", "Departments" |
| **profession** | `Nov25/Libs 25/Professions/professions.json` | Array of objects with "Professions", "Departments" |

### Finding Library Values

**Process:**
1. **Identify Need**: Determine which taxonomy field is needed (action, object, tool, profession)
2. **Open Library File**: Navigate to the appropriate library JSON file
3. **Search**: Search for the value that matches your use case
4. **Use Exact Name**: Copy the exact name as it appears in the library (case-sensitive)
5. **Verify Context**: Check that the value matches your department/profession context

**Example:**
```json
// In actions.json, find:
{
  "Actions": "create",
  "Processes": "creating",
  "Results": "created",
  "Departments": "managers",
  "Professions": "recruiter"
}

// In your template, use:
{
  "action": "create"  // ✅ Use exact name from library
}
```

---

## 📋 Template Structure Logic

### Task Template Structure

**Naming Pattern:** `ACTION + OBJECT + CONTEXT`

**Components:**
1. **ACTION** - From LIBRARIES/Actions
   - Examples: create, update, send, analyze, review, approve, generate, process, archive, delete

2. **OBJECT** - From LIBRARIES/Objects
   - Examples: Job Posting, Client Proposal, Email Outreach, LinkedIn Message, Financial Report, Video CV

3. **CONTEXT** - Additional details or parameters
   - Examples: "for Frontend Developer", "with pricing revisions", "to warm leads"

**Complete Examples:**
- `Create` + `Job Posting` + `for Frontend Developer`
- `Update` + `Client Proposal` + `with pricing revisions`
- `Send` + `Follow-up Email` + `to Old Clients`
- `Analyze` + `Lead Quality` + `from LinkedIn campaign`

**JSON Structure:**
```json
{
  "template_id": "TASK-TEMPLATE-001",
  "task_name": "Create Job Posting for [Position]",
  
  "taxonomy": {
    "action": "Create",                    // From LIBRARIES/Actions
    "object": "Job Posting",               // From LIBRARIES/Objects
    "context": "for [Position]",           // Additional context
    "tool": "Notion",                      // From LIBRARIES/Tools
    "profession": "HR Manager",           // From LIBRARIES/Professions
    "department": "HR"                     // Derived or explicit
  },
  
  "task_details": {
    "name": "Create Job Posting",
    "description": "Create a new job posting...",
    "frequency": "As-needed"
  },
  
  "responsibilities": [
    "Creating Job Posting"                // Action + Object combination
  ]
}
```

### Step Template Structure

**Naming Pattern:** Inherits from parent task or specifies own action+object

**Components:**
1. **Parent Task Reference** - Links to Task Template
2. **Step-Specific Action** - May differ from parent task action
3. **Step-Specific Object** - May differ from parent task object
4. **Tool** - Tool used for this specific step

**JSON Structure:**
```json
{
  "step_template_id": "TEMPLATE-STEP-TASK-TEMPLATE-001-001",
  "step_template_name": "Select job template",
  
  "metadata": {
    "status": "Active | Draft | Deprecated"
  },
  
  "parent_task": {
    "task_id": "TASK-TEMPLATE-001",
    "task_name": "Create Job Posting"
  },
  
  "step_details": {
    "step_number": 1,
    "order": 1,
    "action": "Select",                    // Step-specific action
    "object": "Job Template",             // Step-specific object
    "detail": "Select appropriate job template from Notion",
    "expected_duration": 5                // Minutes (template estimate)
  },
  
  "execution": {
    "tool_used": "Notion",                // From LIBRARIES/Tools
    "inputs": ["Position requirements"],
    "outputs": ["Selected template"],
    "success_criteria": "Template selected and opened"
  }
}
```

**Note:** Tracking fields like `completed_at`, `is_completed`, `assignee_id`, and actual execution timestamps belong to actual Step instances, not Step Templates.

### Checklist Item Structure

**Naming Pattern:** Quality check or verification item

**Note:** Checklist Items are part of Task Templates, not separate templates. They define quality checks that should be performed when executing tasks based on the template.

**Components:**
1. **Item Name** - What to check
2. **Guide** - How to verify
3. **Required** - Whether item is mandatory
4. **Optional Taxonomy** - May reference action, object, or tool

**JSON Structure (within Task Template):**
```json
{
  "checklist": [
    {
      "item": "Job title clear and accurate",
      "guide": "No generic titles, specific role",
      "required": true
    }
  ]
}
```

**Template vs. Checklist:**
- **Checklist Items** in templates define what should be checked (reusable blueprint)
- **Checklist Instances** in actual tasks track completion status (`is_completed`, `completed_at`, `completed_by`)
- One Task Template's checklist can be used in multiple Task instances, each with their own completion tracking

### Milestone Template Structure

**Note:** Milestone Templates are reusable blueprints. Tracking fields belong to actual Milestone instances, not templates.

**Milestone Template Structure:**
```json
{
  "milestone_template_id": "MIL-TEMPLATE-PROJ-{DEPT}-{PROJ_NUMBER}-{MIL_NUMBER}",
  "milestone_template_name": "string",
  "metadata": {
    "status": "Active | Draft | Deprecated"
  },
  "parent_project": {
    "project_template_id": "TEMPLATE-PROJ-{DEPT}-{NUMBER}",
    "project_template_name": "string"
  },
  "milestone_details": {
    "milestone_number": "integer (1, 2, 3...)",
    "order": "integer (execution sequence)",
    "description": "string (what this milestone achieves)",
    "deliverables": ["string", "string"],
    "success_criteria": ["string", "string"]
  },
  "taxonomy": {
    "action": "string (high-level milestone action)",
    "object": "string (what is being delivered)",
    "context": "string (business context)"
  },
  "structure": {
    "tasks": ["TASK-TEMPLATE-ID", "TASK-TEMPLATE-ID"],
    "dependencies": ["MIL-TEMPLATE-PROJ-{DEPT}-{PROJ_NUMBER}-{MIL_NUMBER}"]
  },
  "source_tracking": {
    "source_file": "string",
    "extraction_date": "YYYY-MM-DD"
  }
}
```

**In Project Templates:**
```json
{
  "structure": {
    "milestones": [
      "MIL-TEMPLATE-PROJ-HR-001-001",
      "MIL-TEMPLATE-PROJ-HR-001-002"
    ]
  }
}
```

**Template vs. Milestone:**
- **Milestone Templates** are reusable blueprints that define milestone structure, deliverables, and success criteria (no tracking data)
- **Milestone Instances** in actual Projects have tracking (`target_date`, `actual_completion_date`, `status`, `is_completed`, `start_date`, `end_date`, `expected_hours`)
- One Milestone Template can be used to create multiple Milestone variations, each with different timelines, teams, or contexts
- Milestone Templates belong to Project Templates and contain Task Templates

---

## 🔗 Template Relationships

### Task Template Relationships

**Hierarchical Structure:**
```
Task Template
  ├── Step Templates (multiple)
  │   └── Checklist Items (multiple per step)
  ├── Related Task Templates (dependencies)
  └── Related Entities (JOBS, BUSINESSES, TALENTS)
```

**JSON Representation:**
```json
{
  "template_id": "TASK-TEMPLATE-001",
  
  "relationships": {
    "step_templates": [
      "TEMPLATE-STEP-TASK-TEMPLATE-001-001",
      "TEMPLATE-STEP-TASK-TEMPLATE-001-002",
      "TEMPLATE-STEP-TASK-TEMPLATE-001-003"
    ],
    "parent_task_template": null,          // If this is a child task
    "child_task_templates": [],            // Tasks that depend on this
    "dependencies": [
      "TASK-TEMPLATE-002"                  // Prerequisite tasks
    ],
    "related_entities": [
      "JOBS",                              // Links to JOBS entity
      "TALENTS"                             // Links to TALENTS entity
    ]
  }
}
```

### Step Template Relationships

**Hierarchical Structure:**
```
Step Template
  ├── Parent Task Template (required)
  ├── Checklist Items (optional)
  ├── Dependencies (other steps)
  └── Next Steps (sequential flow)
```

**JSON Representation:**
```json
{
  "step_id": "TEMPLATE-STEP-TASK-TEMPLATE-001-001",
  
  "parent_task": {
    "task_id": "TASK-TEMPLATE-001",
    "task_name": "Create Job Posting"
  },
  
  "relationships": {
    "checklist_items": [
      {
        "item": "Job title clear and accurate",
        "guide": "No generic titles, specific role",
        "required": true
      }
    ],
    "dependencies": [],                    // Steps that must complete first
    "next_steps": [
      "TEMPLATE-STEP-TASK-TEMPLATE-001-002"
    ],
    "parallel_steps": []                   // Steps that can run simultaneously
  }
}
```

### Milestone Template Relationships

**Hierarchical Structure:**
```
Milestone Template
  ├── Parent Project Template (required)
  ├── Task Templates (multiple)
  ├── Dependencies (other Milestone Templates)
  └── Taxonomy (action, object, context)
```

**JSON Representation:**
```json
{
  "milestone_template_id": "MIL-TEMPLATE-PROJ-HR-001-001",
  "milestone_template_name": "Pre-boarding Setup",
  
  "parent_project": {
    "project_template_id": "TEMPLATE-PROJ-HR-001",
    "project_template_name": "Employee Onboarding Project"
  },
  
  "structure": {
    "tasks": [
      "TASK-TEMPLATE-HR-001",
      "TASK-TEMPLATE-HR-002"
    ],
    "dependencies": []                    // Milestones that must complete first
  },
  
  "taxonomy": {
    "action": "Setup",
    "object": "Onboarding Infrastructure",
    "context": "Pre-employment preparation"
  }
}
```

### Project Template Relationships

**Hierarchical Structure:**
```
Project Template
  ├── Milestone Templates (multiple)
  │   └── Task Templates (multiple per milestone)
  └── Related Entities
```

**JSON Representation:**
```json
{
  "template_id": "TEMPLATE-PROJ-HR-001",
  "project_template_name": "Employee Onboarding Project",
  
  "metadata": {
    "status": "Active | Draft | Deprecated"
  },
  
  "structure": {
    "milestones": [
      "MIL-TEMPLATE-PROJ-HR-001-001",
      "MIL-TEMPLATE-PROJ-HR-001-002"
    ],
    "tasks": [
      "TASK-TEMPLATE-001",
      "TASK-TEMPLATE-002"
    ]
  },
  
  "relationships": {
    "related_entities": [
      "TALENTS",                           // Links to TALENTS entity
      "JOBS"                               // Links to JOBS entity
    ]
  }
}
```

---

## ✅ Taxonomy Validation Rules

### Required Fields by Template Type

**Task Templates:**
- ✅ `action` (name from actions.json)
- ✅ `object` (name from objects.json)
- ✅ `name` (task name)
- ✅ `description` (what the task accomplishes)
- ⚠️ `tool` (required if task uses specific tool)
- ⚠️ `profession` (required if task is profession-specific)
- ⚠️ `department` (can be derived from profession or explicit)

**Step Templates:**
- ✅ `action` (name from actions.json)
- ✅ `object` (name from objects.json)
- ✅ `name` (step name)
- ✅ `parent_task` (reference to Task Template)
- ⚠️ `tool` (required if step uses specific tool)

**Checklist Items:**
- ✅ `item` (Checklist Item name)
- ⚠️ `action` (if item involves an action)
- ⚠️ `object` (if item involves an object)
- ⚠️ `tool` (if item is tool-specific)

### Validation Checklist

When creating a template, verify:

- [ ] All taxonomy field names exist in their respective library files
- [ ] Names match exactly (case-sensitive) with library entries
- [ ] Required fields are populated
- [ ] Optional fields are included only when relevant
- [ ] Relationships are properly referenced
- [ ] No orphaned references (all referenced templates exist)
- [ ] Entity connections are explicit where needed

---

## 📝 Best Practices

### 1. Consistency
- ✅ Always use exact names from library files (case-sensitive)
- ✅ Use consistent naming conventions across all templates
- ✅ Document any deviations or custom values

### 2. Completeness
- ✅ Include all required taxonomy fields
- ✅ Add optional fields when they add value
- ✅ Link related templates and entities

### 3. Entity Connections
- ✅ Explicitly reference related entities (JOBS, BUSINESSES, TALENTS)
- ✅ Use taxonomy fields to connect to LIBRARIES entity
- ✅ Document entity relationships in relationships section

### 4. Maintainability
- ✅ Keep library files as single source of truth
- ✅ Update templates when library values change
- ✅ Document taxonomy decisions in template comments

### 5. Validation
- ✅ Validate taxonomy fields against library files
- ✅ Check for orphaned references
- ✅ Ensure required fields are present

---

## 🔍 Entity Connection Examples

### Example 1: Task Template with Multiple Entity Connections

```json
{
  "template_id": "TASK-TEMPLATE-001",
  "task_name": "Create Job Posting for [Position]",
  
  "taxonomy": {
    "action": "Create",                    // From LIBRARIES/Actions
    "object": "Job Posting",              // From LIBRARIES/Objects
    "tool": "Notion",                     // From LIBRARIES/Tools
    "profession": "HR Manager",           // From LIBRARIES/Professions
    "department": "HR"
  },
  
  "responsibilities": [
    "Creating Job Posting"                // Action + Object combination
  ],
  
  "relationships": {
    "related_entities": [
      "JOBS",                             // Creates job posting → JOBS entity
      "TALENTS"                            // Assigned to HR Manager → TALENTS entity
    ],
    "step_templates": [
      "TEMPLATE-STEP-TASK-TEMPLATE-001-001"
    ]
  }
}
```

### Example 2: Step Template with Tool Connection

```json
{
  "step_id": "TEMPLATE-STEP-TASK-TEMPLATE-001-001",
  "step_name": "Select job template",
  
  "taxonomy": {
    "action": "Select",                   // From LIBRARIES/Actions
    "object": "Job Template",             // From LIBRARIES/Objects
    "tool": "Notion"                      // From LIBRARIES/Tools
  },
  
  "parent_task": {
    "task_id": "TASK-TEMPLATE-001",
    "task_name": "Create Job Posting"
  }
}
```

### Example 3: Task Template with Business Entity Connection

```json
{
  "template_id": "TASK-TEMPLATE-002",
  "task_name": "Send Follow-up Email to Old Clients",
  
  "taxonomy": {
    "action": "Send",                     // From LIBRARIES/Actions
    "object": "Follow-up Email",          // From LIBRARIES/Objects
    "tool": "Email",                      // From LIBRARIES/Tools
    "profession": "Sales Manager",       // From LIBRARIES/Professions
    "department": "Sales"
  },
  
  "responsibilities": [
    "Sending Follow-up Email"              // Action + Object combination
  ],
  
  "relationships": {
    "related_entities": [
      "BUSINESSES"                        // Targets old clients → BUSINESSES entity
    ]
  }
}
```

---

## 🔍 Troubleshooting

### Common Issues

**Issue: Taxonomy value not found in library**
- **Solution**: Check exact spelling and case in library file
- **Prevention**: Use copy-paste from library file, don't type manually

**Issue: Missing required taxonomy field**
- **Solution**: Review template requirements and add missing field
- **Prevention**: Use template validation checklist

**Issue: Orphaned relationship reference**
- **Solution**: Verify referenced template exists before creating relationship
- **Prevention**: Validate all references during template creation

**Issue: Unclear entity connection**
- **Solution**: Explicitly list related entities in relationships section
- **Prevention**: Document entity connections when creating templates

---

## 📚 Related Documents

- **[INDEX.md](./INDEX.md)** - Master index of all templates
- **[Task_Templates_Checklist-Item-003.md](./Task_Templates_Checklist-Item-003.md)** - Task Template index
- **[Step_Templates_Checklist-Item-003.md](./Step_Templates_Checklist-Item-003.md)** - Step Template index
- **[Project_Templates_Checklist-Item-003.md](./Project_Templates_Checklist-Item-003.md)** - Project Template index
- **[README.md](./README.md)** - Entity overview

### Library Files
- `Nov25/Libs 25/Actions/actions.json` - Actions library
- `Nov25/Libs 25/Objects/objects.json` - Objects library
- `Nov25/Libs 25/Tools/tools.json` - Tools library
- `Nov25/Libs 25/Professions/professions.json` - Professions library

### Related Entity Documentation
- `../LIBRARIES/README.md` - LIBRARIES entity documentation
- `../TALENTS/README.md` - TALENTS entity documentation
- `../JOBS/README.md` - JOBS entity documentation
- `../BUSINESSES/README.md` - BUSINESSES entity documentation

---

**Last Updated:** November 25, 2025  
**Maintained By:** Framework Architecture Team
