# PMT-078: Cross Entity Search v1.0

**Prompt ID:** PMT-078
**Version:** 1.0
**Department:** System Architecture
**Category:** SEARCH_DISCOVERY
**Date:** 2025-11-21
**Status:** Active
**Parent Prompt:** PMT-074 (Data Architect Master)

---

## Purpose

Unified search system across all 21 ENTITIES folders. Single query returns multi-entity results with relationship traversal and context-aware discovery.

**Core Functions:**
1. **Unified Search**: Query all entities from one interface
2. **Relationship Traversal**: Follow TSK→MLT→PRT chains automatically
3. **Context-Aware Results**: Understand entity relationships
4. **Multi-Pattern Matching**: ID, name, description, content search
5. **Result Ranking**: Score by relevance and relationship strength

---

## Search Architecture

### Search Index Structure

```json
{
  "search_index_version": "1.0",
  "last_updated": "2025-11-21",
  "entities": [
    {
      "entity_type": "Tool",
      "entity_id": "TOL-015",
      "name": "n8n Automation",
      "description": "Workflow automation platform",
      "file_path": "LIBRARIES/Tools/TOL-015_n8n.json",
      "department": "AID",
      "status": "Active",
      "search_keywords": ["n8n", "automation", "workflow", "integration"],
      "related_entities": {
        "responsibilities": ["RSP-089", "RSP-134"],
        "tasks": ["TSK-042", "TSK-055"],
        "mentioned_in_prompts": ["PMT-002", "PMT-070"]
      }
    }
  ]
}
```

### Query Processing Flow

```
User Query: "n8n workflow"
    ↓
[1] Tokenize & Normalize
    "n8n" + "workflow"
    ↓
[2] Search Across Entities
    - Tools: Match "n8n" → TOL-015
    - Responsibilities: Match "workflow" → RSP-134, RSP-089
    - Tasks: Match context → TSK-042
    ↓
[3] Traverse Relationships
    TSK-042 → MLT-010 → PRT-003
    ↓
[4] Rank Results
    Primary: TOL-015 (exact match, 100%)
    Related: TSK-042 (high relevance, 85%)
    Related: RSP-134 (medium relevance, 70%)
    ↓
[5] Return Formatted Results
```

---

## Search Operations

### Operation 1: Simple Entity Search

```python
def search_entities(query, entity_types=None, limit=10):
    """
    Search across all or specific entity types

    Args:
        query: Search terms
        entity_types: List of types or None for all
        limit: Max results to return

    Returns:
        Ranked list of matching entities
    """
    from pathlib import Path
    import json

    # Load search index
    index = load_search_index()

    query_lower = query.lower()
    query_tokens = query_lower.split()

    results = []

    for entity in index['entities']:
        # Filter by entity type if specified
        if entity_types and entity['entity_type'] not in entity_types:
            continue

        # Calculate relevance score
        score = 0

        # Exact ID match (highest priority)
        if entity['entity_id'].lower() == query_lower:
            score = 100

        # Name match
        elif query_lower in entity['name'].lower():
            if entity['name'].lower() == query_lower:
                score = 95  # Exact name match
            else:
                score = 80  # Partial name match

        # Description match
        elif query_lower in entity['description'].lower():
            score = 60

        # Keyword match
        else:
            keyword_matches = sum(1 for kw in entity['search_keywords'] if query_lower in kw)
            if keyword_matches > 0:
                score = 40 + (keyword_matches * 10)

        if score > 0:
            results.append({
                **entity,
                "relevance_score": score,
                "match_type": get_match_type(score)
            })

    # Sort by relevance
    results.sort(key=lambda x: x['relevance_score'], reverse=True)

    return results[:limit]
```

**Example Usage:**
```python
results = search_entities("n8n", entity_types=["Tool", "Task"], limit=5)
```

**Output:**
```markdown
## Search Results for "n8n"

### Found: 3 results

1. **TOL-015: n8n Automation** (Score: 95/100)
   - Type: Tool
   - Description: Workflow automation platform
   - Department: AID
   - Status: Active
   - File: [LIBRARIES/Tools/TOL-015_n8n.json]

2. **TSK-042: Configure_n8n_Integration** (Score: 80/100)
   - Type: Task
   - Description: Setup and configure n8n automation workflows
   - Milestone: MLT-010_CV_Screening_Setup
   - Project: PRT-003_HR_Automation
   - Status: Active

3. **RSP-134: Build_Automation_Workflow** (Score: 65/100)
   - Type: Responsibility
   - Description: Design and implement automation workflows
   - Tools Used: TOL-015 (n8n), TOL-042 (Make)
   - Department: AID
```

---

### Operation 2: Relationship Traversal

```python
def find_related_entities(entity_id, depth=2):
    """
    Find all entities related to given entity

    Args:
        entity_id: Starting entity (e.g., "TSK-042")
        depth: How many relationship hops (1-3)

    Returns:
        Graph of related entities
    """
    index = load_search_index()
    relationships = load_cross_reference_map()

    entity = find_entity_by_id(entity_id, index)
    if not entity:
        return {"error": "Entity not found"}

    related = {"entity": entity, "relationships": {}}

    # Level 1: Direct relationships
    if entity['entity_type'] == "Task":
        # Task → Milestone → Project
        milestone_id = entity.get('milestone_template_id')
        if milestone_id:
            milestone = find_entity_by_id(milestone_id, index)
            related['relationships']['parent_milestone'] = milestone

            project_id = milestone.get('project_template_id')
            if project_id:
                project = find_entity_by_id(project_id, index)
                related['relationships']['parent_project'] = project

        # Task → Steps
        steps = find_children(entity_id, 'Step', relationships)
        related['relationships']['child_steps'] = steps

        # Task → Tools Referenced
        tools = entity.get('tools_referenced', [])
        related['relationships']['tools'] = [
            find_entity_by_id(tool_id, index) for tool_id in tools
        ]

    # Level 2: Extended relationships (if depth ≥ 2)
    if depth >= 2:
        # Find other tasks in same milestone
        if 'parent_milestone' in related['relationships']:
            milestone_id = related['relationships']['parent_milestone']['entity_id']
            sibling_tasks = find_tasks_by_milestone(milestone_id, index)
            related['relationships']['sibling_tasks'] = sibling_tasks

    return related
```

**Example Usage:**
```python
related = find_related_entities("TSK-042", depth=2)
```

**Output:**
```markdown
## Relationship Map for TSK-042

### TSK-042: Configure_n8n_Integration
**Type:** Task
**Status:** Active

### Direct Relationships:

**Parent Milestone:**
└─ MLT-010: CV_Screening_Setup
   └─ **Parent Project:**
      └─ PRT-003: HR_Automation

**Child Steps:**
├─ STT-123: Install_n8n_Self_Hosted
├─ STT-124: Configure_API_Credentials
└─ STT-125: Build_CV_Parsing_Workflow

**Tools Referenced:**
├─ TOL-015: n8n Automation
├─ TOL-042: Make (alternative)
└─ TOL-089: Gemini AI

### Extended Relationships (Depth 2):

**Sibling Tasks (same milestone):**
├─ TSK-043: Setup_Gemini_API
├─ TSK-044: Create_Candidate_Database
└─ TSK-045: Build_CV_Parser_Workflow

**Mentioned In:**
├─ PMT-070: Daily_Report_Entity_Mapping
└─ PMT-003: HR_Automation (project documentation)
```

---

### Operation 3: Context-Aware Search

```python
def smart_search(query, context=None):
    """
    Context-aware search that understands intent

    Args:
        query: Search query
        context: Optional context (department, entity_type, recent_search)

    Returns:
        Intelligent results based on context
    """
    # Parse query for intent
    intent = detect_search_intent(query)

    if intent == "find_tool":
        # Query like "tool for automation"
        return search_entities(query, entity_types=["Tool"], limit=10)

    elif intent == "find_hierarchy":
        # Query like "what project is TSK-042 in?"
        entity_id = extract_entity_id(query)
        return find_related_entities(entity_id, depth=3)

    elif intent == "find_dependencies":
        # Query like "what depends on TOL-015?"
        entity_id = extract_entity_id(query)
        return find_dependencies(entity_id)

    elif intent == "find_department_tools":
        # Query like "tools used by HR department"
        dept_code = extract_department(query)
        return search_entities("", entity_types=["Tool"], filters={"department": dept_code})

    else:
        # General search
        return search_entities(query, limit=20)

def detect_search_intent(query):
    """Classify search query intent"""
    query_lower = query.lower()

    if any(word in query_lower for word in ["tool for", "which tool", "tool to"]):
        return "find_tool"
    elif any(word in query_lower for word in ["project", "milestone", "hierarchy", "parent"]):
        return "find_hierarchy"
    elif any(word in query_lower for word in ["depends", "dependency", "uses", "references"]):
        return "find_dependencies"
    elif any(word in query_lower for word in ["department", "team", "used by"]):
        return "find_department_tools"
    else:
        return "general_search"
```

**Example Queries:**
```python
# Query 1: Find tool
smart_search("tool for workflow automation")
# → Returns: TOL-015 (n8n), TOL-042 (Make), TOL-089 (Zapier)

# Query 2: Find hierarchy
smart_search("what project is TSK-042 in?")
# → Returns: TSK-042 → MLT-010 → PRT-003 (full hierarchy)

# Query 3: Find dependencies
smart_search("what tasks use n8n?")
# → Returns: TSK-042, TSK-055, TSK-067 (all tasks referencing TOL-015)

# Query 4: Department filter
smart_search("tools used by HR department")
# → Returns: All tools with department="HRM"
```

---

### Operation 4: Multi-Entity Search

```python
def search_all(query, max_results_per_type=5):
    """
    Search across all entity types and return categorized results
    """
    entity_types = [
        "Action", "Object", "Tool", "Responsibility", "Profession",
        "Project", "Milestone", "Task", "Step", "ChecklistTemplate",
        "ChecklistItem", "Prompt", "Workflow"
    ]

    results_by_type = {}

    for entity_type in entity_types:
        matches = search_entities(query, entity_types=[entity_type], limit=max_results_per_type)
        if matches:
            results_by_type[entity_type] = matches

    return {
        "query": query,
        "total_results": sum(len(matches) for matches in results_by_type.values()),
        "results_by_type": results_by_type,
        "top_match": get_top_match(results_by_type) if results_by_type else None
    }
```

**Output:**
```markdown
## Comprehensive Search: "automation"

**Total Results:** 42 across 8 entity types

### Tools (5 results):
1. TOL-015: n8n Automation (95%)
2. TOL-042: Make Automation (90%)
3. TOL-067: Zapier Automation (85%)
...

### Tasks (5 results):
1. TSK-042: Configure_n8n_Integration (80%)
2. TSK-067: Build_Automation_Rules (78%)
...

### Responsibilities (5 results):
1. RSP-134: Build_Automation_Workflow (75%)
2. RSP-089: Create_Automation_Trigger (72%)
...

### Prompts (3 results):
1. PMT-067: Rules_Automation (70%)
2. PMT-002: Main_Prompt_v6 (mentions automation) (45%)
...

**Top Match:** TOL-015 (n8n Automation) - 95% relevance
```

---

## Search Index Generation

### Build Search Index

```python
def generate_search_index():
    """
    Build unified search index from all master lists
    """
    import json
    from pathlib import Path

    index = {
        "version": "1.0",
        "generated_at": datetime.now().isoformat(),
        "entities": []
    }

    # Index LIBRARIES
    index['entities'].extend(index_libraries())

    # Index TASK_MANAGERS
    index['entities'].extend(index_task_managers())

    # Index PROMPTS
    index['entities'].extend(index_prompts())

    # Save index
    output_file = Path("PROMPTS/DATA_FIELDS/Search_Index.json")
    with open(output_file, 'w') as f:
        json.dump(index, f, indent=2)

    return {
        "total_entities": len(index['entities']),
        "output_file": str(output_file),
        "size_kb": output_file.stat().st_size / 1024
    }

def index_libraries():
    """Index all LIBRARIES entities"""
    entities = []

    # Actions
    actions = load_json("LIBRARIES/Actions/actions_master.json")
    for action in actions:
        entities.append({
            "entity_type": "Action",
            "entity_id": action['id'],
            "name": action['action'],
            "description": action.get('description', ''),
            "category": action['type'],
            "file_path": f"LIBRARIES/Actions/{action['id']}.json",
            "search_keywords": generate_keywords(action)
        })

    # Tools, Objects, Responsibilities, Professions (similar pattern)
    # ...

    return entities
```

**Run Index Generation:**
```bash
python generate_search_index.py
# Output: Search_Index.json (estimated 1.2 MB, 2,000+ entities)
```

---

## Advanced Search Features

### Fuzzy Matching

```python
from difflib import get_close_matches

def fuzzy_search(query, threshold=0.6):
    """
    Find similar entity names even with typos
    """
    index = load_search_index()

    all_names = [entity['name'] for entity in index['entities']]

    close_matches = get_close_matches(query, all_names, n=10, cutoff=threshold)

    results = []
    for match in close_matches:
        entity = find_entity_by_name(match, index)
        results.append(entity)

    return results

# Example
fuzzy_search("n8 automation")  # Typo: missing "n"
# → Still returns: TOL-015 (n8n Automation)
```

### Filter Search

```python
def filtered_search(query, filters):
    """
    Search with multiple filters

    Args:
        query: Search term
        filters: {
            "department": "AID",
            "status": "Active",
            "entity_type": ["Tool", "Task"],
            "date_range": ("2025-11-01", "2025-11-21")
        }
    """
    results = search_entities(query, entity_types=filters.get('entity_type'))

    # Apply filters
    if 'department' in filters:
        results = [r for r in results if r.get('department') == filters['department']]

    if 'status' in filters:
        results = [r for r in results if r.get('status') == filters['status']]

    if 'date_range' in filters:
        start, end = filters['date_range']
        results = [r for r in results if start <= r.get('last_updated', '') <= end]

    return results
```

---

## Best Practices

### DO:
- ✅ Use context-aware search for better results
- ✅ Traverse relationships to discover connected entities
- ✅ Update search index weekly or after bulk imports
- ✅ Use fuzzy matching for typo tolerance
- ✅ Filter by department for focused searches

### DON'T:
- ❌ Search without relationship context (miss connections)
- ❌ Use outdated search index (rebuild regularly)
- ❌ Ignore relevance scores (trust the ranking)
- ❌ Search only by ID (use name/description too)

---

## Integration with Other Prompts

**PMT-075**: Validate entity references found in search
**PMT-077**: Use search to find related employee activities
**PMT-079**: Update prompts that reference found entities

---

## Version History

**v1.0** (2025-11-21)
- Unified search across 21 entities
- Relationship traversal
- Context-aware search with intent detection
- Fuzzy matching and filters
- Search index generation

---

**Status:** Active

---

**End of Prompt**
