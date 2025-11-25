# DEPARTMENTS Library - Data Architecture Plan

**Created:** November 25, 2025  
**Source:** Overview folder deep analysis files  
**Target:** ENTITIES/LIBRARIES/DEPARTMENTS  
**Status:** Planning Phase

---

## 📋 Executive Summary

This architecture plan defines the data structure for organizing department information from the `Overview` folder into a structured, queryable format within the `ENTITIES/LIBRARIES/DEPARTMENTS` library. The structure will enable:

- **Centralized Department Data**: Single source of truth for all department information
- **Queryable Structure**: JSON-based format for programmatic access
- **Cross-Entity Integration**: Links to related entities (Employees, Tasks, Tools, etc.)
- **Scalability**: Easy to extend with new departments or data fields
- **Consistency**: Aligned with existing ENTITIES ecosystem patterns

---

## 🎯 Data Sources

### Source Files (Overview Folder)
- `AI_Department_Deep_Analysis.md`
- `Design_Department_Deep_Analysis.md`
- `Dev_Department_Deep_Analysis.md`
- `HR_Department_Deep_Analysis.md`
- `LG_Department_Deep_Analysis.md`
- `Video_Department_Deep_Analysis.md`
- `*_Department_Analysis_Process_Log.md` (process documentation)

### Key Data Extracted
1. **Team Composition** - Employees, roles, skills, status
2. **Workflow Patterns** - Daily workflows, file structures, processes
3. **Tools & Platforms** - Software, services, integrations
4. **Metrics & KPIs** - Performance data, statistics
5. **Responsibilities** - Core functions, deliverables
6. **Structure** - Folder organization, file patterns
7. **Projects** - Active initiatives, status
8. **Integration Points** - Cross-department dependencies

---

## 📐 Proposed Folder Structure

```
ENTITIES/LIBRARIES/LBS_006_Departments/
├── departments.json                    # Master department list (EXISTING)
├── README.md                           # Library documentation (EXISTING)
├── README_SHARED_RESOURCES.md          # Shared resources (EXISTING)
│
├── By_Department/                      # Department-specific data (NEW)
│   ├── AI/
│   │   ├── overview.json               # Complete department overview
│   │   ├── team_composition.json       # Employees, roles, structure
│   │   ├── task_managers_reference.json # References to TASK_MANAGERS structure
│   │   ├── tools_reference.json        # References to LIBRARIES/LBS_003_LBS_003_Tools/
│   │   ├── objects_reference.json      # References to LIBRARIES/Objects/ used by department
│   │   ├── metrics.json                # KPIs, statistics, performance
│   │   ├── projects.json                # Active projects and initiatives
│   │   ├── structure.json               # Folder structure, file patterns
│   │   └── integration.json             # Cross-department dependencies
│   │
│   ├── DESIGN/
│   │   ├── overview.json
│   │   ├── team_composition.json
│   │   ├── task_managers_reference.json
│   │   ├── tools_reference.json
│   │   ├── objects_reference.json
│   │   ├── metrics.json
│   │   ├── projects.json
│   │   ├── structure.json
│   │   └── integration.json
│   │
│   ├── DEV/
│   ├── DGN/                      # Alternative code for DESIGN
│   ├── FIN/
│   ├── HR/
│   ├── LG/
│   ├── SALES/
│   ├── SMM/
│   └── VIDEO/
│
├── Index/                              # Cross-department indexes (NEW)
│   ├── all_employees.json              # All employees across departments
│   ├── tools_summary.json              # Summary of tools by department (references LIBRARIES/LBS_003_LBS_003_Tools/)
│   ├── objects_summary.json            # Summary of objects by department (references LIBRARIES/Objects/)
│   ├── all_projects.json               # All active projects
│   ├── task_templates_summary.json     # Summary of all task templates by department
│   ├── step_templates_summary.json     # Summary of all step templates by department
│   └── integration_matrix.json         # Department dependency matrix
│
├── Reports/                            # Generated reports (EXISTING)
│   └── System_Analysis/
│
├── RESEARCHES/                          # Research files (EXISTING)
│
└── Archive/                            # Historical data (EXISTING)
```

---

## 📊 Data Structure Specifications

### 1. `departments.json` (Master List) - EXISTING ✅

**Purpose:** Master reference for all departments

**Current Structure:**
```json
{
  "version": "1.0",
  "source": "ENTITIES/LIBRARIES/DEPARTMENTS",
  "created_date": "2025-11-25",
  "total_departments": 10,
  "data": [
    {
      "id": 1,
      "code": "AI",
      "name": "Artificial Intelligence",
      "full_name": "Artificial Intelligence Department",
      "description": "AI operations, prompt engineering, automation, LLM integration",
      "color": "rgb(61, 183, 124)",
      "is_active": true
    }
  ]
}
```

**Status:** ✅ Complete - No changes needed

---

### 2. `By_Department/{CODE}/overview.json` (NEW)

**Purpose:** High-level department summary and executive information

**Structure:**
```json
{
  "department_id": 1,
  "department_code": "AI",
  "department_name": "Artificial Intelligence",
  "analysis_date": "2025-11-16",
  "team_size": 3,
  "location": "C:\Users\Dell\Dropbox\Nov25\AI Nov25",
  
  "executive_summary": {
    "role": "transformation engine for AI-first operational model",
    "key_metrics": {
      "team": "3 employees (1 PM + 2 Prompt Engineers)",
      "active_projects": 18,
      "file_system_adoption": "Design 100%, LG in progress",
      "administrative_overhead_reduction": "60-80%",
      "tool_library_size": 29,
      "documentation_lines": 2490,
      "actions_library_size": 429
    },
    "primary_functions": [
      "Documentation automation",
      "Task management",
      "Video processing",
      "Knowledge centralization"
    ]
  },
  
  "geographic_distribution": {
    "primary_location": "Ukraine",
    "time_zones": ["EET"],
    "languages": ["English", "Ukrainian"]
  },
  
  "status": {
    "is_active": true,
    "file_system_status": "implemented",
    "compliance_rate": "100%",
    "last_updated": "2025-11-16"
  }
}
```

---

### 3. `By_Department/{CODE}/team_composition.json` (NEW)

**Purpose:** Detailed team structure, employees, roles, and skills

**Structure:**
```json
{
  "department_id": 1,
  "department_code": "AI",
  "total_employees": 3,
  "last_updated": "2025-11-16",
  
  "employees": [
    {
      "employee_id": 37226,
      "full_name": "Artemchuk Nikolay",
      "role": "Project Manager, Lead Generator",
      "is_department_lead": true,
      "status": "Working",
      "workload": "VERY HIGH",
      
      "primary_responsibilities": [
        "Leading AI-first organizational transformation",
        "Project management and team coordination",
        "File system rollout coordination"
      ],
      
      "current_projects": [
        "File System Project rollout",
        "LG Department strategic evaluation",
        "Weekly department call structure"
      ],
      
      "skills": {
        "project_management": ["Agile", "SCRUM", "Kanban", "Waterfall"],
        "tools": ["Asana", "Jira", "Miro", "Monday", "Notion", "Trello", "Slack"],
        "ai_tools": ["ChatGPT", "Claude", "Cursor"],
        "specialties": ["Account Management", "Data Processing", "Personnel Management"]
      },
      
      "background": "Project Management",
      "location": "Ukraine"
    }
  ],
  
  "roles_summary": {
    "project_manager": 1,
    "prompt_engineers": 2
  },
  
  "leadership_structure": {
    "department_lead": {
      "employee_id": 37226,
      "name": "Artemchuk Nikolay"
    },
    "team_leads": []
  }
}
```

---

### 4. `By_Department/{CODE}/task_managers_reference.json` (NEW)

**Purpose:** References to TASK_MANAGERS structure (Task Templates, Step Templates, Project Templates, Workflows)

**Structure:**
```json
{
  "department_id": 1,
  "department_code": "AI",
  "last_updated": "2025-11-25",
  
  "task_managers_path": "ENTITIES/TASK_MANAGERS",
  
  "task_templates": {
    "listing_file": "ENTITIES/TASK_MANAGERS/Task_Templates/Listing.json",
    "department_folder": "ENTITIES/TASK_MANAGERS/Task_Templates/AI/",
    "total_templates": 75,
    "template_ids": [
      "TASK-AI-001",
      "TASK-AI-002",
      "TASK-AI-021"
    ],
    "summary": {
      "by_complexity": {
        "low": 15,
        "medium": 45,
        "high": 15
      },
      "by_status": {
        "active": 70,
        "archived": 5
      },
      "total_estimated_hours": 450.0
    }
  },
  
  "step_templates": {
    "listing_file": "ENTITIES/TASK_MANAGERS/Step_Templates/Listing.json",
    "department_folder": "ENTITIES/TASK_MANAGERS/Step_Templates/AI/",
    "total_steps": 340,
    "summary": {
      "by_task": {
        "TASK-AI-001": 6,
        "TASK-AI-002": 8
      },
      "total_steps": 340
    }
  },
  
  "project_templates": {
    "department_folder": "ENTITIES/TASK_MANAGERS/Project_Templates/",
    "templates": [
      {
        "id": "TEMPLATE-PROJ-AI-002",
        "name": "AI Tutorial Research Pipeline",
        "file": "ENTITIES/TASK_MANAGERS/Project_Templates/TEMPLATE-PROJ-AI-002.json",
        "total_tasks": 10,
        "total_phases": 9,
        "total_milestones": 3
      }
    ],
    "total_templates": 2
  },
  
  "workflows": {
    "department_folder": "ENTITIES/TASK_MANAGERS/Workflows/",
    "workflow_files": [
      {
        "file": "ENTITIES/TASK_MANAGERS/Workflows/AI_Automation_Workflow.yaml",
        "type": "Linear",
        "department": "AI",
        "description": "AI automation workflow"
      }
    ],
    "total_workflows": 1
  },
  
  "milestone_templates": {
    "department_folder": "ENTITIES/TASK_MANAGERS/Milestone_Templates/",
    "templates": [
      {
        "id": "MT-Data_Inventory",
        "file": "ENTITIES/TASK_MANAGERS/Milestone_Templates/MT-Data_Inventory.json"
      }
    ],
    "total_templates": 5
  },
  
  "file_system_structure": {
    "pattern": "Week_X/DD/",
    "status": "implemented",
    "adoption_rate": "100%",
    "three_file_system": {
      "enabled": true,
      "files": [
        {
          "name": "daily.md",
          "purpose": "Daily activity log with timestamps and transcripts",
          "required": true
        },
        {
          "name": "plans.md",
          "purpose": "Strategic next-day plan generated from daily.md",
          "required": true
        },
        {
          "name": "task.md",
          "purpose": "Detailed actionable steps with links and resources",
          "required": true
        }
      ]
    }
  },
  
  "quality_control": {
    "yellow_card_system": {
      "enabled": true,
      "max_cards_per_month": 3,
      "reset_date": "1st of each month",
      "violations": [
        "incomplete/missing daily.md",
        "no plans/tasks",
        "wrong location",
        "missing transcripts"
      ]
    }
  }
}
```

---

### 5. `By_Department/{CODE}/objects_reference.json` (NEW)

**Purpose:** References to objects from LIBRARIES/Objects/ used by the department

**Structure:**
```json
{
  "department_id": 1,
  "department_code": "AI",
  "last_updated": "2025-11-25",
  
  "libraries_objects_path": "ENTITIES/LIBRARIES/Objects/",
  "master_objects_file": "ENTITIES/LIBRARIES/objects.json",
  
  "object_categories": {
    "AI_Automation_Objects": {
      "file": "ENTITIES/LIBRARIES/Objects/AI_Automation_Objects.json",
      "objects_used": [
        "prompts",
        "workflows",
        "automations",
        "models"
      ],
      "object_types": {
        "prompts": ["optimized prompts", "compressed prompts", "system prompts"],
        "workflows": ["n8n workflows", "automation workflows", "data processing workflows"]
      }
    },
    "Documents": {
      "file": "ENTITIES/LIBRARIES/Objects/Documents.json",
      "objects_used": [
        "reports",
        "documentation",
        "guides"
      ]
    },
    "RAG_Objects": {
      "file": "ENTITIES/LIBRARIES/Objects/RAG_Objects.json",
      "objects_used": [
        "embeddings",
        "knowledge_bases",
        "vector_databases"
      ]
    }
  },
  
  "objects_from_master": [
    {
      "object": "videos",
      "object_types": ["tutorial videos", "transcription videos", "workflow videos"],
      "source": "ENTITIES/LIBRARIES/objects.json",
      "used_in_tasks": ["TASK-AI-021", "TASK-AI-022"]
    },
    {
      "object": "reports",
      "object_types": ["daily report", "analysis report", "extraction report"],
      "source": "ENTITIES/LIBRARIES/objects.json"
    }
  ],
  
  "summary": {
    "total_objects": 15,
    "from_categories": 8,
    "from_master": 7
  }
}
```

---

### 6. `By_Department/{CODE}/tools_reference.json` (NEW)

**Purpose:** References to tools from LIBRARIES/LBS_003_LBS_003_Tools/ used by the department

**Structure:**
```json
{
  "department_id": 1,
  "department_code": "AI",
  "last_updated": "2025-11-25",
  
  "libraries_tools_path": "ENTITIES/LIBRARIES/LBS_003_LBS_003_Tools/",
  
  "tool_categories": {
    "AI_Tools": {
      "path": "ENTITIES/LIBRARIES/LBS_003_LBS_003_Tools/By_Category/AI/",
      "tools": [
        {
          "tool_file": "ENTITIES/LIBRARIES/LBS_003_LBS_003_Tools/By_Category/AI/ChatGPT.json",
          "usage_frequency": "daily",
          "primary_users": [37226, 86246, 86981],
          "is_critical": true
        },
        {
          "tool_file": "ENTITIES/LIBRARIES/LBS_003_LBS_003_Tools/By_Category/AI/Claude.json",
          "usage_frequency": "daily",
          "primary_users": [37226, 86246, 86981],
          "is_critical": true
        }
      ],
      "total_tools": 13
    },
    "Development_Tools": {
      "path": "ENTITIES/LIBRARIES/LBS_003_LBS_003_Tools/By_Category/Development/",
      "tools": [
        {
          "tool_file": "ENTITIES/LIBRARIES/LBS_003_LBS_003_Tools/By_Category/Development/Cursor.json",
          "usage_frequency": "daily",
          "is_critical": true
        }
      ],
      "total_tools": 8
    },
    "Automation_Tools": {
      "path": "ENTITIES/LIBRARIES/LBS_003_LBS_003_Tools/By_Category/Automation/",
      "tools": [
        {
          "tool_file": "ENTITIES/LIBRARIES/LBS_003_LBS_003_Tools/By_Category/Automation/n8n.json",
          "usage_frequency": "daily",
          "is_critical": true
        }
      ],
      "total_tools": 3
    }
  },
  
  "summary": {
    "total_tools": 29,
    "critical_tools": 15,
    "daily_use": 20,
    "weekly_use": 9
  }
}
```

---

### 7. `By_Department/{CODE}/metrics.json` (NEW)

**Purpose:** KPIs, statistics, and performance metrics

**Structure:**
```json
{
  "department_id": 1,
  "department_code": "AI",
  "reporting_period": "2025-11",
  "last_updated": "2025-11-16",
  
  "team_metrics": {
    "team_size": 3,
    "active_employees": 3,
    "on_leave": 0,
    "attrition_rate": "0%"
  },
  
  "performance_metrics": {
    "file_system_adoption": {
      "department": "100%",
      "cross_department": {
        "DESIGN": "100%",
        "LG": "in_progress"
      }
    },
    "administrative_overhead_reduction": "60-80%",
    "documentation_quality": {
      "training_guides_lines": 2490,
      "daily_reports_lines": 1165,
      "compliance_rate": "100%"
    }
  },
  
  "project_metrics": {
    "active_projects": 18,
    "completed_this_month": 5,
    "in_progress": 13,
    "success_rate": "95%"
  },
  
  "tool_metrics": {
    "tools_documented": 29,
    "tools_in_use": 25,
    "integration_count": 15
  },
  
  "library_metrics": {
    "actions_library_size": 429,
    "objects_library_size": 150,
    "tools_library_size": 29
  }
}
```

---

### 8. `By_Department/{CODE}/projects.json` (NEW)

**Purpose:** Active projects and initiatives

**Structure:**
```json
{
  "department_id": 1,
  "department_code": "AI",
  "last_updated": "2025-11-16",
  
  "projects": [
    {
      "project_id": "PROJ-AI-FS-001",
      "name": "File System Project Rollout",
      "status": "in_progress",
      "priority": "high",
      "start_date": "2025-11-01",
      "target_completion": "2025-11-30",
      "owner": {
        "employee_id": 37226,
        "name": "Artemchuk Nikolay"
      },
      "description": "Rollout of Week_X/DD/ file structure across all departments",
      "progress": {
        "completed": ["DESIGN"],
        "in_progress": ["LG"],
        "pending": ["DEV", "HR", "SALES", "VIDEO"]
      },
      "dependencies": [],
      "related_projects": []
    }
  ],
  
  "summary": {
    "total_projects": 18,
    "active": 13,
    "completed": 5,
    "on_hold": 0
  }
}
```

---

### 9. `By_Department/{CODE}/structure.json` (NEW)

**Purpose:** Folder structure, file patterns, and organization

**Structure:**
```json
{
  "department_id": 1,
  "department_code": "AI",
  "base_path": "C:\\Users\\Dell\\Dropbox\\Nov25\\AI Nov25",
  "last_updated": "2025-11-16",
  
  "folder_structure": {
    "pattern": "Week_X/DD/",
    "status": "implemented",
    "adoption_rate": "100%",
    "example_path": "AI Nov25/Employee Name/Week_1/03/",
    
    "required_files": [
      "daily.md",
      "plans.md",
      "task.md"
    ],
    
    "optional_folders": [
      "TEAMLEADS/",
      "Projects/",
      "Reports/",
      "prompt/"
    ]
  },
  
  "file_patterns": {
    "daily_log": {
      "pattern": "daily.md",
      "location": "Week_X/DD/",
      "required": true,
      "content_type": "markdown",
      "sections": [
        "timestamped_activities",
        "whisper_flow_transcripts",
        "outcomes_results"
      ]
    },
    "plans": {
      "pattern": "plans.md",
      "location": "Week_X/DD/",
      "required": true,
      "content_type": "markdown",
      "sections": [
        "review_of_daily",
        "prioritized_action_items",
        "goals_objectives"
      ]
    },
    "tasks": {
      "pattern": "task.md",
      "location": "Week_X/DD/",
      "required": true,
      "content_type": "markdown",
      "sections": [
        "step_by_step_breakdown",
        "links_resources",
        "execution_instructions"
      ]
    }
  },
  
  "special_folders": {
    "TEAMLEADS": {
      "purpose": "Shared documentation for team leads",
      "files": [
        "instructions.md",
        "plans.md",
        "meetings.md"
      ]
    },
    "Projects": {
      "purpose": "Department-specific project files",
      "structure": "project_name/"
    }
  }
}
```

---

### 10. `By_Department/{CODE}/integration.json` (NEW)

**Purpose:** Cross-department dependencies and integration points

**Structure:**
```json
{
  "department_id": 1,
  "department_code": "AI",
  "last_updated": "2025-11-16",
  
  "dependencies": {
    "depends_on": [],
    "depended_by": [
      {
        "department_code": "DESIGN",
        "dependency_type": "file_system_rollout",
        "description": "AI coordinates file system implementation"
      },
      {
        "department_code": "LG",
        "dependency_type": "file_system_rollout",
        "description": "AI coordinates file system implementation"
      }
    ]
  },
  
  "integrations": {
    "provides_to": [
      {
        "department_code": "ALL",
        "service": "documentation_automation",
        "description": "AI tools and workflows for documentation"
      },
      {
        "department_code": "ALL",
        "service": "prompt_optimization",
        "description": "Prompt engineering and optimization services"
      }
    ],
    "receives_from": [
      {
        "department_code": "VIDEO",
        "service": "video_transcripts",
        "description": "Video processing and transcript extraction"
      }
    ]
  },
  
  "shared_resources": [
    {
      "resource": "ENTITIES/LIBRARIES/LBS_006_Departments/_SHARED/Prompts/",
      "shared_with": ["ALL"],
      "access_type": "read"
    }
  ],
  
  "cross_department_projects": [
    {
      "project_id": "PROJ-AI-FS-001",
      "involves": ["DESIGN", "LG", "DEV", "HR", "SALES", "VIDEO"],
      "ai_role": "coordinator"
    }
  ]
}
```

---

## 📑 Index Files Structure

### 10. `Index/all_employees.json` (NEW)

**Purpose:** Cross-department employee directory

**Structure:**
```json
{
  "version": "1.0",
  "last_updated": "2025-11-25",
  "total_employees": 32,
  
  "employees": [
    {
      "employee_id": 37226,
      "full_name": "Artemchuk Nikolay",
      "department_code": "AI",
      "department_id": 1,
      "role": "Project Manager",
      "is_department_lead": true,
      "status": "Working"
    }
  ],
  
  "by_department": {
    "AI": 3,
    "DESIGN": 9,
    "DEV": 3,
    "HR": 2,
    "LG": 22,
    "SALES": 1,
    "VIDEO": 3
  }
}
```

### 11. `Index/tools_summary.json` (NEW)

**Purpose:** Summary of tools by department (references LIBRARIES/LBS_003_LBS_003_Tools/)

**Structure:**
```json
{
  "version": "1.0",
  "last_updated": "2025-11-25",
  "libraries_tools_path": "ENTITIES/LIBRARIES/LBS_003_LBS_003_Tools/",
  "master_tools_file": "ENTITIES/LIBRARIES/tools.json",
  
  "by_department": {
    "AI": {
      "tool_categories": ["AI_Tools", "Development_Tools", "Automation_Tools"],
      "total_tools": 29,
      "critical_tools": 15
    },
    "DESIGN": {
      "tool_categories": ["Development_Tools", "Social_Media_Platforms"],
      "total_tools": 18,
      "critical_tools": 8
    }
  },
  
  "shared_tools": [
    {
      "tool_file": "ENTITIES/LIBRARIES/LBS_003_LBS_003_Tools/File_Management/Dropbox.json",
      "shared_by": 7,
      "departments": ["AI", "DESIGN", "DEV", "HR", "LG", "SALES", "VIDEO"]
    }
  ],
  
  "by_category": {
    "AI_Tools": {
      "count": 25,
      "departments": ["AI", "DESIGN", "DEV", "HR", "LG", "SALES", "VIDEO"]
    },
    "Development_Tools": {
      "count": 30,
      "departments": ["AI", "DESIGN", "DEV"]
    }
  }
}
```

### 12. `Index/objects_summary.json` (NEW)

**Purpose:** Summary of objects by department (references LIBRARIES/Objects/)

**Structure:**
```json
{
  "version": "1.0",
  "last_updated": "2025-11-25",
  "libraries_objects_path": "ENTITIES/LIBRARIES/Objects/",
  "master_objects_file": "ENTITIES/LIBRARIES/objects.json",
  
  "by_department": {
    "AI": {
      "object_categories": ["AI_Automation_Objects", "Documents", "RAG_Objects"],
      "objects_from_master": ["videos", "reports", "documentation"],
      "total_objects": 15
    },
    "HR": {
      "object_categories": ["Recruitment_Objects"],
      "objects_from_master": ["candidates", "interviews", "contracts", "reports"],
      "total_objects": 12
    },
    "DESIGN": {
      "object_categories": ["Design_Deliverables"],
      "objects_from_master": ["mockups", "logos", "illustrations"],
      "total_objects": 20
    }
  },
  
  "by_category": {
    "Recruitment_Objects": {
      "file": "ENTITIES/LIBRARIES/Objects/Recruitment_Objects.json",
      "departments": ["HR"],
      "objects": ["vacancies", "interviews", "job_requests", "candidates"]
    },
    "Design_Deliverables": {
      "file": "ENTITIES/LIBRARIES/Objects/Design_Deliverables.json",
      "departments": ["DESIGN"],
      "objects": ["banners", "logos", "mockups", "illustrations"]
    }
  },
  
  "common_objects": [
    {
      "object": "reports",
      "object_types": ["daily report", "monthly report", "department report"],
      "used_by": ["AI", "HR", "LG", "SALES"],
      "source": "ENTITIES/LIBRARIES/objects.json"
    }
  ]
}
```

### 13. `Index/integration_matrix.json` (NEW)

**Purpose:** Department dependency and integration matrix

**Structure:**
```json
{
  "version": "1.0",
  "last_updated": "2025-11-25",
  
  "matrix": {
    "AI": {
      "provides_to": ["ALL"],
      "receives_from": ["VIDEO"],
      "coordinates": ["DESIGN", "LG"]
    },
    "DESIGN": {
      "provides_to": ["DEV", "VIDEO"],
      "receives_from": ["AI"],
      "coordinates": []
    }
  },
  
  "dependency_graph": {
    "nodes": [
      {"id": "AI", "type": "coordinator"},
      {"id": "DESIGN", "type": "service_provider"},
      {"id": "DEV", "type": "service_provider"}
    ],
    "edges": [
      {"from": "AI", "to": "DESIGN", "type": "coordination"},
      {"from": "DESIGN", "to": "DEV", "type": "design_handoff"}
    ]
  }
}
```

---

## 🔄 Migration Plan

### Phase 1: Structure Setup (Day 1)
1. ✅ Create `By_Department/` folder structure
2. ✅ Create `Index/` folder structure
3. ✅ Create department subfolders (AI, DESIGN, DGN, DEV, FIN, HR, LG, SALES, SMM, VIDEO)

### Phase 2: Data Extraction (Days 2-3)
1. Parse `*_Department_Deep_Analysis.md` files from `Overview/` folder
   - Source: `C:\Users\Dell\Dropbox\Overview\`
   - Files: `AI_Department_Deep_Analysis.md`, `Design_Department_Deep_Analysis.md`, etc.
   - See `SOURCE_DATA_MAPPING.md` for complete file mapping
2. Extract structured data for each department
3. Link to existing LIBRARIES structure:
   - Reference objects from `LIBRARIES/Objects/` and `LIBRARIES/objects.json`
   - Reference tools from `LIBRARIES/LBS_003_LBS_003_Tools/` categories
   - Reference TASK_MANAGERS structure (Task_Templates, Step_Templates, Project_Templates, Workflows)
4. Create JSON files for each department:
   - overview.json
   - team_composition.json
   - task_managers_reference.json (references to TASK_MANAGERS structure)
   - tools_reference.json (references to LIBRARIES/LBS_003_LBS_003_Tools/)
   - objects_reference.json (references to LIBRARIES/Objects/)
   - metrics.json
   - projects.json
   - structure.json
   - integration.json

### Phase 3: Index Creation (Day 4)
1. Generate `Index/all_employees.json` from all departments
2. Generate `Index/tools_summary.json` from department tools_reference.json files (references LIBRARIES/LBS_003_LBS_003_Tools/)
3. Generate `Index/objects_summary.json` from department objects_reference.json files (references LIBRARIES/Objects/)
4. Generate `Index/integration_matrix.json` from integration data
5. Generate `Index/all_projects.json` from all departments
6. Generate `Index/task_templates_summary.json` from TASK_MANAGERS/Task_Templates/Listing.json
7. Generate `Index/step_templates_summary.json` from TASK_MANAGERS/Step_Templates/Listing.json

### Phase 4: Validation & Documentation (Day 5)
1. Validate JSON structure against schema
2. Cross-reference with existing ENTITIES data
3. Update README.md with new structure
4. Create migration log

---

## 📝 Implementation Notes

### Data Extraction Strategy
- **Automated Parsing**: Use Python scripts to parse markdown files
- **LIBRARIES Integration**: Reference existing LIBRARIES structure (Objects, Tools) instead of creating new categories
- **TASK_MANAGERS Integration**: Reference existing TASK_MANAGERS structure instead of duplicating workflow data
- **Naming Conventions**: Follow existing LIBRARIES naming patterns (lowercase, plural nouns for objects)
- **Manual Review**: Review extracted data for accuracy
- **Validation**: Cross-reference with existing ENTITIES data (LIBRARIES, TASK_MANAGERS, TALENTS)

### Consistency Requirements
- **Department Codes**: Use consistently (AI, DESIGN, DGN, DEV, FIN, HR, LG, SALES, SMM, VIDEO)
  - **DGN** is an alternative code for DESIGN department
  - **FIN** is the Finance department code
  - **SMM** is the Social Media Management department code
- **Objects**: Reference from `LIBRARIES/Objects/` and `LIBRARIES/objects.json` - use lowercase plural nouns
- **Object Types**: Use existing object types from LIBRARIES structure
- **Tools**: Reference from `LIBRARIES/LBS_003_LBS_003_Tools/` categories - use existing tool file structure
- **Naming Conventions**: Follow LIBRARIES patterns:
  - Objects: lowercase, plural (e.g., "candidates", "reports", "videos")
  - Object Types: lowercase, descriptive (e.g., "needed candidates", "daily report")
  - File names: `[Category]_[Type].json` pattern (e.g., `Recruitment_Objects.json`, `Design_Deliverables.json`)
- **Cross-References**: 
  - Link to employee IDs from TALENTS entity
  - Link to project IDs from ANALYTICS/Projects
  - Reference TASK_MANAGERS structure (Task_Templates, Step_Templates, Project_Templates, Workflows)
- **Paths**: Use relative paths: `ENTITIES/LIBRARIES/...`, `ENTITIES/TASK_MANAGERS/...`
- **Dates**: Use ISO date format (YYYY-MM-DD)

### Maintenance
- **Update Frequency**: Monthly or when major changes occur
- **Version Control**: Track changes in version field
- **Backup**: Archive old versions before updates

---

## 🎯 Success Criteria

- ✅ All 7 departments have complete data structure
- ✅ All JSON files validate against schema
- ✅ Cross-references to other entities are valid
- ✅ Index files are generated and accurate
- ✅ Documentation is complete and up-to-date
- ✅ Migration log documents all changes

---

## 📚 Related Documentation

- `departments.json` - Master department list
- `README.md` - Library documentation
- `ENTITIES/TALENTS/` - Employee directory
- `ENTITIES/LIBRARIES/` - Core library structure
  - `Objects/` - Object categories and definitions
    - `objects.json` - Master objects library
    - `Recruitment_Objects.json` - HR/Recruitment objects
    - `Design_Deliverables.json` - Design objects
    - `Lead_Generation_Objects.json` - Lead generation objects
    - `Video_Deliverables.json` - Video production objects
    - `object_types.json` - Object types by profession
  - `LBS_003_Tools/` - Tool categories organized by type
    - `AI_LBS_003_Tools/` - AI and LLM tools
    - `Development_LBS_003_Tools/` - Development tools
    - `Automation_LBS_003_Tools/` - Automation platforms
    - `tools.json` - Master tools library
  - `Actions/` - Standardized action verbs
  - `LBS_005_Professions/` - Profession definitions
- `ENTITIES/ANALYTICS/Projects/` - Project tracking
- `ENTITIES/TASK_MANAGERS/` - Task Templates, Step Templates, Project Templates, Workflows
  - `Task_Templates/Listing.json` - All task templates by department
  - `Step_Templates/Listing.json` - All step templates by department
  - `Project_Templates/` - Project template definitions
  - `Workflows/` - Workflow definitions (YAML files)
  - `Milestone_Templates/` - Milestone template definitions

---

---

## 📋 Department-Specific Integration Plans

### SMM Department
- **Status:** New department, no employees yet
- **Integration Plan:** `By_Department/SMM/INTEGRATION_PLAN.md`
- **Source Data:** `Nov25/SMM Nov25/` (comprehensive data ready)
- **Strategy:** Reference-based integration initially, full migration when ready

---

**Last Updated:** November 25, 2025  
**Next Review:** December 1, 2025

