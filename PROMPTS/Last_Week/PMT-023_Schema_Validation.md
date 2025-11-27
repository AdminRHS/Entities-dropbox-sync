# Milestone 2: Schema & Naming Validation

**Milestone ID:** MIL-TEMPL-002
**Phase:** 2
**Can Run Parallel:** Yes
**Dependencies:** None
**Estimated Hours:** 3.0

---

## Objective

Validate naming conventions, JSON schemas, and version control consistency across all ENTITIES to ensure structural integrity and adherence to standards.

---

## Tasks Overview

This milestone consists of 3 tasks:

1. **TASK-TEMPLATE-ANALYSIS-004:** Naming Convention Audit (1.0 hours)
2. **TASK-TEMPLATE-ANALYSIS-005:** JSON Schema Validation (1.5 hours)
3. **TASK-TEMPLATE-ANALYSIS-006:** Version Control Consistency (0.5 hours)

---

## Task 1: Naming Convention Audit

**Task ID:** TASK-TEMPLATE-ANALYSIS-004
**Estimated Hours:** 1.0

### Steps:

#### Step 1: Extract naming patterns
- Scan all file and folder names across ENTITIES
- Group by entity type (Actions, Products, Tools, etc.)
- Document observed patterns for each type

**PowerShell Command:**
```powershell
Get-ChildItem -Path "C:\Users\Dell\Dropbox\ENTITIES" -Recurse -File |
  Select-Object Name, DirectoryName, Extension |
  Export-Csv -Path "C:\Users\Dell\Dropbox\ENTITIES\ANALYTICS\REPORTS\System_Analysis\naming_patterns.csv" -NoTypeInformation
```

**Expected Output:**
- CSV file with all filenames and paths
- Pattern groups by entity type

#### Step 2: Validate against conventions
- Compare extracted patterns against documented conventions:
  - Actions: `ACTION-###` (e.g., ACTION-001)
  - Products: `PDT-####` (e.g., PDT-0001)
  - Steps: `STEP-{CATEGORY}-{TASK#}-{STEP#}`
  - Projects: `PROJ-###`
  - Milestones: `MIL-TEMPL-###`
  - Tasks: `TASK-TEMPLATE-{CATEGORY}-###`

**Python Script:**
```python
import pandas as pd
import re

# Load naming data
df = pd.read_csv('naming_patterns.csv')

# Define patterns
patterns = {
    'Actions': r'ACTION-\d{3}',
    'Products': r'PDT-\d{4}',
    'Steps': r'STEP-[A-Z]+-\d{3}-\d{2}',
    'Projects': r'PROJ-\d{3}',
    'Milestones': r'MIL-TEMPL-\d{3}',
    'Tasks': r'TASK-TEMPLATE-[A-Z]+-\d{3}'
}

# Validate each pattern
violations = []
for pattern_name, pattern in patterns.items():
    matching_files = df[df['Name'].str.contains(pattern, na=False)]
    non_matching = df[~df['Name'].str.contains(pattern, na=False) &
                      df['DirectoryName'].str.contains(pattern_name, na=False)]
    violations.extend(non_matching.to_dict('records'))

# Save violations
pd.DataFrame(violations).to_csv('naming_violations.csv', index=False)
```

#### Step 3: Document violations
- Create report of all naming convention violations
- Categorize by severity (critical, warning, info)
- Provide recommendations for each violation

**Report Structure:**
```markdown
# Naming Convention Violations

## Critical Violations
- Files that completely break naming patterns
- Missing required prefixes

## Warnings
- Minor inconsistencies (case, separators)
- Deprecated patterns still in use

## Recommendations
- Standardize to: [pattern]
- Rename: [old] → [new]
```

### Checklist:
- [ ] Extract all naming patterns
- [ ] Validate against documented conventions
- [ ] Document all violations
- [ ] Create remediation recommendations

---

## Task 2: JSON Schema Validation

**Task ID:** TASK-TEMPLATE-ANALYSIS-005
**Estimated Hours:** 1.5

### Steps:

#### Step 1: Extract JSON schemas by type
- Scan all JSON files across ENTITIES
- Group by entity type (Actions, Products, Tools, etc.)
- Extract field structure for each type

**PowerShell Command:**
```powershell
$jsonFiles = Get-ChildItem -Path "C:\Users\Dell\Dropbox\ENTITIES" -Filter "*.json" -Recurse
$schemas = @{}

foreach ($file in $jsonFiles) {
    $content = Get-Content $file.FullName | ConvertFrom-Json
    $type = $file.Directory.Name

    if (-not $schemas.ContainsKey($type)) {
        $schemas[$type] = @()
    }

    $fields = $content.PSObject.Properties.Name
    $schemas[$type] += @{
        File = $file.Name
        Fields = $fields
    }
}

$schemas | ConvertTo-Json -Depth 10 | Out-File "schema_extraction.json"
```

#### Step 2: Validate required fields
- Define required fields for each entity type
- Check all files for presence of required fields
- Document missing fields

**Required Fields by Entity:**

**Actions:**
- action_id
- action_name
- category
- version

**Products:**
- product_id
- product_name
- tools (array)
- actions (array)

**Steps:**
- step_template_id
- action
- tool
- description

**Projects:**
- project_template_id
- template_name
- department
- milestone_templates

**Milestones:**
- milestone_template_id
- name
- task_templates
- dependencies

**Tasks:**
- task_template_id
- task_template_name
- category
- step_templates

#### Step 3: Check field consistency
- Verify field naming conventions (snake_case vs camelCase)
- Check data types consistency
- Validate array structures

**Python Validation:**
```python
import json
from pathlib import Path

# Load required schemas
required_schemas = {
    'Actions': ['action_id', 'action_name', 'category', 'version'],
    'Products': ['product_id', 'product_name', 'tools', 'actions'],
    'Steps': ['step_template_id', 'action', 'tool', 'description'],
    # Add more...
}

violations = []

for json_file in Path('C:/Users/Dell/Dropbox/ENTITIES').rglob('*.json'):
    with open(json_file) as f:
        data = json.load(f)

    entity_type = json_file.parent.name
    if entity_type in required_schemas:
        missing = set(required_schemas[entity_type]) - set(data.keys())
        if missing:
            violations.append({
                'file': str(json_file),
                'type': entity_type,
                'missing_fields': list(missing)
            })

# Save violations
with open('schema_violations.json', 'w') as f:
    json.dump(violations, f, indent=2)
```

#### Step 4: Document schema violations
- Create comprehensive schema validation report
- Categorize by entity type
- Provide field addition recommendations

### Checklist:
- [ ] Extract schemas by entity type
- [ ] Validate required fields
- [ ] Check field consistency
- [ ] Document all schema violations

---

## Task 3: Version Control Consistency

**Task ID:** TASK-TEMPLATE-ANALYSIS-006
**Estimated Hours:** 0.5

### Steps:

#### Step 1: Extract version fields
- Find all files with version or last_updated fields
- Extract version numbers and timestamps

**PowerShell Command:**
```powershell
$jsonFiles = Get-ChildItem -Path "C:\Users\Dell\Dropbox\ENTITIES" -Filter "*.json" -Recurse
$versions = @()

foreach ($file in $jsonFiles) {
    $content = Get-Content $file.FullName | ConvertFrom-Json

    if ($content.version -or $content.last_updated) {
        $versions += [PSCustomObject]@{
            File = $file.FullName
            Version = $content.version
            LastUpdated = $content.last_updated
            CreatedDate = $content.created_date
        }
    }
}

$versions | Export-Csv -Path "version_inventory.csv" -NoTypeInformation
```

#### Step 2: Validate version formats
- Check version number formats (semantic versioning)
- Validate format consistency (1.0 vs 1.0.0 vs v1.0)

**Valid Formats:**
- Semantic: `1.0.0`, `2.1.3`
- Simple: `1.0`, `2.5`
- Invalid: `v1`, `version 1.0`, `1`

#### Step 3: Check update timestamps
- Validate date formats
- Check for missing timestamps
- Identify files with outdated versions

**Expected Date Formats:**
- ISO 8601: `2025-11-17`
- Timestamp: `2025-11-17T10:30:00Z`

### Checklist:
- [ ] Extract all version fields
- [ ] Validate version number formats
- [ ] Check timestamp consistency
- [ ] Document inconsistencies

---

## Expected Reports

1. **REP-002: Naming Convention Audit**
   - Location: `ANALYTICS/REPORTS/System_Analysis/`
   - Format: Markdown + CSV
   - Contains: Violations list, recommendations

2. **REP-003: Schema Validation Report**
   - Location: `ANALYTICS/REPORTS/System_Analysis/`
   - Format: JSON + Markdown
   - Contains: Missing fields, schema violations, remediation steps

---

## Success Criteria

- [ ] All naming patterns documented
- [ ] Naming violations identified and categorized
- [ ] JSON schemas extracted for all entity types
- [ ] Required fields validated across all entities
- [ ] Version formats standardized
- [ ] Reports generated and saved
- [ ] Remediation recommendations provided

---

## Notes

- This milestone can run in parallel with Milestone 1 and 3
- Focus on structural consistency rather than content
- Document edge cases and exceptions
- Prioritize critical violations over warnings
