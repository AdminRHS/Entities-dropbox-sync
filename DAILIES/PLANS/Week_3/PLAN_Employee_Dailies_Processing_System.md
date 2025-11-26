# Employee Daily Files Processing System
## Multi-Script Sequence Plan

**Version**: 1.0
**Date**: 2025-11-19
**Purpose**: Process employee daily files from DAILIES/ using context from PROMPTS/ to generate structured summaries with taxonomy entity extraction

---

## Executive Summary

This system splits the PMT-070 Entity Identification prompt into **8 modular Python scripts** that work sequentially to:
1. Collect and organize daily employee files
2. Extract taxonomy entities (Actions, Objects, Responsibilities, Tools, Tasks, Milestones)
3. Generate structured 15-section markdown reports
4. Create aggregated summaries across multiple employees

---

## System Architecture

### Input Sources
- **Daily Files**: `C:\Users\Dell\Dropbox\ENTITIES\DAILIES\{day}/`
  - `daily_{id}_{name}.md` - Daily activity logs with transcripts
  - `task_{id}_{name}.md` - Task breakdowns
  - `plans_{id}_{name}.md` - Strategic plans

- **Context Prompts**: `C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\`
  - PMT-070: Entity Identification v1.2 (master extraction methodology)
  - PMT-033 to PMT-043: Department-specific daily report prompts

- **Taxonomy Libraries**: `C:\Users\Dell\Dropbox\ENTITIES\LIBRARIES\`
  - Actions_Master.json (429 actions)
  - phrase_matching_index.json (193 responsibilities)
  - Tools/ (190+ categorized tools)
  - skills_master.json (28 skills)
  - professions.json

### Output Formats
- **Intermediate**: JSON files per processing stage (debugging, inspection)
- **Final Reports**: Markdown files with 15 structured sections
- **Summary**: Cross-employee aggregated analysis

---

## Script Sequence (8 Scripts)

### Script 1: File Collector & Metadata Generator
**File**: `script_01_file_collector.py`
**Purpose**: Scan DAILIES directory, identify employee files, extract metadata
**PMT-070 Sections**: 1 (Metadata), 15 (Source Metadata & Provenance)

**Inputs**:
- DAILIES/{day}/ directories
- copy_log.json (department tracking)

**Processing**:
1. Scan date folders (17, 18, etc.)
2. Identify file patterns: `daily_{id}_{name}.md`, `task_{id}_{name}.md`, `plans_{id}_{name}.md`
3. Extract employee metadata:
   - Employee ID
   - Last Name, First Name
   - Department (from copy_log.json)
   - Date
   - File size, language
4. Create processing queue with priority

**Output**: `processing_queue.json`
```json
{
  "queue": [
    {
      "employee_id": "228_Kucherenko_Iuliia",
      "daily_file": "C:\\...\\daily_228_Kucherenko_Iuliia.md",
      "task_file": "C:\\...\\task_228_Kucherenko_Iuliia.md",
      "plans_file": "C:\\...\\plans_228_Kucherenko_Iuliia.md",
      "department": "Design",
      "date": "2025-11-17",
      "file_size": 1250,
      "language": "Ukrainian/English",
      "priority": 1
    }
  ]
}
```

---

### Script 2: Action & Object Extractor
**File**: `script_02_action_object_extractor.py`
**Purpose**: Extract verbs, categorize into 7 types (A-G), identify objects with probability scores
**PMT-070 Sections**: 3 (Action Extraction), 4 (Object Probability Marking)

**Inputs**:
- Daily files from processing_queue.json
- LIBRARIES/Actions_Master.json (429 actions)

**Processing**:
1. **Action Extraction**:
   - Extract all verbs from text
   - Categorize into 7 types:
     - A. CREATION (create, generate, build, design)
     - B. MODIFICATION (edit, update, refactor, optimize)
     - C. ANALYSIS (review, analyze, identify, research)
     - D. ORGANIZATION (organize, plan, structure, categorize)
     - E. COMMUNICATION (translate, document, share, present)
     - F. AGENTIC/AUTOMATION (deploy, automate, execute, trigger)
     - G. DATA OPERATIONS (extract, insert, migrate, transform)
   - Count frequency
   - Match against Actions_Master.json library
   - Flag new actions not in library

2. **Object Identification**:
   - For each action, identify objects (nouns/noun phrases)
   - Calculate probability scores:
     - HIGH (0.8-1.0): Direct objects with strong evidence
     - MEDIUM (0.5-0.79): Indirect objects with moderate evidence
     - LOW (< 0.5): Weak associations
   - Use phrase matching for multi-word objects

**Output**: `{id}_actions_objects.json`
```json
{
  "employee_id": "228_Kucherenko_Iuliia",
  "date": "2025-11-17",
  "actions": {
    "A_CREATION": [
      {"id": "ACT-044", "verb": "create", "count": 12, "status": "MATCHED"}
    ],
    "B_MODIFICATION": [
      {"id": "ACT-156", "verb": "edit", "count": 8, "status": "MATCHED"}
    ]
  },
  "objects": {
    "ACT-044": {
      "HIGH": [
        {"object": "lesson structure", "probability": 0.95, "evidence": "phrase_matching_index"},
        {"object": "video tutorials", "probability": 0.88, "status": "NEW"}
      ],
      "MEDIUM": [
        {"object": "documentation", "probability": 0.68, "status": "VERIFY"}
      ]
    }
  },
  "summary": {
    "total_actions": 15,
    "matched_actions": 15,
    "new_actions": 0,
    "total_objects": 32,
    "high_probability": 24,
    "medium_probability": 8
  }
}
```

---

### Script 3: Responsibility & Tool Identifier
**File**: `script_03_responsibility_tool_identifier.py`
**Purpose**: Form action+object pairs, identify tools used
**PMT-070 Sections**: 5 (Responsibility Formation), 6 (Tool Identification)

**Inputs**:
- {id}_actions_objects.json
- LIBRARIES/phrase_matching_index.json (193 responsibilities)
- LIBRARIES/Tools/ (categorized tools)

**Processing**:
1. **Responsibility Formation**:
   - Combine action + object pairs
   - Format: "ACT-### + object"
   - Match against phrase_matching_index.json
   - Assign department codes (DGN, DEV, AID, SLS, etc.)
   - Extract evidence (direct quotes from daily file)
   - Flag new responsibilities

2. **Tool Identification**:
   - Extract tool mentions from text (case-insensitive)
   - Match against Tools/ library:
     - TOOL-AI-### (AI/LLM tools)
     - TOOL-AUTO-### (Automation)
     - TOOL-DESIGN-### (Design software)
     - TOOL-DEV-### (Development)
     - TOOL-VIDEO-### (Video production)
     - TOOL-COMM-### (Communication)
     - TOOL-DATA-### (Data tools)
     - TOOL-FILE-### (File management)
   - Count mentions and extract context
   - Flag new tools with suggested categories

**Output**: `{id}_responsibilities_tools.json`
```json
{
  "employee_id": "228_Kucherenko_Iuliia",
  "responsibilities": {
    "matched": [
      {
        "id": "RSP-089",
        "action": "ACT-044",
        "object": "lesson structure",
        "department": "DGN",
        "evidence": "Create lesson structure in Lesson Library",
        "status": "MATCHED"
      }
    ],
    "new": [
      {
        "id": "RSP-NEW-001",
        "action": "ACT-089",
        "object": "interactive elements",
        "department": "DGN",
        "tools": ["TOOL-AI-008"],
        "evidence": "Generated AI code for flip cards, animations",
        "priority": "CRITICAL",
        "add_to": "phrase_matching_index.json"
      }
    ]
  },
  "tools": {
    "matched": [
      {
        "id": "TOOL-AI-028",
        "name": "GPT-5.1",
        "category": "AI",
        "mentions": 12,
        "context": ["Code generation", "Translation"],
        "library_path": "AI_Tools/OpenAI_GPT5.json"
      }
    ],
    "new": [
      {
        "name": "Whisper Flow",
        "suggested_category": "AI",
        "suggested_id": "TOOL-AI-###",
        "mentions": 15,
        "context": ["Audio transcription", "Meeting documentation"],
        "department": "ALL",
        "priority": "HIGH",
        "add_to": "Tools/AI_Tools/"
      }
    ]
  }
}
```

---

### Script 4: Task & Steps Clustering Engine
**File**: `script_04_task_steps_clustering.py`
**Purpose**: Group responsibilities into tasks with atomic steps
**PMT-070 Sections**: 7 (Task & Steps Clustering)

**Inputs**:
- {id}_responsibilities_tools.json

**Processing**:
1. **Task Clustering**:
   - Group related responsibilities by:
     - Common objects
     - Time proximity
     - Shared tools
     - Logical workflow sequence
   - Format: ACTION + OBJECT + CONTEXT
   - Assign task IDs (TST-###)
   - Link tools and responsibilities

2. **Steps Breakdown**:
   - Break each task into atomic steps
   - Assign step IDs (STP-###)
   - Create 6-step execution sequence pattern
   - Calculate duration per task
   - Determine department and status

**Output**: `{id}_tasks_steps.json`
```json
{
  "employee_id": "228_Kucherenko_Iuliia",
  "tasks": [
    {
      "id": "TSK-001",
      "name": "Create Online Academy Lessons with AI",
      "format": "Create + Online Academy Lessons + with AI assistance",
      "responsibilities": ["RSP-089", "RSP-NEW-001", "RSP-156", "RSP-201"],
      "tools": ["TOOL-LMS-030", "TOOL-AI-008", "TOOL-DEV-019"],
      "skills": ["SKL-015", "SKL-023"],
      "steps": [
        {"id": "STP-001", "order": 1, "action": "Create structure", "duration": "30min"},
        {"id": "STP-002", "order": 2, "action": "Generate code", "duration": "45min"},
        {"id": "STP-003", "order": 3, "action": "Copy content", "duration": "15min"},
        {"id": "STP-004", "order": 4, "action": "Preview", "duration": "20min"},
        {"id": "STP-005", "order": 5, "action": "Refine", "duration": "40min"},
        {"id": "STP-006", "order": 6, "action": "Publish", "duration": "10min"}
      ],
      "duration": "3-4 hours",
      "department": "DGN",
      "status": "Completed"
    }
  ]
}
```

---

### Script 5: Milestone & Workflow Builder
**File**: `script_05_milestone_workflow_builder.py`
**Purpose**: Cluster tasks into milestones, document workflows
**PMT-070 Sections**: 8 (Milestone Formation), 10 (Workflow Sequences)

**Inputs**:
- {id}_tasks_steps.json

**Processing**:
1. **Milestone Formation**:
   - Group related tasks into deliverable clusters
   - Identify:
     - Common timeline (morning/afternoon sessions)
     - Shared professions
     - Related deliverables
   - Assign milestone IDs (MLS-###)
   - Calculate complexity and duration

2. **Workflow Documentation**:
   - Extract end-to-end workflow sequences
   - Format: Trigger → Steps → Outcome
   - Identify:
     - Workflow triggers
     - Step-by-step process
     - Duration and frequency
   - Assign workflow IDs (WF-###)

**Output**: `{id}_milestones_workflows.json`
```json
{
  "employee_id": "228_Kucherenko_Iuliia",
  "milestones": [
    {
      "id": "MLS-001",
      "name": "AI Workflow Infrastructure",
      "tasks": ["TSK-001", "TSK-002", "TSK-003"],
      "timeline": "Morning session (09:00-12:00)",
      "professions": ["PRF-NEW-001", "PRF-015"],
      "deliverables": [
        "Functional multi-model system",
        "Documented workflows",
        "Tested integrations"
      ],
      "department": "AID",
      "status": "Completed",
      "complexity": "High",
      "duration": "3 hours"
    }
  ],
  "workflows": [
    {
      "id": "WF-001",
      "name": "Multi-Model AI Orchestration",
      "trigger": "Complex task requiring multiple AI models",
      "steps": [
        "Analyze task requirements → Identify model strengths",
        "Select primary model (GPT-5.1/Perplexity/Gemini) → Context-based choice",
        "Execute via Cursor interface → Single workspace",
        "Cross-verify results → Secondary model validation",
        "Document outcomes → Knowledge base"
      ],
      "duration": "15-30 min/task",
      "frequency": "10-15x/day"
    }
  ]
}
```

---

### Script 6: Profession & Dependency Analyzer
**File**: `script_06_profession_dependency_analyzer.py`
**Purpose**: Identify professions, analyze dependencies and blockers
**PMT-070 Sections**: 9 (Profession Identification), 11 (Dependencies and Blockers)

**Inputs**:
- {id}_milestones_workflows.json
- All previous JSON outputs
- LIBRARIES/professions.json

**Processing**:
1. **Profession Identification**:
   - Analyze skills and responsibilities demonstrated
   - Match against existing professions library
   - Identify new professions based on:
     - Unique skill combinations
     - Specialized responsibilities
     - Tool expertise
   - Assign profession IDs (PRF-###)

2. **Dependency Analysis**:
   - Extract task dependencies from text
   - Categorize:
     - Tool dependencies
     - Data dependencies
     - Process dependencies
   - Track status (Met/Unmet)

3. **Blocker Identification**:
   - Identify blockers from daily notes
   - Classify severity (HIGH/MEDIUM/LOW)
   - Assess impact
   - Track resolution status

**Output**: `{id}_analysis.json`
```json
{
  "employee_id": "228_Kucherenko_Iuliia",
  "professions": {
    "matched": [
      {
        "id": "PRF-015",
        "name": "Backend Developer",
        "skills": ["SKL-031", "SKL-023"],
        "responsibilities": ["RSP-044", "RSP-187", "RSP-156"]
      }
    ],
    "new": [
      {
        "id": "PRF-NEW-001",
        "name": "AI Engineer",
        "skills": ["SKL-NEW-002", "SKL-NEW-003"],
        "responsibilities": ["RSP-NEW-005", "RSP-NEW-006"],
        "tools": ["TOOL-AI-028", "TOOL-AI-004", "TOOL-DEV-044"],
        "department": "AID",
        "priority": "HIGH"
      }
    ]
  },
  "dependencies": [
    {
      "task": "TSK-001",
      "depends_on": "Cursor installed",
      "type": "Tool",
      "status": "Met"
    }
  ],
  "blockers": [
    {
      "blocker": "Time Tracker down",
      "severity": "HIGH",
      "impact": "Report submission failed",
      "resolution": "Escalated to IT",
      "status": "In Progress"
    }
  ]
}
```

---

### Script 7: Entity ID Assignment & Master List Generator
**File**: `script_07_entity_master_list.py`
**Purpose**: Assign IDs to all entities, create comprehensive master list
**PMT-070 Sections**: 12 (Entity ID Assignment & Master List)

**Inputs**:
- All previous JSON outputs

**Processing**:
1. **Entity ID Assignment**:
   - Collect all entities from previous stages
   - Assign unique IDs following format:
     - MLS-### (Milestones)
     - TST-### (Tasks)
     - STP-### (Steps)
     - ACT-### (Actions)
     - OBJ-### (Objects)
     - RSP-### (Responsibilities)
     - TOOL-{CATEGORY}-### (Tools)
     - SKL-### (Skills)
     - PRF-### (Professions)
     - WF-### (Workflows)
   - Validate ID uniqueness

2. **Master List Creation**:
   - Create comprehensive table with:
     - ID, Type, Name, Department, Source, Status
     - Enrichment flags (✅ MATCHED / ❌ NEW)
   - Calculate entity count summary
   - Generate library addition recommendations

3. **Library Path Mapping**:
   - For each new entity, provide exact library file path
   - Prioritize: CRITICAL / HIGH / MEDIUM

**Output**: `{id}_entity_master.json` + `{id}_entity_summary.md`
```json
{
  "employee_id": "228_Kucherenko_Iuliia",
  "entities": [
    {
      "id": "MLS-001",
      "type": "Milestone",
      "name": "AI Workflow Infrastructure",
      "department": "AID",
      "source": "daily_171125",
      "status": "Completed",
      "enrichment_flag": "MATCHED"
    },
    {
      "id": "RSP-NEW-001",
      "type": "Responsibility",
      "name": "generate interactive elements",
      "department": "DGN",
      "source": "daily_171125",
      "status": "New",
      "enrichment_flag": "NEW_CRITICAL",
      "add_to": "phrase_matching_index.json"
    }
  ],
  "summary": {
    "total_entities": 93,
    "matched": 36,
    "new": 57,
    "by_type": {
      "Milestones": {"matched": 0, "new": 3},
      "Tasks": {"matched": 0, "new": 8},
      "Actions": {"matched": 15, "new": 0},
      "Responsibilities": {"matched": 7, "new": 4}
    }
  },
  "library_additions": {
    "CRITICAL": [
      "RSP-NEW-001 → phrase_matching_index.json",
      "SKL-NEW-001 → skills_master.json"
    ],
    "HIGH": [
      "TOOL-AI-### (Whisper Flow) → Tools/AI_Tools/"
    ]
  }
}
```

---

### Script 8: Report Assembler & Formatter
**File**: `script_08_report_assembler.py`
**Purpose**: Assemble final markdown report with all 15 sections, generate summaries
**PMT-070 Sections**: All sections + Department prompts

**Inputs**:
- All JSON outputs
- PMT-070 template
- Department-specific prompts (PMT-033 to PMT-043)

**Processing**:
1. **Section Assembly**:
   - Generate all 15 sections in markdown format:
     1. METADATA
     2. EXECUTIVE SUMMARY
     3. ACTION EXTRACTION
     4. OBJECT PROBABILITY MARKING
     5. RESPONSIBILITY FORMATION
     6. TOOL IDENTIFICATION
     7. TASK & STEPS CLUSTERING
     8. MILESTONE FORMATION
     9. PROFESSION IDENTIFICATION
     10. WORKFLOW SEQUENCES
     11. DEPENDENCIES AND BLOCKERS
     12. ENTITY ID ASSIGNMENT & MASTER LIST
     13. HIERARCHICAL RELATIONSHIP TREES (ASCII)
     14. DEPARTMENT DISTRIBUTION ANALYSIS
     15. SOURCE METADATA & PROVENANCE

2. **ASCII Tree Generation**:
   - Create hierarchical trees showing entity relationships
   - Format with proper ASCII characters (├── └── │)
   - Include enrichment markers

3. **Department Distribution**:
   - Calculate work distribution across departments
   - Create table format

4. **Validation**:
   - Validate against PMT-070 checklist:
     - Format (Markdown-only, all sections present)
     - Content (proper categorization, IDs, scores)
     - Integration (ID formats, dept codes, counts)

5. **Summary Generation**:
   - Create cross-employee aggregated summary
   - Combine multiple processed files
   - Generate department-level insights

**Output**:
- `daily_processed_{id}_{name}.md` (15-section report)
- `PROCESSING_SUMMARY.md` (aggregated summary)

---

## Supporting Files

### Utilities Module
**File**: `utils.py`

**Functions**:
- `load_json(filepath)` - Load JSON with UTF-8 encoding
- `save_json(data, filepath)` - Save JSON with proper formatting
- `load_markdown(filepath)` - Load markdown with multilingual support
- `save_markdown(content, filepath)` - Save markdown
- `load_library(library_name)` - Load taxonomy library files
- `get_department_from_log(employee_id)` - Parse copy_log.json
- `generate_entity_id(type, counter)` - Generate XXX-### format IDs
- `validate_entity_id(entity_id)` - Validate ID format
- `enrichment_marker(is_matched)` - Return ✅ or ❌
- `load_prompt_template(pmt_id)` - Load prompt from PROMPTS/
- `extract_employee_info(filename)` - Parse filename for ID, name
- `calculate_probability(action, object, context)` - Calculate object probability
- `categorize_action(verb)` - Assign action to A-G category
- `match_to_library(item, library)` - Fuzzy matching against library
- `create_ascii_tree(entities)` - Generate hierarchical ASCII tree

---

### Configuration File
**File**: `config.json`

```json
{
  "version": "1.0",
  "paths": {
    "dailies": "C:\\Users\\Dell\\Dropbox\\ENTITIES\\DAILIES",
    "prompts": "C:\\Users\\Dell\\Dropbox\\ENTITIES\\PROMPTS",
    "libraries": "C:\\Users\\Dell\\Dropbox\\ENTITIES\\LIBRARIES",
    "output": "C:\\Users\\Dell\\Dropbox\\ENTITIES\\DAILIES\\Output",
    "temp": "C:\\Users\\Dell\\Dropbox\\ENTITIES\\DAILIES\\temp"
  },
  "prompts": {
    "pmt_070": "UTILITIES/Daily_Updates/PMT-070_Entity_Identification_v1_2.md",
    "department_prompts": {
      "AI": "DEPARTMENTS/Daily_Reports/Department_Prompts/PMT-033_AI_Daily_Report.md",
      "Design": "DEPARTMENTS/Daily_Reports/Department_Prompts/PMT-035_Design_Daily_Report.md",
      "Dev": "DEPARTMENTS/Daily_Reports/Department_Prompts/PMT-036_Dev_Daily_Report.md",
      "HR": "DEPARTMENTS/Daily_Reports/Department_Prompts/PMT-038_HR_Daily_Report.md",
      "LG": "DEPARTMENTS/Daily_Reports/Department_Prompts/PMT-039_LG_Daily_Report.md",
      "Video": "DEPARTMENTS/Daily_Reports/Department_Prompts/PMT-043_Video_Daily_Report.md"
    }
  },
  "libraries": {
    "actions": "Actions_Master.json",
    "responsibilities": "phrase_matching_index.json",
    "tools_dir": "Tools/",
    "skills": "skills_master.json",
    "professions": "professions.json"
  },
  "action_categories": {
    "A": ["create", "generate", "build", "design", "develop"],
    "B": ["edit", "update", "modify", "refactor", "optimize"],
    "C": ["review", "analyze", "identify", "research", "investigate"],
    "D": ["organize", "plan", "structure", "categorize", "arrange"],
    "E": ["translate", "document", "share", "present", "communicate"],
    "F": ["deploy", "automate", "execute", "trigger", "schedule"],
    "G": ["extract", "insert", "migrate", "transform", "load"]
  },
  "tool_categories": [
    "AI", "AUTO", "DESIGN", "DEV", "VIDEO", "COMM", "DATA", "FILE"
  ],
  "probability_thresholds": {
    "HIGH": 0.8,
    "MEDIUM": 0.5,
    "LOW": 0.0
  },
  "enrichment_priorities": {
    "CRITICAL": "Immediate addition required",
    "HIGH": "Within 1 week",
    "MEDIUM": "Within 2 weeks",
    "LOW": "Nice to have"
  },
  "output_formats": {
    "intermediate": "json",
    "final": "md"
  },
  "processing": {
    "batch_size": 10,
    "parallel_processing": false,
    "log_level": "INFO"
  }
}
```

---

### Orchestrator Script
**File**: `run_pipeline.py`

**Purpose**: Execute all 8 scripts in sequence, handle errors, track progress

**Features**:
- Sequential execution of all scripts
- Error handling and retry logic
- Progress tracking and logging
- Batch processing for multiple employees
- Optional parallel processing (per employee)
- Performance metrics collection

**Usage**:
```bash
# Process all employees for a specific day
python run_pipeline.py --day 17

# Process specific employee
python run_pipeline.py --employee 228_Kucherenko_Iuliia

# Process multiple days
python run_pipeline.py --days 17,18

# Parallel processing (experimental)
python run_pipeline.py --day 17 --parallel
```

---

## Data Flow Diagram

```
INPUT SOURCES
│
├── DAILIES/{day}/
│   ├── daily_{id}_{name}.md
│   ├── task_{id}_{name}.md
│   └── plans_{id}_{name}.md
│
├── PROMPTS/
│   ├── PMT-070_Entity_Identification_v1_2.md
│   └── DEPARTMENTS/Daily_Reports/PMT-033 to PMT-043
│
└── LIBRARIES/
    ├── Actions_Master.json
    ├── phrase_matching_index.json
    ├── Tools/
    ├── skills_master.json
    └── professions.json

        ↓

PROCESSING PIPELINE
│
├── [Script 1] File Collector
│   └── → processing_queue.json
│
├── [Script 2] Action & Object Extractor
│   └── → {id}_actions_objects.json
│
├── [Script 3] Responsibility & Tool Identifier
│   └── → {id}_responsibilities_tools.json
│
├── [Script 4] Task & Steps Clustering
│   └── → {id}_tasks_steps.json
│
├── [Script 5] Milestone & Workflow Builder
│   └── → {id}_milestones_workflows.json
│
├── [Script 6] Profession & Dependency Analyzer
│   └── → {id}_analysis.json
│
├── [Script 7] Entity Master List Generator
│   └── → {id}_entity_master.json
│   └── → {id}_entity_summary.md
│
└── [Script 8] Report Assembler
    └── → daily_processed_{id}_{name}.md (15 sections)
    └── → PROCESSING_SUMMARY.md

        ↓

OUTPUT LOCATION
└── DAILIES/Output/
    ├── daily_processed_{id}_{name}.md
    ├── PROCESSING_SUMMARY.md
    └── temp/
        └── {intermediate JSON files}
```

---

## Implementation Phases

### Phase 1: Setup & Infrastructure (Week 1)
- Create project structure
- Implement utilities module
- Create configuration file
- Test file reading/writing with UTF-8 and multilingual support

### Phase 2: Core Extraction Scripts (Week 2-3)
- Build Script 1: File Collector
- Build Script 2: Action & Object Extractor
- Build Script 3: Responsibility & Tool Identifier
- Test with sample daily files

### Phase 3: Clustering & Analysis Scripts (Week 3-4)
- Build Script 4: Task & Steps Clustering
- Build Script 5: Milestone & Workflow Builder
- Build Script 6: Profession & Dependency Analyzer
- Validate intermediate outputs

### Phase 4: Assembly & Reporting (Week 4-5)
- Build Script 7: Entity Master List Generator
- Build Script 8: Report Assembler
- Implement ASCII tree generation
- Validate final markdown outputs

### Phase 5: Integration & Testing (Week 5-6)
- Build orchestrator script
- End-to-end testing with multiple employees
- Performance optimization
- Error handling improvements

### Phase 6: Documentation & Deployment (Week 6)
- Create README documentation
- Usage examples
- Troubleshooting guide
- Production deployment

---

## Validation & Quality Assurance

### Per-Script Validation
Each script includes:
- Schema validation for JSON outputs
- Required field checks
- ID format validation (XXX-###)
- Enrichment flag consistency (✅ ❌)
- Error logging

### Final Report Validation (PMT-070 Checklist)

**Format Checks**:
- [ ] Markdown output only (no CSV/JSON)
- [ ] All 15 sections present
- [ ] Master list is markdown table with Flag column
- [ ] ASCII trees use correct characters (├── └── │)

**Content Checks**:
- [ ] Actions categorized into 7 types (A-G)
- [ ] Objects have probability scores
- [ ] Responsibilities match action+object pattern
- [ ] Tools use TOOL-{CATEGORY}-### format
- [ ] Library enrichment complete for all entity types

**Integration Checks**:
- [ ] All IDs follow XXX-### format
- [ ] Department codes valid (AID, DEV, DGN, SLS, HRM, etc.)
- [ ] Master list count matches tree count
- [ ] Enrichment flags correct (✅ MATCHED / ❌ NEW)
- [ ] Library paths provided for all new entities

---

## Expected Outputs

### Per-Employee Outputs
1. **Intermediate JSON files** (7 files per employee):
   - processing_queue.json
   - {id}_actions_objects.json
   - {id}_responsibilities_tools.json
   - {id}_tasks_steps.json
   - {id}_milestones_workflows.json
   - {id}_analysis.json
   - {id}_entity_master.json

2. **Final Markdown Report**:
   - daily_processed_{id}_{name}.md (15 sections, ~500-2000 lines)

### Aggregated Outputs
1. **Cross-Employee Summary**:
   - PROCESSING_SUMMARY.md
   - Department-level insights
   - Entity statistics
   - Library enrichment recommendations

---

## Performance Metrics

### Processing Time Estimates
- Script 1 (File Collector): ~1-2 min for 50 employees
- Script 2 (Action/Object): ~3-5 min per employee
- Script 3 (Responsibility/Tool): ~2-3 min per employee
- Script 4 (Task/Steps): ~2-3 min per employee
- Script 5 (Milestone/Workflow): ~1-2 min per employee
- Script 6 (Profession/Dependency): ~1-2 min per employee
- Script 7 (Entity Master): ~1 min per employee
- Script 8 (Report Assembly): ~2-3 min per employee

**Total**: ~15-20 minutes per employee (sequential)

### Optimization Opportunities
- Parallel processing per employee (reduce to ~5-8 min for batch)
- Caching library files in memory
- Incremental processing (only new daily files)
- Multi-threading for JSON operations

---

## Error Handling

### Common Errors & Solutions
1. **File not found**: Check paths in config.json
2. **Encoding errors**: Ensure UTF-8 for all file operations
3. **Library mismatch**: Validate library file formats
4. **ID conflicts**: Check entity_master for duplicates
5. **Missing sections**: Validate intermediate JSON completeness

### Logging Strategy
- INFO: Processing progress, file counts
- WARNING: Missing files, library mismatches
- ERROR: Critical failures, invalid data
- DEBUG: Detailed entity extraction, matching results

---

## Future Enhancements

### Phase 2 Features (Post-MVP)
1. **Skills Recognition**: Implement Responsibility + Tool = Skill logic
2. **Library Enrichment Automation**: Auto-add new entities to libraries
3. **Web Dashboard**: Visualize entity relationships, department analytics
4. **Real-time Processing**: Process daily files as they're created
5. **AI-Powered Categorization**: Use LLMs for better action/object extraction
6. **Multi-language NLP**: Improve Ukrainian/Russian text processing
7. **Dependency Graph Visualization**: Interactive dependency trees

---

## Maintenance & Updates

### Regular Tasks
- Update action categories as new verbs emerge
- Refresh tool library quarterly
- Review and merge new responsibilities monthly
- Archive old daily files annually

### Version Control
- Use semantic versioning (MAJOR.MINOR.PATCH)
- Tag releases in git
- Maintain CHANGELOG.md
- Document breaking changes

---

## Contact & Support

**System Owner**: Niko
**Documentation**: C:\Users\Dell\Dropbox\ENTITIES\PLANS\
**Issues**: Track in project issue log
**Updates**: Document in CHANGELOG.md

---

**END OF PLAN**
