# Milestone 4: Relationship Validation

**Milestone ID:** MIL-TEMPL-004
**Phase:** 4
**Can Run Parallel:** No
**Dependencies:** MIL-TEMPL-001 (Data Inventory)
**Estimated Hours:** 3.0

---

## Objective

Validate all cross-references between entities, verify index accuracy, and map dependency flows to ensure proper linking throughout the ecosystem.

---

## Tasks Overview

This milestone consists of 3 tasks:

1. **TASK-TEMPLATE-ANALYSIS-010:** Cross-Reference Validation (1.5 hours)
2. **TASK-TEMPLATE-ANALYSIS-011:** Index Accuracy Check (1.0 hours)
3. **TASK-TEMPLATE-ANALYSIS-012:** Dependency Flow Mapping (0.5 hours)

---

## Task 1: Cross-Reference Validation

**Task ID:** TASK-TEMPLATE-ANALYSIS-010
**Estimated Hours:** 1.5

### Steps:

#### Step 1: Extract all reference IDs
- Scan all JSON files for reference fields
- Extract all entity IDs that are referenced
- Build reference map

**Python Script:**
```python
import json
from pathlib import Path

references = {
    'tasks_to_steps': [],
    'milestones_to_tasks': [],
    'projects_to_milestones': []
}

# Define reference fields by entity type
reference_fields = {
    'Task_Templates': {
        'step_templates': 'tasks_to_steps'
    },
    'Milestone_Templates': {
        'task_templates': 'milestones_to_tasks'
    },
    'Project_Templates': {
        'milestone_templates': 'projects_to_milestones'
    }
}

# Extract references
for json_file in Path('C:/Users/Dell/Dropbox/ENTITIES').rglob('*.json'):
    try:
        with open(json_file) as f:
            data = json.load(f)

        entity_type = json_file.parent.name

        if entity_type in reference_fields:
            for field, ref_type in reference_fields[entity_type].items():
                if field in data:
                    value = data[field]

                    # Handle both single values and arrays
                    if isinstance(value, list):
                        for item in value:
                            if isinstance(item, dict):
                                # Extract ID from object
                                for key in item:
                                    if '_id' in key:
                                        references[ref_type].append({
                                            'source': str(json_file),
                                            'target_id': item[key]
                                        })
                            else:
                                references[ref_type].append({
                                    'source': str(json_file),
                                    'target_id': item
                                })
                    else:
                        references[ref_type].append({
                            'source': str(json_file),
                            'target_id': value
                        })
    except:
        pass

# Save reference map
with open('reference_map.json', 'w') as f:
    json.dump(references, f, indent=2)
```

**Expected Output:**
- Complete map of all cross-references
- Source and target IDs for each reference
- Reference counts by type

#### Step 2: Validate references exist
- Check that all referenced IDs actually exist
- Identify broken references
- Categorize by severity

**Python Validation Script:**
```python
import json
from pathlib import Path

# Load reference map
with open('reference_map.json') as f:
    references = json.load(f)

# Build index of all existing IDs
existing_ids = {
    'steps': set(),
    'tasks': set(),
    'milestones': set(),
    'projects': set()
}

# Scan all files to build ID index
for json_file in Path('C:/Users/Dell/Dropbox/ENTITIES').rglob('*.json'):
    try:
        with open(json_file) as f:
            data = json.load(f)

        # Extract ID based on field name
        for key, value in data.items():
            if key.endswith('_id') and not key.endswith('parent_id'):
                if 'STEP' in value:
                    existing_ids['steps'].add(value)
                elif 'TASK' in value:
                    existing_ids['tasks'].add(value)
                elif 'MIL' in value:
                    existing_ids['milestones'].add(value)
                elif 'PROJ' in value:
                    existing_ids['projects'].add(value)
    except:
        pass

# Validate references
broken_references = []

# Map reference types to ID collections
ref_to_id_map = {
    'tasks_to_steps': 'steps',
    'milestones_to_tasks': 'tasks',
    'projects_to_milestones': 'milestones'
}

for ref_type, refs in references.items():
    id_collection = ref_to_id_map[ref_type]

    for ref in refs:
        if ref['target_id'] not in existing_ids[id_collection]:
            broken_references.append({
                'reference_type': ref_type,
                'source_file': ref['source'],
                'target_id': ref['target_id'],
                'severity': 'critical' if 'TASK' in ref['target_id'] or 'MIL' in ref['target_id'] else 'warning'
            })

# Save broken references
with open('broken_references.json', 'w') as f:
    json.dump({
        'total_broken': len(broken_references),
        'broken_by_type': {},
        'details': broken_references
    }, f, indent=2)
```

#### Step 3: Check bidirectional links
- Verify that references work both ways
- Find unidirectional references
- Document linking inconsistencies

**Python Script:**
```python
import json

# Load reference map
with open('reference_map.json') as f:
    references = json.load(f)

bidirectional_issues = []

# Check Tasks → Steps bidirectional references
tasks_to_steps = {ref['target_id']: ref['source'] for ref in references['tasks_to_steps']}
steps_to_tasks = {ref['target_id']: ref['source'] for ref in references.get('steps_to_tasks', [])}

# Find unidirectional references
for step_id, task_file in tasks_to_steps.items():
    if step_id not in steps_to_tasks:
        bidirectional_issues.append({
            'type': 'tasks_steps',
            'issue': 'Task references step, but step does not reference task',
            'task_file': task_file,
            'step_id': step_id
        })

# Save results
with open('bidirectional_issues.json', 'w') as f:
    json.dump(bidirectional_issues, f, indent=2)
```

#### Step 4: Document broken references
- Create comprehensive cross-reference validation report
- Prioritize fixes by severity
- Provide fix recommendations

**Report Structure:**
```markdown
# Cross-Reference Validation Report

## Summary
- Total References: [count]
- Broken References: [count]
- Bidirectional Issues: [count]

## Critical Broken References
[List of missing critical references]

## Warning-Level Issues
[List of minor broken references]

## Bidirectional Link Issues
[List of unidirectional references]

## Fix Recommendations
1. Add missing entities for IDs: [list]
2. Update references in files: [list]
3. Add reverse references: [list]
```

### Checklist:
- [ ] Extract all reference IDs
- [ ] Validate referenced IDs exist
- [ ] Check bidirectional links
- [ ] Document all broken references
- [ ] Create fix priority list

---

## Task 2: Index Accuracy Check

**Task ID:** TASK-TEMPLATE-ANALYSIS-011
**Estimated Hours:** 1.0

### Steps:

#### Step 1: Extract index file contents
- Read all index and listing files
- Extract entity listings from each index

**PowerShell Script:**
```powershell
$indexFiles = Get-ChildItem -Path "C:\Users\Dell\Dropbox\ENTITIES" -Filter "*INDEX*.md" -Recurse
$indexFiles += Get-ChildItem -Path "C:\Users\Dell\Dropbox\ENTITIES" -Filter "*Checklist-Item-003*.md" -Recurse
$indexFiles += Get-ChildItem -Path "C:\Users\Dell\Dropbox\ENTITIES" -Filter "*Checklist-Item-003*.json" -Recurse

$indexContents = @()

foreach ($file in $indexFiles) {
    $indexContents += [PSCustomObject]@{
        File = $file.FullName
        Name = $file.Name
        Type = $file.Extension
        Content = Get-Content $file.FullName -Raw
    }
}

$indexContents | ConvertTo-Json -Depth 10 | Out-File "index_contents.json"
```

#### Step 2: Compare against actual files
- Compare index listings with actual file system
- Find missing entries in indexes
- Find orphaned index entries (no matching file)

**Python Comparison:**
```python
import json
import re
from pathlib import Path

# Load index contents
with open('index_contents.json') as f:
    indexes = json.load(f)

# Get actual files
actual_files = {
    'actions': list(Path('C:/Users/Dell/Dropbox/ENTITIES/LIBRARIES/Actions').rglob('*.json')),
    'products': list(Path('C:/Users/Dell/Dropbox/ENTITIES/LIBRARIES/Products').rglob('*.json')),
    'tasks': list(Path('C:/Users/Dell/Dropbox/ENTITIES/TASK_MANAGERS/Task_Templates').rglob('*.json')),
    'milestones': list(Path('C:/Users/Dell/Dropbox/ENTITIES/TASK_MANAGERS/Milestone_Templates').rglob('*.json')),
    'projects': list(Path('C:/Users/Dell/Dropbox/ENTITIES/TASK_MANAGERS/Project_Templates').rglob('*.json'))
}

# Extract IDs from index files
indexed_ids = {
    'actions': set(),
    'products': set(),
    'tasks': set(),
    'milestones': set(),
    'projects': set()
}

for index in indexes:
    content = index['Content']

    # Extract ACTION IDs
    actions = re.findall(r'ACTION-\d{3}', content)
    indexed_ids['actions'].update(actions)

    # Extract Product IDs
    products = re.findall(r'PDT-\d{4}', content)
    indexed_ids['products'].update(products)

    # Extract Task IDs
    tasks = re.findall(r'TASK-TEMPLATE-[A-Z]+-\d{3}', content)
    indexed_ids['tasks'].update(tasks)

    # Extract Milestone IDs
    milestones = re.findall(r'MIL-TEMPL-\d{3}', content)
    indexed_ids['milestones'].update(milestones)

    # Extract Project IDs
    projects = re.findall(r'PROJ-TEMPL-\d{3}', content)
    indexed_ids['projects'].update(projects)

# Compare with actual files
discrepancies = {}

for entity_type, files in actual_files.items():
    actual_ids = set()

    for file in files:
        with open(file) as f:
            data = json.load(f)

        # Extract ID
        for key, value in data.items():
            if key.endswith('_id'):
                actual_ids.add(value)
                break

    # Find missing and orphaned
    missing_from_index = actual_ids - indexed_ids[entity_type]
    orphaned_in_index = indexed_ids[entity_type] - actual_ids

    discrepancies[entity_type] = {
        'missing_from_index': list(missing_from_index),
        'orphaned_in_index': list(orphaned_in_index)
    }

# Save results
with open('index_discrepancies.json', 'w') as f:
    json.dump(discrepancies, f, indent=2)
```

#### Step 3: Identify missing entries
- List all entities not in indexes
- Categorize by entity type
- Calculate index coverage percentage

#### Step 4: Document index errors
- Create index accuracy report
- Provide update recommendations

**Report Structure:**
```markdown
# Index Accuracy Report

## Coverage Summary
- Actions: [X]% coverage ([Y] indexed / [Z] total)
- Products: [X]% coverage
- Tasks: [X]% coverage
- Milestones: [X]% coverage

## Missing from Indexes
[List of entities not in indexes]

## Orphaned Index Entries
[List of index entries with no matching file]

## Recommendations
- Add to indexes: [list]
- Remove from indexes: [list]
- Create missing files: [list]
```

### Checklist:
- [ ] Extract all index file contents
- [ ] Compare indexes against actual files
- [ ] Identify missing entries
- [ ] Identify orphaned entries
- [ ] Calculate coverage percentages
- [ ] Document all index errors

---

## Task 3: Dependency Flow Mapping

**Task ID:** TASK-TEMPLATE-ANALYSIS-012
**Estimated Hours:** 0.5

### Steps:

#### Step 1: Extract dependency chains
- Identify all dependency relationships
- Build dependency tree
- Map hierarchical flows

**Python Script:**
```python
import json
from pathlib import Path

dependency_chains = []

# Scan milestones for dependencies
for milestone_file in Path('C:/Users/Dell/Dropbox/ENTITIES/TASK_MANAGERS/Milestone_Templates').rglob('*.json'):
    with open(milestone_file) as f:
        data = json.load(f)

    if 'dependencies' in data and data['dependencies']:
        for dep in data['dependencies']:
            dependency_chains.append({
                'source': data['milestone_template_id'],
                'target': dep,
                'type': 'milestone_dependency'
            })

# Save dependency chains
with open('dependency_chains.json', 'w') as f:
    json.dump(dependency_chains, f, indent=2)
```

#### Step 2: Create flow diagrams
- Generate Mermaid diagrams for dependencies
- Create entity relationship diagrams
- Visualize reference flows

**Mermaid Diagram Generation:**
```python
import json

# Load dependencies
with open('dependency_chains.json') as f:
    dependencies = json.load(f)

# Generate Mermaid syntax
mermaid = "graph TD\n"

for dep in dependencies:
    mermaid += f"    {dep['source']} --> {dep['target']}\n"

# Save diagram
with open('dependency_flow.mmd', 'w') as f:
    f.write(mermaid)
```

#### Step 3: Identify circular dependencies
- Detect circular reference patterns
- Flag potential issues
- Recommend resolution

**Circular Dependency Detection:**
```python
def find_circular_dependencies(dependencies):
    """Detect circular dependencies using DFS"""
    graph = {}

    # Build adjacency list
    for dep in dependencies:
        if dep['source'] not in graph:
            graph[dep['source']] = []
        graph[dep['source']].append(dep['target'])

    # DFS to detect cycles
    visited = set()
    rec_stack = set()
    cycles = []

    def dfs(node, path):
        visited.add(node)
        rec_stack.add(node)
        path.append(node)

        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor, path.copy()):
                        return True
                elif neighbor in rec_stack:
                    cycles.append(path + [neighbor])
                    return True

        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            dfs(node, [])

    return cycles

# Load dependencies
with open('dependency_chains.json') as f:
    dependencies = json.load(f)

# Find circular dependencies
circular = find_circular_dependencies(dependencies)

# Save results
with open('circular_dependencies.json', 'w') as f:
    json.dump({
        'found_circular': len(circular) > 0,
        'cycles': circular
    }, f, indent=2)
```

### Checklist:
- [ ] Extract all dependency chains
- [ ] Create flow diagrams (Mermaid)
- [ ] Identify circular dependencies
- [ ] Document dependency structure

---

## Expected Reports

1. **REP-007: Cross-Reference Validation Report**
   - Location: `ANALYTICS/REPORTS/System_Analysis/`
   - Format: Markdown + JSON
   - Contains: Broken references, bidirectional issues, fix recommendations

2. **REP-008: Index Accuracy Report**
   - Location: `ANALYTICS/REPORTS/System_Analysis/`
   - Format: Markdown + JSON
   - Contains: Coverage percentages, missing entries, orphaned entries

---

## Success Criteria

- [ ] All cross-references validated
- [ ] Broken references documented
- [ ] Index accuracy verified
- [ ] Dependency flows mapped
- [ ] Circular dependencies identified (if any)
- [ ] All reports generated and saved
- [ ] Fix recommendations prioritized

---

## Notes

- This milestone MUST run after Milestone 1 (needs file inventory)
- Cannot run in parallel - requires complete entity list
- Dependency validation is critical for project execution
- Focus on structural integrity of the entire system
