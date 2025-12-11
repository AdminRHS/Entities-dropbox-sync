# Libraries Quick Start Guide

**Created:** 2025-12-11
**Purpose:** Guide to when and how to use each library in the ENTITIES/LIBRARIES ecosystem

---

## Library Ecosystem Overview

```csv
LIBRARY,PATH,SIZE,PRIMARY_USE,WHEN_TO_USE
Responsibilities,LIBRARIES/Responsibilities/,193 items,RESP-ID assignment,Every task/action creation
Actions,Responsibilities/Variants/action_variants.csv,57 variants,Action normalization,Processing verbs
Objects,Responsibilities/Variants/object_variants.csv,169 variants,Object normalization,Processing nouns
Templates,TASK_MANAGERS/TSM-004_Step_Templates/,155+ files,Step reuse,Before creating custom steps
Parameters,TASK_MANAGERS/TSM-003_Parameters/,7321 mappings,Output enrichment,Adding metadata/quality params
Tools,Responsibilities/Metadata/tools_by_dept.csv,Tool catalog,Tool selection,Choosing software/platforms
Professions,Responsibilities/Metadata/professions.csv,Role definitions,Role assignment,Assigning work by skill
```

---

## When to Use Which Library

### Decision Tree

```
START: Need to process a task/action
│
├─ Do you need to assign RESP-ID?
│  YES → Use Responsibilities Library
│  │
│  └─ Is action/object in standard form?
│     NO → Use Action/Object Variants to normalize first
│     YES → Continue to phrase matching
│
├─ Do you need to create task steps?
│  YES → Use Templates Library (TSM-004)
│  │
│  └─ Found template with ≥80% match?
│     YES → Inherit and customize
│     NO → Check similar patterns, then create custom
│
├─ Do you need to enrich output with parameters?
│  YES → Use Parameters Library (TSM-003)
│  │
│  └─ Load quality_parameters.csv and state_parameters.csv
│     Filter by action/object
│
├─ Do you need to assign tools?
│  YES → Use Tools Library
│  │
│  └─ Filter by department
│     Select appropriate tools
│
└─ Do you need to assign by role/skill?
   YES → Use Professions Library
   │
   └─ Match required skills
      Assign appropriate role
```

---

## Library 1: Responsibilities

**Path:** `ENTITIES/LIBRARIES/Responsibilities/`
**Size:** 193 responsibilities, 209 phrase patterns
**Purpose:** Assign RESP-ID to every task/action

### When to Use
- Creating any new task or action
- Processing whisper transcripts
- Extracting action items from meetings
- Validating task assignments
- Department routing

### Quick Start

**Step 1: Load phrase matching index**
```python
import json

with open('ENTITIES/LIBRARIES/Responsibilities/Core/phrase_matching_index.json', 'r') as f:
    phrase_index = json.load(f)

# Structure:
# {
#   "create+api_endpoint": {
#     "responsibility_id": "RESP-DEV-015",
#     "department": "Development",
#     "confidence": 100
#   }
# }
```

**Step 2: Build search key**
```python
action = "create"  # from user input or transcript
object = "api endpoint"  # from user input or transcript

# Normalize: lowercase, replace spaces with +
key = f"{action.lower().replace(' ', '+')}+{object.lower().replace(' ', '+')}"
# Result: "create+api+endpoint"
```

**Step 3: Search**
```python
if key in phrase_index:
    resp = phrase_index[key]
    resp_id = resp['responsibility_id']
    dept = resp['department']
    confidence = resp['confidence']
    print(f"✓ {resp_id} ({dept}) - {confidence}% match")
else:
    print(f"✗ No match for: {key}")
    # Use action/object variants to find alternatives
```

**Step 4: Handle no match**
```python
# If no exact match, search for similar phrases
def find_similar(search_key, phrase_index, threshold=70):
    from difflib import SequenceMatcher

    matches = []
    for key, data in phrase_index.items():
        similarity = SequenceMatcher(None, search_key, key).ratio() * 100
        if similarity >= threshold:
            matches.append({
                'key': key,
                'resp_id': data['responsibility_id'],
                'similarity': similarity
            })

    return sorted(matches, key=lambda x: x['similarity'], reverse=True)

similar = find_similar(key, phrase_index)
# Returns top matches above threshold
```

### Example Usage

**Example 1: Single responsibility lookup**
```python
import json

with open('Responsibilities/Core/phrase_matching_index.json', 'r') as f:
    index = json.load(f)

# Look up "create research folder"
key = "create+research+folder"
resp = index.get(key, {})

if resp:
    print(f"RESP-ID: {resp['responsibility_id']}")
    print(f"Department: {resp['department']}")
else:
    print("No match found")

# Output:
# RESP-ID: RESP-AI-001
# Department: AI
```

**Example 2: Batch processing from CSV**
```python
import pandas as pd
import json

# Load actions
actions_df = pd.read_csv('extracted_actions.csv')
# Columns: ACTION, OBJECT, ASSIGNEE, PRIORITY

# Load index
with open('Responsibilities/Core/phrase_matching_index.json', 'r') as f:
    index = json.load(f)

# Assign RESP-IDs
results = []
for _, row in actions_df.iterrows():
    key = f"{row['ACTION'].lower()}+{row['OBJECT'].lower().replace(' ', '+')}"
    resp = index.get(key, {})

    results.append({
        'ACTION': row['ACTION'],
        'OBJECT': row['OBJECT'],
        'RESP_ID': resp.get('responsibility_id', 'UNKNOWN'),
        'DEPARTMENT': resp.get('department', 'UNKNOWN'),
        'ASSIGNEE': row['ASSIGNEE'],
        'PRIORITY': row['PRIORITY']
    })

# Save enriched CSV
pd.DataFrame(results).to_csv('actions_with_resp_ids.csv', index=False)
```

---

## Library 2: Action Variants

**Path:** `ENTITIES/LIBRARIES/Responsibilities/Variants/action_variants.csv`
**Size:** 57 action variants
**Purpose:** Normalize action verbs to canonical forms

### When to Use
- Before searching Responsibilities library
- User input uses non-standard verbs (build, make, setup vs create)
- Processing natural language (transcripts, emails)
- Ensuring consistent action naming

### Quick Start

**Step 1: Load variants**
```python
import pandas as pd

action_variants = pd.read_csv('Responsibilities/Variants/action_variants.csv')

# Structure:
# variant,canonical_form,department,usage_count
# build,create,Development,142
# make,create,All,89
# setup,configure,All,67
```

**Step 2: Normalize action**
```python
def normalize_action(input_action):
    canonical = action_variants[
        action_variants['variant'] == input_action.lower()
    ]['canonical_form'].values

    if len(canonical) > 0:
        return canonical[0]
    else:
        return input_action  # Return original if no variant

# Example
normalize_action("build")  # Returns: "create"
normalize_action("setup")  # Returns: "configure"
normalize_action("create")  # Returns: "create" (already canonical)
```

**Step 3: Use in workflow**
```python
# User says: "build an API endpoint"
user_action = "build"
user_object = "API endpoint"

# Normalize
normalized_action = normalize_action(user_action)  # "create"

# Now search Responsibilities
key = f"{normalized_action}+{user_object.lower().replace(' ', '+')}"
# key = "create+api+endpoint"

resp = phrase_index[key]  # Will find RESP-DEV-015
```

### Example Usage

**Example 1: Batch normalization**
```python
import pandas as pd

# Load variants
variants = pd.read_csv('Responsibilities/Variants/action_variants.csv')

# Create lookup dictionary
action_map = dict(zip(variants['variant'], variants['canonical_form']))

# Normalize list of actions
user_actions = ["build", "make", "setup", "create", "configure"]
normalized = [action_map.get(a.lower(), a) for a in user_actions]

# Result: ["create", "create", "configure", "create", "configure"]
```

---

## Library 3: Object Variants

**Path:** `ENTITIES/LIBRARIES/Responsibilities/Variants/object_variants.csv`
**Size:** 169 object variants
**Purpose:** Normalize object nouns to canonical forms

### When to Use
- Before searching Responsibilities library
- User input uses synonyms (folder vs directory, DB vs database)
- Processing natural language
- Ensuring consistent object naming

### Quick Start

**Step 1: Load variants**
```python
import pandas as pd

object_variants = pd.read_csv('Responsibilities/Variants/object_variants.csv')

# Structure:
# variant,canonical_form,category,usage_count
# folder,directory,filesystem,156
# DB,database,data,203
# auth,authentication,security,87
```

**Step 2: Normalize object**
```python
def normalize_object(input_object):
    canonical = object_variants[
        object_variants['variant'] == input_object.lower()
    ]['canonical_form'].values

    if len(canonical) > 0:
        return canonical[0]
    else:
        return input_object

# Example
normalize_object("folder")  # Returns: "directory"
normalize_object("DB")  # Returns: "database"
normalize_object("api_endpoint")  # Returns: "api_endpoint" (already canonical)
```

**Step 3: Combined normalization**
```python
def normalize_action_object(action, object):
    norm_action = normalize_action(action)
    norm_object = normalize_object(object)
    return norm_action, norm_object

# Example
action, object = normalize_action_object("build", "folder")
# Returns: ("create", "directory")

# Build search key
key = f"{action}+{object}"
# key = "create+directory"
```

### Example Usage

**Example 1: Normalize from transcript**
```python
# Transcript: "We need to setup a new DB for the API"
# Extracted: action="setup", object="DB"

norm_action = normalize_action("setup")  # "configure"
norm_object = normalize_object("DB")  # "database"

key = f"{norm_action}+{norm_object}"  # "configure+database"

resp = phrase_index[key]  # Finds RESP-DEV-023
```

---

## Library 4: Templates (TSM-004)

**Path:** `TASK_MANAGERS/TSM-004_Step_Templates/`
**Size:** 155+ templates across 8 departments
**Purpose:** Reuse existing step templates before creating custom

### When to Use
- Creating any multi-step task
- Before writing custom task steps
- Ensuring consistency across similar tasks
- Reducing redundant template creation

### Quick Start

**Step 1: Search templates by action and department**
```python
import glob
import json

def find_templates(action, department=None):
    pattern = 'TASK_MANAGERS/TSM-004_Step_Templates/**/*.json'
    templates = glob.glob(pattern, recursive=True)

    matches = []
    for path in templates:
        # Filter by department
        if department and f'/{department}/' not in path:
            continue

        with open(path, 'r') as f:
            template = json.load(f)

        # Check if action matches
        if action.lower() in template.get('action', '').lower():
            matches.append({
                'path': path,
                'action': template.get('action'),
                'steps': template.get('steps', []),
                'match_score': calculate_similarity(action, template.get('action', ''))
            })

    # Sort by match score
    matches.sort(key=lambda x: x['match_score'], reverse=True)
    return matches

# Example
api_templates = find_templates('create api', 'DEV')
```

**Step 2: Evaluate template match**
```python
def should_inherit_template(match_score):
    if match_score >= 80:
        return 'inherit'  # Use as-is, customize parameters only
    elif match_score >= 50:
        return 'modify'  # Use structure, change steps
    else:
        return 'reference'  # Create custom, reference similar patterns

# Example
for template in api_templates[:3]:  # Top 3 matches
    decision = should_inherit_template(template['match_score'])
    print(f"{template['path']}: {template['match_score']}% - {decision}")
```

**Step 3: Inherit template**
```python
import json

# Load best match
with open(api_templates[0]['path'], 'r') as f:
    template = json.load(f)

# Customize
template['parameters']['endpoint_path'] = '/api/v2/users'
template['parameters']['http_method'] = 'POST'
template['assignee'] = 'Artem_Skichko'

# Save customized version
with open('output/task_create_users_api.json', 'w') as f:
    json.dump(template, f, indent=2)
```

### Template Structure

```json
{
  "template_id": "TSM-004-DEV-015",
  "action": "create_api_endpoint",
  "department": "DEV",
  "steps": [
    {
      "step_number": 1,
      "description": "Define endpoint specification",
      "parameters": ["endpoint_path", "http_method", "auth_required"],
      "tools": ["Cursor", "Postman"],
      "estimated_duration": "15min"
    },
    {
      "step_number": 2,
      "description": "Implement request handler",
      "parameters": ["input_schema", "output_schema", "error_handling"],
      "tools": ["Cursor", "VS_Code"],
      "estimated_duration": "45min"
    }
  ],
  "total_duration": "2hr",
  "dependencies": ["database_configured", "auth_setup"],
  "outputs": ["endpoint_code", "api_tests", "documentation"]
}
```

### Example Usage

**Example 1: Find and inherit template**
```python
# Task: Create new API endpoint for user registration

# Search templates
templates = find_templates('create api', 'DEV')

# Best match: create_api_endpoint.json (92% similarity)
with open(templates[0]['path'], 'r') as f:
    template = json.load(f)

# Customize
template['parameters']['endpoint_path'] = '/api/v1/auth/register'
template['parameters']['http_method'] = 'POST'
template['steps'][0]['parameters'].append('user_schema')

# Use customized template
# (Pass to execution system)
```

---

## Library 5: Parameters (TSM-003)

**Path:** `TASK_MANAGERS/TSM-003_Parameters/`
**Size:** 7,321 parameter mappings (473 state-based, 6,848 quality-based)
**Purpose:** Enrich outputs with metadata and quality parameters

### When to Use
- After completing task execution
- Before generating final output
- Adding validation rules
- Enriching CSVs/JSON with metadata

### Quick Start

**Step 1: Load parameters**
```python
import pandas as pd

quality_params = pd.read_csv('TSM-003_Parameters/Mappings/quality_parameters.csv')
state_params = pd.read_csv('TSM-003_Parameters/Mappings/state_parameters.csv')

# Structure (quality):
# action,object,parameter_name,data_type,default_value,validation_rule,required
# create,api_endpoint,http_method,enum,GET,"GET|POST|PUT|DELETE",true
# create,api_endpoint,auth_required,boolean,true,true|false,true

# Structure (state):
# entity_type,state_name,allowed_transitions,validation,metadata
# task,pending,"in_progress,cancelled",assignee_required,priority_set
# task,in_progress,"completed,blocked",duration_tracking,progress_percentage
```

**Step 2: Get parameters for action/object**
```python
def get_parameters(action, object, param_type='quality'):
    if param_type == 'quality':
        df = quality_params
    else:
        df = state_params

    # Filter by action/object
    params = df[
        (df['action'] == action) | (df['object'] == object)
    ]

    return params.to_dict('records')

# Example
api_params = get_parameters('create', 'api_endpoint')
# Returns list of parameter definitions
```

**Step 3: Apply parameters to output**
```python
def enrich_output(data, action, object):
    params = get_parameters(action, object)

    enriched = data.copy()

    # Add parameters with defaults
    for param in params:
        param_name = param['parameter_name']
        if param_name not in enriched:
            enriched[param_name] = param['default_value']

    # Validate
    for param in params:
        if param['required'] and enriched.get(param['parameter_name']) is None:
            raise ValueError(f"Required parameter missing: {param['parameter_name']}")

    return enriched

# Example
task_data = {
    'task_id': 'TSK-001',
    'description': 'Create user API endpoint'
}

enriched_task = enrich_output(task_data, 'create', 'api_endpoint')
# Adds: http_method, auth_required, endpoint_path, etc.
```

### Example Usage

**Example 1: Enrich CSV output**
```python
import pandas as pd

# Original output
tasks = pd.read_csv('tasks_basic.csv')
# Columns: TASK_ID, ACTION, OBJECT, ASSIGNEE

# Load parameters
quality_params = pd.read_csv('TSM-003_Parameters/Mappings/quality_parameters.csv')

# For each row, add parameters
enriched_rows = []
for _, task in tasks.iterrows():
    params = quality_params[
        (quality_params['action'] == task['ACTION']) &
        (quality_params['object'] == task['OBJECT'])
    ]

    row = task.to_dict()

    for _, param in params.iterrows():
        row[param['parameter_name']] = param['default_value']

    enriched_rows.append(row)

# Save enriched CSV
pd.DataFrame(enriched_rows).to_csv('tasks_enriched.csv', index=False)
```

---

## Library 6: Tools

**Path:** `ENTITIES/LIBRARIES/Responsibilities/Metadata/tools_by_dept.csv`
**Purpose:** Select appropriate tools by department and task

### When to Use
- Assigning tasks to employees
- Checking tool availability
- Enforcing tool requirements
- Tool compliance tracking

### Quick Start

```python
import pandas as pd

tools = pd.read_csv('Responsibilities/Metadata/tools_by_dept.csv')

# Structure:
# department,tool_name,tool_type,required,usage_count
# Development,Cursor,IDE,yes,387
# Development,VS_Code,IDE,yes,256
# Development,AntiGravity,IDE,yes,12
# Design,Figma,design_tool,yes,198

# Get tools for department
dev_tools = tools[tools['department'] == 'Development']
required_dev_tools = dev_tools[dev_tools['required'] == 'yes']

# Check employee has tools
employee_tools = ['Cursor', 'VS_Code']
missing = set(required_dev_tools['tool_name']) - set(employee_tools)
if missing:
    print(f"Missing required tools: {missing}")
```

---

## Library 7: Professions

**Path:** `ENTITIES/LIBRARIES/Responsibilities/Metadata/professions.csv`
**Purpose:** Assign work by role and skill level

### Quick Start

```python
import pandas as pd

professions = pd.read_csv('Responsibilities/Metadata/professions.csv')

# Structure:
# role,required_skills,department,level,responsibilities
# frontend_developer,"HTML,CSS,JS,React",Development,mid,"RESP-DEV-001,RESP-DEV-015"
# backend_developer,"Python,API,Database",Development,mid,"RESP-DEV-023,RESP-DEV-042"

# Match task to role
required_skills = ['API', 'Database']
matches = professions[
    professions['required_skills'].str.contains('API') &
    professions['required_skills'].str.contains('Database')
]
```

---

## Integration Workflow

### Complete library integration for single task:

```python
import json
import pandas as pd

# Task input
user_action = "build"
user_object = "API endpoint"
assignee = "Artem_Skichko"

# Step 1: Normalize action/object (Variants)
norm_action = normalize_action(user_action)  # "create"
norm_object = normalize_object(user_object)  # "api_endpoint"

# Step 2: Get RESP-ID (Responsibilities)
key = f"{norm_action}+{norm_object}"
with open('Responsibilities/Core/phrase_matching_index.json', 'r') as f:
    phrase_index = json.load(f)
resp = phrase_index[key]
resp_id = resp['responsibility_id']  # RESP-DEV-015
dept = resp['department']  # Development

# Step 3: Find template (Templates)
templates = find_templates(norm_action, dept)
if templates and templates[0]['match_score'] >= 80:
    with open(templates[0]['path'], 'r') as f:
        template = json.load(f)
else:
    template = create_custom_template()

# Step 4: Enrich with parameters (Parameters)
params = get_parameters(norm_action, norm_object)
for param in params:
    template['parameters'][param['parameter_name']] = param['default_value']

# Step 5: Assign tools (Tools)
tools_df = pd.read_csv('Responsibilities/Metadata/tools_by_dept.csv')
required_tools = tools_df[
    (tools_df['department'] == dept) &
    (tools_df['required'] == 'yes')
]['tool_name'].tolist()
template['required_tools'] = required_tools

# Step 6: Output enriched task
output = {
    'task_id': 'TSK-NEW-001',
    'resp_id': resp_id,
    'department': dept,
    'action': norm_action,
    'object': norm_object,
    'assignee': assignee,
    'template_used': templates[0]['path'] if templates else 'custom',
    'parameters': template['parameters'],
    'required_tools': required_tools,
    'steps': template['steps']
}

# Save
with open('output/task_enriched.json', 'w') as f:
    json.dump(output, f, indent=2)
```

---

## Quick Reference Card

```csv
NEED,USE_LIBRARY,PATH,METHOD
Assign RESP-ID,Responsibilities,Responsibilities/Core/phrase_matching_index.json,Search by action+object
Normalize action,Action Variants,Responsibilities/Variants/action_variants.csv,Lookup variant → canonical
Normalize object,Object Variants,Responsibilities/Variants/object_variants.csv,Lookup variant → canonical
Reuse template,Templates,TSM-004_Step_Templates/**/*.json,Search by action+dept
Enrich output,Parameters,TSM-003_Parameters/Mappings/,Filter by action+object
Select tools,Tools,Responsibilities/Metadata/tools_by_dept.csv,Filter by department
Assign by role,Professions,Responsibilities/Metadata/professions.csv,Match skills
```

---

**Use this guide when:**
- Starting any new task processing
- Unsure which library to use
- Need quick integration examples
- Building automated workflows

**Next steps:**
- Read full library documentation: `ENTITIES/LIBRARIES/Responsibilities/README.md`
- Review template index: `TASK_MANAGERS/TEMPLATES_INDEX.md` (to be created)
- Use integrated prompt template: `System/SYS.14_PROMPT_TEMPLATE_LIBRARY_INTEGRATED.md`

---

**END QUICK START GUIDE**
