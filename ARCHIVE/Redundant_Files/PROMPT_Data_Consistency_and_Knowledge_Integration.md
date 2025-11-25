# Prompt: Data Consistency & Knowledge Base Integration System

## Purpose
Establish a comprehensive system for maintaining data consistency, enabling machine-readable access, and creating a feedback loop where prompts extract and prepare data that automatically populates the LIBRARIES knowledge base.

---

## Core Principles

### 1. Data Consistency
- **Single Source of Truth:** LIBRARIES entities are the authoritative source
- **Schema Validation:** All data must conform to JSON schemas
- **Cross-Reference Integrity:** Maintain bidirectional relationships
- **Version Control:** Track changes and maintain backward compatibility
- **Naming Standards:** Enforce consistent naming conventions

### 2. Machine Accessibility
- **Structured JSON:** All entities stored as machine-readable JSON
- **API-Ready Format:** Compatible with microservice architecture
- **Index Files:** Quick lookup and search capabilities
- **Schema Documentation:** Clear structure definitions
- **Query Support:** Enable filtering, searching, and aggregation

### 3. Prompt-to-Knowledge Pipeline
- **Extract:** Prompts extract structured data from sources
- **Validate:** Data validated against LIBRARIES schemas
- **Transform:** Data formatted to match LIBRARIES structure
- **Populate:** Validated data added to LIBRARIES entities
- **Cross-Reference:** Automatic relationship mapping

---

## LIBRARIES Entity Schemas

### Actions Schema
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Actions",
  "action_id": "ACT-[CATEGORY]-[NUMBER]",
  "action": "ActionVerb",
  "action_type": "Communication | Creation | Analysis | Management | Processing | Verification | Storage | General",
  "description": "Clear description of what this action does",
  "common_objects": ["Object1", "Object2"],
  "tool_requirements": ["Tool1", "Tool2"],
  "examples": ["Example usage 1", "Example usage 2"],
  "related_processes": ["process1", "process2"],
  "related_results": ["result1", "result2"],
  "department_mapping": ["Department1", "Department2"],
  "profession_mapping": ["Profession1", "Profession2"],
  "tags": ["tag1", "tag2"],
  "version": "1.0",
  "created": "YYYY-MM-DD",
  "last_updated": "YYYY-MM-DD",
  "source": "Video_XXX | Manual | Import"
}
```

### Objects Schema
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Objects",
  "object_id": "OBJ-[CATEGORY]-[NUMBER]",
  "name": "ObjectName",
  "category": "Document | Communication | Data | Media | System | Process",
  "description": "Clear description of what this object is",
  "attributes": ["attribute1", "attribute2"],
  "common_actions": ["Action1", "Action2"],
  "storage_location": "Path pattern or location",
  "file_format": "JSON | Markdown | PDF | etc.",
  "related_entities": ["Entity1", "Entity2"],
  "related_tools": ["TOOL-ID-1", "TOOL-ID-2"],
  "related_workflows": ["WF-ID-1", "WF-ID-2"],
  "department_mapping": ["Department1"],
  "profession_mapping": ["Profession1"],
  "tags": ["tag1", "tag2"],
  "version": "1.0",
  "created": "YYYY-MM-DD",
  "last_updated": "YYYY-MM-DD",
  "source": "Video_XXX | Manual | Import"
}
```

### Tools Schema
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Tool",
  "tool_id": "TOOL-[CATEGORY]-[NUMBER]",
  "tool_name": "ToolName",
  "vendor": "VendorName",
  "category": "AI_Tools | Development | Design | Marketing | Automation | Infrastructure | Database",
  "description": "Clear description of tool purpose",
  "primary_use": "Main use case",
  "platform_type": "Web | Desktop | API | CLI | Mobile",
  "pricing": "Free | Paid | Usage-based | Subscription",
  "skill_level_required": "Novice | Intermediate | Advanced | Expert",
  "platform_compatibility": ["Platform1", "Platform2"],
  "integration_capabilities": ["Integration1", "Integration2"],
  "documentation_url": "https://docs.example.com",
  "actions": ["action1", "action2"],
  "creates_objects": ["OBJ-ID-1", "OBJ-ID-2"],
  "used_by_professions": ["Profession1", "Profession2"],
  "used_in_workflows": ["WF-ID-1", "WF-ID-2"],
  "key_features": {
    "feature1": "Description",
    "feature2": "Description"
  },
  "tags": ["tag1", "tag2"],
  "version": "1.0",
  "created": "YYYY-MM-DD",
  "last_updated": "YYYY-MM-DD",
  "source": "Video_XXX | Manual | Import"
}
```

### Processes Schema
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Processes",
  "process_id": "PROC-[CATEGORY]-[NUMBER]",
  "process_name": "processname",
  "category": "Communication | Creation | Analysis | Management | Processing | Verification | Storage | General",
  "description": "Description of ongoing action",
  "related_actions": ["Action1", "Action2"],
  "related_results": ["Result1", "Result2"],
  "common_departments": ["Department1", "Department2"],
  "common_professions": ["Profession1", "Profession2"],
  "usage_count": 0,
  "tags": ["tag1", "tag2"],
  "version": "1.0",
  "created": "YYYY-MM-DD",
  "last_updated": "YYYY-MM-DD",
  "source": "Video_XXX | Manual | Import"
}
```

### Results Schema
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Results",
  "result_id": "RES-[CATEGORY]-[NUMBER]",
  "result_name": "resultname",
  "category": "Communication | Creation | Analysis | Management | Processing | Verification | Storage | General",
  "description": "Description of completed state",
  "related_actions": ["Action1", "Action2"],
  "related_processes": ["Process1", "Process2"],
  "common_departments": ["Department1"],
  "common_professions": ["Profession1"],
  "usage_count": 0,
  "tags": ["tag1", "tag2"],
  "version": "1.0",
  "created": "YYYY-MM-DD",
  "last_updated": "YYYY-MM-DD",
  "source": "Video_XXX | Manual | Import"
}
```

### Skills Schema
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Skills",
  "skill_id": "SKL-[NUMBER]",
  "skill_phrase": "responsibility + tool",
  "responsibility": "action + object phrase",
  "tool": "ToolName",
  "result": "completed action (past participle)",
  "department": "Department",
  "professions": ["Profession1", "Profession2"],
  "difficulty_level": "beginner | intermediate | advanced | expert",
  "frequency_of_use": "daily | weekly | monthly | occasional",
  "time_estimate": "X minutes/hours",
  "automation_potential": "high | medium | low",
  "related_skills": ["SKL-XXX", "SKL-YYY"],
  "example_tasks": ["Task1", "Task2"],
  "training_resources": ["Resource1", "Resource2"],
  "tags": ["tag1", "tag2"],
  "version": "1.0",
  "created": "YYYY-MM-DD",
  "last_updated": "YYYY-MM-DD",
  "source": "Video_XXX | Manual | Import"
}
```

### Professions Schema
```json
{
  "entity_type": "LIBRARIES",
  "sub_entity": "Profession",
  "profession_id": "PROF-[NUMBER]",
  "title": "ProfessionTitle",
  "department": "Department",
  "description": "Role description",
  "skill_requirements": {
    "technical": ["Skill1", "Skill2"],
    "soft_skills": ["Skill1", "Skill2"]
  },
  "tool_proficiency": {
    "required": ["Tool1", "Tool2"],
    "optional": ["Tool3", "Tool4"]
  },
  "typical_responsibilities": ["Responsibility1", "Responsibility2"],
  "career_progression": {
    "junior": "Description",
    "mid": "Description",
    "senior": "Description",
    "expert": "Description"
  },
  "related_processes": ["Process1", "Process2"],
  "related_skills": ["SKL-XXX", "SKL-YYY"],
  "tags": ["tag1", "tag2"],
  "version": "1.0",
  "created": "YYYY-MM-DD",
  "last_updated": "YYYY-MM-DD",
  "source": "Video_XXX | Manual | Import"
}
```

---

## Prompt Integration Standards

### Prompt Output Format
All prompts that extract LIBRARIES data MUST output in the following structure:

```json
{
  "extraction_metadata": {
    "source": "Video_XXX | Document_XXX | Manual",
    "extraction_date": "YYYY-MM-DD",
    "prompt_version": "vX.X",
    "extractor": "AI Assistant Name"
  },
  "entities": {
    "actions": [
      {
        "action": "ActionVerb",
        "action_type": "Category",
        "description": "Description",
        "common_objects": ["Object1"],
        "tool_requirements": ["Tool1"],
        "examples": ["Example"],
        "source_context": "Where this was found"
      }
    ],
    "objects": [
      {
        "name": "ObjectName",
        "category": "Category",
        "description": "Description",
        "attributes": ["attr1"],
        "common_actions": ["Action1"],
        "source_context": "Where this was found"
      }
    ],
    "tools": [
      {
        "tool_name": "ToolName",
        "vendor": "Vendor",
        "category": "Category",
        "description": "Description",
        "primary_use": "Use case",
        "pricing": "Pricing info",
        "source_context": "Where this was found"
      }
    ],
    "processes": [
      {
        "process_name": "processname",
        "category": "Category",
        "description": "Description",
        "related_actions": ["Action1"],
        "source_context": "Where this was found"
      }
    ],
    "results": [
      {
        "result_name": "resultname",
        "category": "Category",
        "description": "Description",
        "related_actions": ["Action1"],
        "source_context": "Where this was found"
      }
    ],
    "skills": [
      {
        "skill_phrase": "responsibility + tool",
        "responsibility": "action + object",
        "tool": "ToolName",
        "department": "Department",
        "difficulty_level": "level",
        "source_context": "Where this was found"
      }
    ],
    "professions": [
      {
        "title": "ProfessionTitle",
        "department": "Department",
        "description": "Description",
        "typical_responsibilities": ["Resp1"],
        "source_context": "Where this was found"
      }
    ]
  },
  "cross_references": {
    "action_object_pairs": [
      {
        "action": "Action1",
        "object": "Object1",
        "context": "Usage context"
      }
    ],
    "tool_object_pairs": [
      {
        "tool": "Tool1",
        "object": "Object1",
        "context": "Usage context"
      }
    ],
    "workflow_components": [
      {
        "workflow_name": "WorkflowName",
        "actions": ["Action1"],
        "tools": ["Tool1"],
        "objects": ["Object1"],
        "steps": ["Step1", "Step2"]
      }
    ]
  }
}
```

---

## Data Consistency Rules

### 1. Naming Conventions
- **Actions:** PascalCase verbs (Create, Analyze, Send)
- **Objects:** PascalCase nouns (JobPosting, Email, Report)
- **Tools:** Tool name as provided by vendor (Claude, GitHub, Figma)
- **Processes:** Lowercase gerund form (creating, analyzing, sending)
- **Results:** Lowercase past participle (created, analyzed, sent)
- **Skills:** Natural language phrase (send cold emails via Gmail)
- **Professions:** Standardized titles (Frontend Developer, Lead Generator)

### 2. ID Generation
- **Format:** `[TYPE]-[CATEGORY]-[NUMBER]`
- **Actions:** `ACT-CREA-001`, `ACT-COMM-001`
- **Objects:** `OBJ-DOC-001`, `OBJ-COMM-001`
- **Tools:** `TOOL-AI-001`, `TOOL-DEV-001`
- **Processes:** `PROC-CREA-001`
- **Results:** `RES-CREA-001`
- **Skills:** `SKL-001` (sequential)
- **Professions:** `PROF-001` (sequential)

### 3. Category Standards
- **Action Types:** Communication, Creation, Analysis, Management, Processing, Verification, Storage, General
- **Object Categories:** Document, Communication, Data, Media, System, Process
- **Tool Categories:** AI_Tools, Development, Design, Marketing, Automation, Infrastructure, Database
- **Process/Result Categories:** Same as Action Types

### 4. Cross-Reference Requirements
- **Actions ↔ Objects:** Every action should list common objects
- **Actions ↔ Tools:** Every action should list tool requirements
- **Objects ↔ Tools:** Objects created by tools should reference tools
- **Tools ↔ Workflows:** Tools used in workflows should reference workflows
- **Skills ↔ Responsibilities:** Skills should map to profession responsibilities
- **Professions ↔ Skills:** Professions should list required skills

---

## Machine Access Patterns

### 1. Direct File Access
```
LIBRARIES/
├── Actions/
│   ├── Actions_Master.json          # All actions
│   └── [Category]/                   # Category-specific
├── Objects/
│   ├── objects.json                  # Master objects
│   └── [Category]_Objects.json       # Category-specific
├── Tools/
│   ├── tools.json                    # Master tools index
│   └── [Category]/                   # Category-specific folders
└── [Other entities]/
```

### 2. Index Files for Quick Lookup
```json
{
  "index_type": "LIBRARIES_INDEX",
  "version": "1.0",
  "last_updated": "YYYY-MM-DD",
  "entities": {
    "actions": {
      "total": 429,
      "by_category": {
        "Creation": 120,
        "Communication": 85,
        "Analysis": 75
      },
      "master_file": "Actions/Actions_Master.json"
    },
    "objects": {
      "total": 152,
      "by_category": {
        "Document": 45,
        "Communication": 30,
        "Media": 25
      },
      "master_file": "Objects/objects.json"
    },
    "tools": {
      "total": 150,
      "by_category": {
        "AI_Tools": 29,
        "Development": 35,
        "Design": 20
      },
      "master_file": "Tools/tools.json"
    }
  },
  "cross_references": {
    "action_object_pairs": 850,
    "tool_object_pairs": 320,
    "workflow_tool_pairs": 180
  }
}
```

### 3. Query Patterns
```json
{
  "query_type": "find_action_by_object",
  "object": "JobPosting",
  "results": [
    {
      "action_id": "ACT-CREA-001",
      "action": "Create",
      "action_type": "Creation"
    },
    {
      "action_id": "ACT-MGMT-045",
      "action": "Update",
      "action_type": "Management"
    }
  ]
}
```

---

## Prompt-to-Knowledge Pipeline

### Phase 1: Extraction (Prompts)
**Input:** Raw source (video, document, conversation)
**Process:** Use specialized prompts to extract structured data
**Output:** JSON following extraction format

**Prompts Used:**
- `Video_Transcription_Custom_Instructions.md` - Extract from videos
- `Video_Analysis_Prompt.md` - Analyze and structure
- `Objects_Library_Extraction_Prompt.md` - Extract objects
- `Taxonomy_Analysis_and_Updates_Prompt.md` - Complete integration

### Phase 2: Validation
**Input:** Extracted JSON
**Process:** Validate against LIBRARIES schemas
**Checks:**
- Required fields present
- Data types correct
- Naming conventions followed
- IDs properly formatted
- Categories valid
- Cross-references resolvable

**Validation Script:**
```python
def validate_entity(entity, schema):
    """Validate entity against schema"""
    checks = [
        check_required_fields(entity, schema),
        check_data_types(entity, schema),
        check_naming_conventions(entity),
        check_id_format(entity),
        check_categories(entity, schema),
        check_cross_references(entity)
    ]
    return all(checks)
```

### Phase 3: Transformation
**Input:** Validated extracted data
**Process:** Transform to match LIBRARIES structure
**Steps:**
1. Generate IDs (check for duplicates)
2. Normalize names (apply naming conventions)
3. Map categories (standardize category names)
4. Resolve cross-references (link to existing entities)
5. Add metadata (source, dates, version)

### Phase 4: Population
**Input:** Transformed, validated data
**Process:** Add to LIBRARIES entities
**Steps:**
1. Check for duplicates (by name, not ID)
2. Merge if exists (update with new information)
3. Create if new (add to appropriate file)
4. Update master files
5. Update index files
6. Create cross-references

### Phase 5: Cross-Reference Update
**Input:** New/updated entities
**Process:** Update all related entities
**Steps:**
1. Update action-object relationships
2. Update tool-object relationships
3. Update workflow-tool relationships
4. Update profession-skill relationships
5. Update skill-responsibility relationships
6. Verify bidirectional references

---

## Integration Workflow

### Complete Flow Diagram
```
[Source Material]
    ↓
[Prompt Extraction]
    ↓
[Structured JSON Output]
    ↓
[Schema Validation]
    ↓
[Data Transformation]
    ↓
[Duplicate Check]
    ↓
[LIBRARIES Population]
    ↓
[Cross-Reference Update]
    ↓
[Index Update]
    ↓
[Knowledge Base Ready]
```

### Example: Video Processing
```
Video_006 (Lead Generation Tutorial)
    ↓
Video_Transcription_Custom_Instructions.md
    ↓
Extract: 18 tools, 10 objects, 12 actions, 14 workflows
    ↓
Validate against schemas
    ↓
Transform: Generate IDs, normalize names
    ↓
Check duplicates: 0 duplicates found
    ↓
Populate LIBRARIES:
    - Add 18 tools to Tools/
    - Add 10 objects to Objects/
    - Add 12 actions to Actions/
    - Create 14 workflows in Processes/Workflows/
    ↓
Update cross-references:
    - Link tools to workflows
    - Link objects to tools
    - Link actions to objects
    ↓
Update indexes:
    - Update Tools index
    - Update Objects index
    - Update Actions index
    ↓
Knowledge base updated ✅
```

---

## Consistency Maintenance

### 1. Automated Validation
**Script:** `validate_libraries_consistency.py`
**Checks:**
- All IDs unique
- All cross-references valid
- All categories standard
- All naming conventions followed
- All required fields present
- No orphaned references

### 2. Regular Audits
**Frequency:** Weekly
**Process:**
1. Run validation script
2. Check for duplicates
3. Verify cross-references
4. Update documentation
5. Fix inconsistencies

### 3. Version Control
**Approach:**
- Track all changes
- Maintain change logs
- Version entity files
- Document breaking changes

### 4. Conflict Resolution
**When duplicates found:**
1. Compare source contexts
2. Merge information (prefer more detailed)
3. Update both references
4. Document merge decision

**When cross-reference broken:**
1. Identify missing entity
2. Check if renamed/moved
3. Update reference or mark as deprecated
4. Document resolution

---

## Machine Access API Patterns

### 1. Get Entity by ID
```json
GET /libraries/actions/ACT-CREA-001
Response: {
  "entity_type": "LIBRARIES",
  "sub_entity": "Actions",
  "action_id": "ACT-CREA-001",
  ...
}
```

### 2. Search Entities
```json
POST /libraries/search
Body: {
  "entity_type": "tools",
  "filters": {
    "category": "AI_Tools",
    "pricing": "Free"
  }
}
Response: {
  "results": [...],
  "total": 15
}
```

### 3. Get Related Entities
```json
GET /libraries/actions/ACT-CREA-001/related
Response: {
  "common_objects": [...],
  "tool_requirements": [...],
  "related_processes": [...],
  "related_results": [...]
}
```

### 4. Cross-Reference Query
```json
POST /libraries/cross-reference
Body: {
  "action": "Create",
  "object": "JobPosting"
}
Response: {
  "exists": true,
  "usage_count": 15,
  "examples": [...]
}
```

---

## Prompt Enhancement Instructions

### For All Extraction Prompts
Add these sections:

#### 1. Schema Reference Section
```markdown
## LIBRARIES Schema Reference

This prompt outputs data in LIBRARIES-compatible format. Reference schemas:
- Actions: `Entities/LIBRARIES/Actions/Actions_Master.json`
- Objects: `Entities/LIBRARIES/Objects/objects.json`
- Tools: `Entities/LIBRARIES/Tools/tools.json`
- [Other entities...]

**Required:** All outputs MUST conform to these schemas.
```

#### 2. Output Format Section
```markdown
## Required Output Format

Output MUST be valid JSON following this structure:
[Include extraction format template]

**Validation:** Output will be validated against LIBRARIES schemas before population.
```

#### 3. Naming Conventions Section
```markdown
## Naming Conventions

- **Actions:** PascalCase verbs (Create, Analyze, Send)
- **Objects:** PascalCase nouns (JobPosting, Email)
- **Tools:** Vendor name (Claude, GitHub)
- **Processes:** Lowercase gerund (creating, analyzing)
- **Results:** Lowercase past participle (created, analyzed)

**Required:** Follow these conventions exactly.
```

#### 4. Cross-Reference Instructions
```markdown
## Cross-Reference Requirements

When extracting entities, also extract:
- Action-Object pairs (which actions work with which objects)
- Tool-Object pairs (which tools create which objects)
- Workflow components (actions, tools, objects used together)

**Required:** Include cross_references section in output.
```

---

## Implementation Checklist

### For Prompts
- [ ] Add schema reference section
- [ ] Add output format template
- [ ] Add naming conventions guide
- [ ] Add cross-reference instructions
- [ ] Test output against validation script
- [ ] Document example outputs

### For LIBRARIES Structure
- [ ] Ensure all schemas documented
- [ ] Create validation scripts
- [ ] Create transformation scripts
- [ ] Create population scripts
- [ ] Create index update scripts
- [ ] Create cross-reference update scripts

### For Data Consistency
- [ ] Implement validation checks
- [ ] Create audit scripts
- [ ] Set up version control
- [ ] Document conflict resolution
- [ ] Create consistency reports

### For Machine Access
- [ ] Create index files
- [ ] Document query patterns
- [ ] Create API documentation
- [ ] Test machine readability
- [ ] Optimize for search

---

## Success Metrics

### Data Quality
- ✅ 100% schema compliance
- ✅ 0 duplicate entities (by name)
- ✅ 100% valid cross-references
- ✅ Consistent naming throughout

### Machine Accessibility
- ✅ All entities in JSON format
- ✅ Index files updated
- ✅ Query patterns documented
- ✅ API-ready structure

### Integration Efficiency
- ✅ Prompts output valid JSON
- ✅ Automated validation passes
- ✅ Population succeeds without errors
- ✅ Cross-references automatically created

---

## Example: Complete Integration

### Input: Video Transcript
```
"In this tutorial, we'll use Claude Desktop to create custom MCP connectors..."
```

### Prompt Processing
Using `Video_Transcription_Custom_Instructions.md`:
- Extract: Tool "Claude Desktop", Action "Create", Object "MCP Connector"

### Output: Structured JSON
```json
{
  "extraction_metadata": {
    "source": "Video_008",
    "extraction_date": "2025-11-13",
    "prompt_version": "v3.1"
  },
  "entities": {
    "tools": [{
      "tool_name": "Claude Desktop",
      "vendor": "Anthropic",
      "category": "AI_Tools",
      "description": "Desktop application for Claude AI with MCP connector support",
      "primary_use": "Local AI access with custom integrations",
      "pricing": "Free",
      "source_context": "Video_008 - MCP Connector Tutorial"
    }],
    "actions": [{
      "action": "Create",
      "action_type": "Creation",
      "description": "Build or generate new item",
      "common_objects": ["MCP Connector"],
      "source_context": "Video_008"
    }],
    "objects": [{
      "name": "MCP Connector",
      "category": "System",
      "description": "Custom connector for Model Context Protocol",
      "common_actions": ["Create", "Configure", "Deploy"],
      "source_context": "Video_008"
    }]
  },
  "cross_references": {
    "action_object_pairs": [{
      "action": "Create",
      "object": "MCP Connector",
      "context": "Creating custom connectors for Claude Desktop"
    }],
    "tool_object_pairs": [{
      "tool": "Claude Desktop",
      "object": "MCP Connector",
      "context": "Claude Desktop uses MCP connectors for integrations"
    }]
  }
}
```

### Validation
- ✅ Schema compliance: PASS
- ✅ Naming conventions: PASS
- ✅ Required fields: PASS
- ✅ ID format: PASS

### Transformation
- Generate IDs: `TOOL-AI-080`, `ACT-CREA-001`, `OBJ-SYS-015`
- Normalize names: Already correct
- Map categories: Already correct
- Resolve cross-references: Link to existing entities

### Population
- Add tool to `Tools/AI_Tools/Claude_Desktop.json`
- Update `Tools/tools.json` index
- Add action to `Actions/Actions_Master.json` (if new)
- Add object to `Objects/objects.json` (if new)
- Create cross-references in all related files

### Result
✅ Knowledge base updated with new information
✅ Cross-references maintained
✅ Indexes updated
✅ Machine-readable format preserved

---

## Maintenance Schedule

### Daily
- Run validation script on new additions
- Check for duplicate entries
- Verify cross-references

### Weekly
- Full consistency audit
- Update indexes
- Review naming conventions
- Check for orphaned references

### Monthly
- Schema review and updates
- Documentation updates
- Performance optimization
- User feedback integration

---

**Created:** 2025-11-13
**Purpose:** Establish data consistency and machine access for LIBRARIES
**Status:** Ready for Implementation
**Version:** 1.0

---

*This system ensures prompts extract data that seamlessly integrates with the LIBRARIES knowledge base, maintaining consistency and enabling machine access.*

