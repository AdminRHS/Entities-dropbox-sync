# PROMPT: Chat Instruction Extraction for Taxonomy Integration

**ID:** PRM-006  
**Type:** Instruction Extraction Prompt  
**Category:** Taxonomy Integration  
**Department:** AID  
**Status:** Active  
**Version:** 1.0  
**Created:** 2025-12-08  

---

## PURPOSE

Extract structured, actionable instructions from chat conversations and format them according to the TAX-002 Task Managers taxonomy system for integration into the task management ecosystem.

---

## CONTEXT & SYSTEM OVERVIEW

### Taxonomy Entity Types (ISO Codes)
- **PRT** - Project Template (meta-level project workflows)
- **MLT** - Milestone Template (project phases/checkpoints)
- **TST** - Task Template (specific actionable tasks)
- **STT** - Step Template (granular execution steps)
- **CHT** - Checklist Template (verification items)
- **WRF** - Workflow (multi-step process definitions)
- **GDS** - Guide (documentation/instructions)
- **PRM** - Prompt (AI instruction templates)
- **RSR** - Research (investigation/analysis entities)

### Department Codes
- **AID** - AI Department (Automations, Operations, Administration)
- **HRM** - Human Resource Management
- **DEV** - Development & Engineering
- **LGN** - Lead Generation & Marketing
- **DGN** - Design & Creative
- **VID** - Video Production
- **SLS** - Sales & Client Relations

### Naming Convention
- Format: `[ISO-CODE]-###_[Descriptive_Name]`
- Example: `TST-072_Create_Instruction_Extraction_Prompt`
- Use underscores, no spaces
- Descriptive names should be clear and specific

---

## EXTRACTION INSTRUCTIONS

### Step 1: Analyze Conversation Context

**Identify:**
1. **Primary Intent** - What is the user trying to accomplish?
2. **Scope** - Is this a project, task, step, or workflow?
3. **Department** - Which department should own this?
4. **Dependencies** - What must exist before this can execute?
5. **Deliverables** - What outputs are expected?

**Context Clues:**
- "Create a system for..." → PRT (Project Template)
- "Build a workflow that..." → WRF (Workflow)
- "Write instructions for..." → GDS (Guide) or PRM (Prompt)
- "Research..." → RSR (Research)
- "Do this task..." → TST (Task Template)
- "Step 1, Step 2..." → STT (Step Template)
- "Check that..." → CHT (Checklist Template)
- "When X is complete..." → MLT (Milestone Template)

### Step 2: Extract Structured Elements

For each instruction found, extract:

#### Required Fields
```json
{
  "entity_type": "[PRT|MLT|TST|STT|CHT|WRF|GDS|PRM|RSR]",
  "name": "[Descriptive_Name]",
  "description": "[Clear description of purpose and scope]",
  "department": "[AID|HRM|DEV|LGN|DGN|VID|SLS]",
  "priority": "[CRITICAL|HIGH|MEDIUM|LOW]",
  "status": "[Active|Deprecated|Pending]"
}
```

#### Optional Fields
```json
{
  "dependencies": ["[Entity-ID-1]", "[Entity-ID-2]"],
  "deliverables": ["[Output-1]", "[Output-2]"],
  "estimated_duration": "[Time estimate]",
  "risk_level": "[LOW|MEDIUM|HIGH]",
  "tags": ["[tag1]", "[tag2]"],
  "related_entities": ["[Entity-ID-1]", "[Entity-ID-2]"]
}
```

### Step 3: Identify Actionable Components

**Break down complex instructions into:**
1. **Main Entity** - The primary instruction (PRT, TST, WRF, etc.)
2. **Sub-Entities** - Nested instructions (STT, CHT)
3. **Relationships** - Dependencies and connections
4. **Execution Order** - Sequence if multiple steps

**Pattern Recognition:**
- Sequential steps → STT entities with order numbers
- Verification points → CHT entities
- Decision points → Extract as separate decision entities
- Reusable processes → WRF entities
- One-time actions → TST entities

### Step 4: Format for Integration

#### Output Format: JSON Structure

```json
{
  "extraction_metadata": {
    "source": "chat_conversation",
    "extracted_date": "YYYY-MM-DD",
    "extractor_version": "1.0",
    "conversation_context": "[Brief summary]"
  },
  "entities": [
    {
      "id": "[ISO-CODE]-###",
      "type": "[Entity Type]",
      "name": "[Name]",
      "description": "[Description]",
      "department": "[Department Code]",
      "priority": "[Priority]",
      "status": "[Status]",
      "dependencies": [],
      "deliverables": [],
      "execution_steps": [],
      "checklist_items": [],
      "related_entities": []
    }
  ],
  "relationships": [
    {
      "from": "[Entity-ID-1]",
      "to": "[Entity-ID-2]",
      "type": "[depends_on|part_of|related_to]"
    }
  ],
  "validation": {
    "all_required_fields_present": true,
    "naming_convention_valid": true,
    "department_code_valid": true,
    "iso_code_valid": true
  }
}
```

---

## EXTRACTION RULES

### Rule 1: Entity Type Classification

**Project Template (PRT)** - When conversation describes:
- Complete end-to-end workflows
- Multi-phase initiatives
- Systems requiring multiple milestones
- Complex processes spanning departments

**Task Template (TST)** - When conversation describes:
- Single, specific actionable items
- Discrete operations
- One-time or repeatable tasks
- Clear input/output operations

**Step Template (STT)** - When conversation describes:
- Granular execution steps
- Sub-tasks within a larger task
- Sequential operations
- Detailed procedures

**Workflow (WRF)** - When conversation describes:
- Multi-step processes with branching
- Conditional logic flows
- Reusable process definitions
- Cross-entity coordination

**Guide (GDS)** - When conversation describes:
- Documentation needs
- How-to instructions
- Reference materials
- Best practices

**Prompt (PRM)** - When conversation describes:
- AI instruction templates
- System prompts
- Agent instructions
- Automated prompt generation

**Research (RSR)** - When conversation describes:
- Investigation activities
- Analysis requirements
- Information gathering
- Knowledge discovery

**Milestone Template (MLT)** - When conversation describes:
- Project checkpoints
- Phase completions
- Validation points
- Progress markers

**Checklist Template (CHT)** - When conversation describes:
- Verification items
- Quality checks
- Validation criteria
- Completion requirements

### Rule 2: Department Assignment

**AID (AI Department)** - Default for:
- Automation tasks
- System infrastructure
- AI/ML operations
- General operations
- Administrative tasks

**HRM** - Assign when:
- Human resources mentioned
- Recruitment/onboarding
- Employee management
- CV screening/interviews

**DEV** - Assign when:
- Software development
- Code/script creation
- Technical implementation
- Development tools

**LGN** - Assign when:
- Lead generation
- Marketing campaigns
- Email enrichment
- Sales prospecting

**DGN** - Assign when:
- Design work
- Creative projects
- Visual content
- Portfolio management

**VID** - Assign when:
- Video production
- Content creation
- Video processing
- Media management

**SLS** - Assign when:
- Sales activities
- Client relations
- Customer engagement
- Revenue generation

### Rule 3: Naming Convention Enforcement

**Format:** `[ISO-CODE]-###_[Descriptive_Name]`

**Rules:**
- Use next available number in sequence
- Name must be descriptive and specific
- Use Title_Case_With_Underscores
- No spaces, special characters (except underscores)
- Keep names concise but clear (max 60 chars)

**Examples:**
- ✅ `TST-072_Create_Instruction_Extraction_Prompt`
- ✅ `PRT-010_Chat_Processing_Pipeline`
- ❌ `TST-072 create prompt` (spaces)
- ❌ `TST-072_Create` (too vague)
- ❌ `TST-072_Create_A_Comprehensive_And_Detailed_Instruction_Extraction_Prompt_For_AI_Agents` (too long)

### Rule 4: Dependency Detection

**Identify dependencies when conversation mentions:**
- "After X is complete..."
- "Requires Y to exist..."
- "Depends on Z..."
- "First, we need..."
- "Prerequisite: ..."

**Format dependencies as:**
- Entity IDs: `["PRT-001", "TST-045"]`
- Or descriptions if IDs unknown: `["Complete Project Setup", "Research Phase"]`

### Rule 5: Deliverable Extraction

**Identify deliverables when conversation mentions:**
- "Create a file..."
- "Generate a report..."
- "Output should be..."
- "Deliverable: ..."
- "Result: ..."

**Format deliverables as:**
- File paths: `["ENTITIES/PROMPTS/Extraction_Prompt.md"]`
- Output types: `["JSON schema", "Markdown documentation"]`
- Artifacts: `["Task list", "Checklist items"]`

---

## OUTPUT VALIDATION

### Required Checks

1. **All Required Fields Present**
   - Entity type, name, description, department, priority, status

2. **Naming Convention Valid**
   - Matches `[ISO-CODE]-###_[Name]` pattern
   - No spaces or invalid characters
   - Descriptive and specific

3. **Department Code Valid**
   - One of: AID, HRM, DEV, LGN, DGN, VID, SLS

4. **ISO Code Valid**
   - One of: PRT, MLT, TST, STT, CHT, WRF, GDS, PRM, RSR

5. **Priority Level Valid**
   - One of: CRITICAL, HIGH, MEDIUM, LOW

6. **Status Valid**
   - One of: Active, Deprecated, Pending

7. **ID Uniqueness**
   - Check against existing taxonomy master list
   - Use next available number

### Validation Output

```json
{
  "validation": {
    "all_required_fields_present": true,
    "naming_convention_valid": true,
    "department_code_valid": true,
    "iso_code_valid": true,
    "priority_level_valid": true,
    "status_valid": true,
    "id_uniqueness_verified": true,
    "validation_passed": true,
    "warnings": [],
    "errors": []
  }
}
```

---

## INTEGRATION WORKFLOW

### Step 1: Extract
Run this prompt on chat conversation to extract structured instructions.

### Step 2: Validate
Check all validation rules pass.

### Step 3: Assign IDs
Query taxonomy master list to get next available ID numbers.

### Step 4: Create Files
Generate entity files in appropriate taxonomy directories:
- `ENTITIES/TASK_MANAGERS/TSM-001_Project_Templates/` for PRT
- `ENTITIES/TASK_MANAGERS/TSM-003_Task_Templates/` for TST
- `ENTITIES/TASK_MANAGERS/TSM-006_Workflows/` for WRF
- etc.

### Step 5: Update Master List
Add new entities to `Taxonomy_Master_List.csv`

### Step 6: Update Relationships
Add dependency relationships to migration map if needed.

---

## EXAMPLE EXTRACTION

### Input Conversation:
```
User: "I need a prompt for AI to extract structured instructions from chat conversations. 
It should format them according to our taxonomy system and integrate into the task manager."

AI: "I'll create a comprehensive extraction prompt that identifies entity types, 
assigns departments, and formats output for integration."
```

### Extracted Output:
```json
{
  "extraction_metadata": {
    "source": "chat_conversation",
    "extracted_date": "2025-12-08",
    "extractor_version": "1.0",
    "conversation_context": "User requested prompt creation for instruction extraction"
  },
  "entities": [
    {
      "id": "PRM-006",
      "type": "PRM",
      "name": "Chat_Instruction_Extraction",
      "description": "Extract structured, actionable instructions from chat conversations and format them according to TAX-002 Task Managers taxonomy system for integration into task management ecosystem",
      "department": "AID",
      "priority": "HIGH",
      "status": "Active",
      "dependencies": [],
      "deliverables": [
        "ENTITIES/TAXONOMY/TAX-002_Task_Managers/PROMPT_Chat_Instruction_Extraction.md",
        "JSON extraction output"
      ],
      "execution_steps": [
        "Analyze conversation context",
        "Extract structured elements",
        "Identify actionable components",
        "Format for integration",
        "Validate output"
      ],
      "checklist_items": [
        "All required fields present",
        "Naming convention valid",
        "Department code valid",
        "ISO code valid"
      ],
      "related_entities": ["TAX-002"]
    }
  ],
  "relationships": [],
  "validation": {
    "all_required_fields_present": true,
    "naming_convention_valid": true,
    "department_code_valid": true,
    "iso_code_valid": true,
    "priority_level_valid": true,
    "status_valid": true,
    "id_uniqueness_verified": true,
    "validation_passed": true,
    "warnings": [],
    "errors": []
  }
}
```

---

## USAGE INSTRUCTIONS FOR AI AGENTS

### When to Use This Prompt

Use this prompt when:
1. User provides instructions in chat conversation
2. Need to convert informal requests into structured entities
3. Processing historical chat logs for instruction extraction
4. Integrating external instructions into taxonomy system
5. Creating reusable templates from one-off conversations

### How to Execute

1. **Provide Context:**
   - Include the full chat conversation
   - Provide relevant taxonomy context (current entity counts)
   - Include department assignments if unclear

2. **Run Extraction:**
   - Apply all extraction rules
   - Classify entity types accurately
   - Assign appropriate departments
   - Extract all dependencies and deliverables

3. **Validate Output:**
   - Run all validation checks
   - Verify ID uniqueness
   - Check naming conventions
   - Confirm all required fields

4. **Generate Integration Files:**
   - Create entity JSON files
   - Update master list CSV
   - Create relationship mappings
   - Generate documentation

### Output Format

Always output in the JSON structure defined above, ready for:
- Direct integration into taxonomy system
- File generation automation
- Master list updates
- Relationship mapping

---

## MAINTENANCE

**Update Frequency:** When new entity types or department codes are added  
**Review Cycle:** Quarterly  
**Version History:**
- v1.0 (2025-12-08) - Initial creation

---

## RELATED ENTITIES

- **TAX-002** - Task Managers Taxonomy (parent taxonomy)
- **SYS.03** - Taxonomy system documentation
- **SYS.05** - Naming conventions
- **AI_OUTPUT_SCHEMA** - Decision making schema

---

**END PROMPT**

