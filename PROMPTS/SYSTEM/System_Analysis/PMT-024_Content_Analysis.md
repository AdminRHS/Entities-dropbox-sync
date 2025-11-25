# Milestone 3: Content Analysis

**Milestone ID:** MIL-TEMPL-003
**Phase:** 3
**Can Run Parallel:** Yes
**Dependencies:** None
**Estimated Hours:** 4.0

---

## Objective

Detect duplicate content between JSON and Markdown files, extract comprehensive terminology from all sources, and assess documentation completeness.

---

## Tasks Overview

This milestone consists of 3 tasks:

1. **TASK-TEMPLATE-ANALYSIS-007:** Duplicate Content Detection (1.5 hours)
2. **TASK-TEMPLATE-ANALYSIS-008:** Terminology Extraction (2.0 hours) - **KEY TASK**
3. **TASK-TEMPLATE-ANALYSIS-009:** Documentation Completeness (0.5 hours)

---

## Task 1: Duplicate Content Detection

**Task ID:** TASK-TEMPLATE-ANALYSIS-007
**Estimated Hours:** 1.5

### Steps:

#### Step 1: Hash all file contents
- Create content hashes for all files
- Use MD5 for quick comparison
- Store hashes with file metadata

**PowerShell Script:**
```powershell
$files = Get-ChildItem -Path "C:\Users\Dell\Dropbox\ENTITIES" -Recurse -File
$hashes = @()

foreach ($file in $files) {
    $hash = Get-FileHash -Path $file.FullName -Algorithm MD5
    $hashes += [PSCustomObject]@{
        File = $file.FullName
        Name = $file.Name
        Extension = $file.Extension
        Hash = $hash.Hash
        Size = $file.Length
    }
}

$hashes | Export-Csv -Path "C:\Users\Dell\Dropbox\ENTITIES\ANALYTICS\REPORTS\System_Analysis\file_hashes.csv" -NoTypeInformation
```

#### Step 2: Compare JSON vs Markdown
- Find JSON files with corresponding Markdown files
- Extract content from both formats
- Compare for duplicate information

**Python Script:**
```python
import json
import hashlib
from pathlib import Path

duplicates = []

json_files = list(Path('C:/Users/Dell/Dropbox/ENTITIES').rglob('*.json'))
md_files = list(Path('C:/Users/Dell/Dropbox/ENTITIES').rglob('*.md'))

for json_file in json_files:
    # Find matching markdown file
    md_counterpart = json_file.with_suffix('.md')

    if md_counterpart in md_files:
        # Read both files
        with open(json_file) as f:
            json_content = json.load(f)

        with open(md_counterpart) as f:
            md_content = f.read()

        # Check if JSON content appears in MD
        json_str = json.dumps(json_content, indent=2)

        if json_str in md_content or str(json_content) in md_content:
            duplicates.append({
                'json_file': str(json_file),
                'md_file': str(md_counterpart),
                'type': 'exact_duplicate'
            })

# Save results
with open('duplicate_content.json', 'w') as f:
    json.dump(duplicates, f, indent=2)
```

#### Step 3: Identify partial duplicates
- Use fuzzy matching to find similar content
- Calculate similarity scores
- Flag potential redundancies

**Python with difflib:**
```python
from difflib import SequenceMatcher
import json

def similarity_score(text1, text2):
    return SequenceMatcher(None, text1, text2).ratio()

partial_duplicates = []

# Compare all JSON files with all MD files
for json_file in json_files:
    with open(json_file) as f:
        json_text = json.dumps(json.load(f))

    for md_file in md_files:
        with open(md_file) as f:
            md_text = f.read()

        score = similarity_score(json_text, md_text)

        if score > 0.7:  # 70% similarity threshold
            partial_duplicates.append({
                'json': str(json_file),
                'markdown': str(md_file),
                'similarity': score
            })

# Save results
with open('partial_duplicates.json', 'w') as f:
    json.dump(partial_duplicates, f, indent=2)
```

#### Step 4: Generate duplicate report
- Create comprehensive duplicate content report
- Categorize by duplication type
- Provide deduplication recommendations

**Report Structure:**
```markdown
# Duplicate Content Report

## Exact Duplicates
- [List of exact matches between JSON and MD]

## Partial Duplicates (>70% similarity)
- [List with similarity scores]

## Recommendations
- Consolidate: [files to merge]
- Remove: [redundant files]
- Convert: [JSON-only or MD-only]
```

### Checklist:
- [ ] Hash all file contents
- [ ] Compare JSON vs Markdown files
- [ ] Identify partial duplicates
- [ ] Generate duplicate report with recommendations

---

## Task 2: Terminology Extraction (KEY TASK)

**Task ID:** TASK-TEMPLATE-ANALYSIS-008
**Estimated Hours:** 2.0

### Steps:

#### Step 1: Extract JSON field names
- Parse all JSON files
- Extract all unique field names
- Track frequency and locations

**Python Script:**
```python
import json
from pathlib import Path
from collections import Counter

field_names = Counter()
field_locations = {}

def extract_fields(obj, parent=''):
    """Recursively extract field names from JSON object"""
    if isinstance(obj, dict):
        for key, value in obj.items():
            full_key = f"{parent}.{key}" if parent else key
            field_names[key] += 1

            if key not in field_locations:
                field_locations[key] = []

            extract_fields(value, full_key)

    elif isinstance(obj, list):
        for item in obj:
            extract_fields(item, parent)

# Process all JSON files
for json_file in Path('C:/Users/Dell/Dropbox/ENTITIES').rglob('*.json'):
    try:
        with open(json_file) as f:
            data = json.load(f)
            field_locations[str(json_file)] = []
            extract_fields(data)
    except:
        pass

# Save results
with open('json_field_names.json', 'w') as f:
    json.dump({
        'field_counts': dict(field_names.most_common()),
        'total_unique_fields': len(field_names)
    }, f, indent=2)
```

**Expected Output:**
- Complete list of all JSON field names
- Frequency counts
- Field hierarchy (nested fields)

#### Step 2: Extract Markdown headings
- Parse all Markdown files
- Extract all heading levels (H1-H6)
- Categorize by heading level

**Python Script:**
```python
import re
from pathlib import Path

headings = {
    'h1': [],
    'h2': [],
    'h3': [],
    'h4': [],
    'h5': [],
    'h6': []
}

heading_pattern = r'^(#{1,6})\s+(.+)$'

for md_file in Path('C:/Users/Dell/Dropbox/ENTITIES').rglob('*.md'):
    with open(md_file, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(heading_pattern, line)
            if match:
                level = len(match.group(1))
                text = match.group(2).strip()
                headings[f'h{level}'].append({
                    'file': str(md_file),
                    'text': text
                })

# Save results
with open('markdown_headings.json', 'w') as f:
    json.dump(headings, f, indent=2)
```

#### Step 3: Extract entity names from filenames
- Parse all file and folder names
- Extract entity identifiers and names
- Build entity name dictionary

**PowerShell Script:**
```powershell
$entities = Get-ChildItem -Path "C:\Users\Dell\Dropbox\ENTITIES" -Recurse |
  Select-Object Name, DirectoryName, Extension |
  ForEach-Object {
    [PSCustomObject]@{
        FullName = $_.Name
        BaseName = [System.IO.Path]::GetFileNameWithoutExtension($_.Name)
        Extension = $_.Extension
        ParentFolder = Split-Path $_.DirectoryName -Leaf
    }
  }

$entities | Export-Csv -Path "entity_names.csv" -NoTypeInformation
```

**Python Processing:**
```python
import pandas as pd
import re

# Load entity names
df = pd.read_csv('entity_names.csv')

# Extract patterns
patterns = {
    'Action IDs': r'ACTION-\d{3}',
    'Product IDs': r'PDT-\d{4}',
    'Step IDs': r'STEP-[A-Z]+-\d{3}-\d{2}',
    'Project IDs': r'PROJ-\d{3}',
    'Task IDs': r'TASK-TEMPLATE-[A-Z]+-\d{3}',
    'Milestone IDs': r'MIL-TEMPL-\d{3}'
}

extracted_entities = {}

for pattern_name, pattern in patterns.items():
    matches = df['FullName'].str.extract(pattern, expand=False).dropna().unique()
    extracted_entities[pattern_name] = matches.tolist()

# Save results
with open('extracted_entities.json', 'w') as f:
    json.dump(extracted_entities, f, indent=2)
```

#### Step 4: Extract script variables
- Parse Python, PowerShell, and Batch scripts
- Extract variable names
- Categorize by script type

**Python Script Variable Extraction:**
```python
import ast
from pathlib import Path

python_variables = {}

for py_file in Path('C:/Users/Dell/Dropbox/ENTITIES').rglob('*.py'):
    try:
        with open(py_file) as f:
            tree = ast.parse(f.read())

        variables = set()

        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                variables.add(node.id)
            elif isinstance(node, ast.FunctionDef):
                variables.add(node.name)
            elif isinstance(node, ast.ClassDef):
                variables.add(node.name)

        python_variables[str(py_file)] = list(variables)

    except:
        pass

# Save results
with open('python_variables.json', 'w') as f:
    json.dump(python_variables, f, indent=2)
```

**PowerShell Variable Extraction:**
```powershell
$psFiles = Get-ChildItem -Path "C:\Users\Dell\Dropbox\ENTITIES" -Filter "*.ps1" -Recurse
$variables = @{}

foreach ($file in $psFiles) {
    $content = Get-Content $file.FullName -Raw
    $matches = [regex]::Matches($content, '\$([a-zA-Z_][a-zA-Z0-9_]*)')

    $vars = @()
    foreach ($match in $matches) {
        $vars += $match.Groups[1].Value
    }

    $variables[$file.FullName] = $vars | Select-Object -Unique
}

$variables | ConvertTo-Json -Depth 10 | Out-File "powershell_variables.json"
```

#### Step 5: Build terminology dictionary
- Merge all extracted terminology
- Identify redundant terms (synonyms, variations)
- Create standardized terminology dictionary

**Python Consolidation:**
```python
import json
from collections import Counter

# Load all extracted data
with open('json_field_names.json') as f:
    json_fields = json.load(f)

with open('markdown_headings.json') as f:
    md_headings = json.load(f)

with open('extracted_entities.json') as f:
    entities = json.load(f)

with open('python_variables.json') as f:
    py_vars = json.load(f)

with open('powershell_variables.json') as f:
    ps_vars = json.load(f)

# Build unified dictionary
terminology = {
    'json_fields': list(json_fields['field_counts'].keys()),
    'markdown_headings': [h['text'] for level in md_headings.values() for h in level],
    'entity_ids': {k: v for k, v in entities.items()},
    'script_variables': {
        'python': list(set([var for vars in py_vars.values() for var in vars])),
        'powershell': list(set([var for vars in ps_vars.values() for var in vars]))
    }
}

# Identify redundant terms
all_terms = (
    terminology['json_fields'] +
    terminology['markdown_headings'] +
    terminology['script_variables']['python'] +
    terminology['script_variables']['powershell']
)

# Find similar terms (case-insensitive, underscore vs camelCase)
term_variations = {}
for term in all_terms:
    normalized = term.lower().replace('_', '').replace('-', '')
    if normalized not in term_variations:
        term_variations[normalized] = []
    term_variations[normalized].append(term)

# Find redundant terms (multiple variations)
redundant_terms = {k: v for k, v in term_variations.items() if len(v) > 1}

# Save final dictionary
with open('terminology_dictionary.json', 'w') as f:
    json.dump({
        'terminology': terminology,
        'redundant_terms': redundant_terms,
        'total_unique_terms': len(set(all_terms)),
        'redundancy_count': len(redundant_terms)
    }, f, indent=2)
```

### Checklist:
- [ ] Extract all JSON field names
- [ ] Extract all Markdown headings
- [ ] Extract entity names from filenames
- [ ] Extract script variables (Python, PowerShell, Batch)
- [ ] Build consolidated terminology dictionary
- [ ] Identify redundant variables and synonyms

---

## Task 3: Documentation Completeness

**Task ID:** TASK-TEMPLATE-ANALYSIS-009
**Estimated Hours:** 0.5

### Steps:

#### Step 1: Check README files
- Find all README files across ENTITIES
- Assess completeness and quality

**PowerShell Command:**
```powershell
$readmeFiles = Get-ChildItem -Path "C:\Users\Dell\Dropbox\ENTITIES" -Filter "README.md" -Recurse

foreach ($readme in $readmeFiles) {
    $content = Get-Content $readme.FullName -Raw
    $wordCount = ($content -split '\s+').Count

    [PSCustomObject]@{
        File = $readme.FullName
        Exists = $true
        WordCount = $wordCount
        HasHeadings = ($content -match '^#')
        HasLinks = ($content -match '\[.*\]\(.*\)')
    }
} | Export-Csv -Path "readme_analysis.csv" -NoTypeInformation
```

#### Step 2: Verify description fields
- Check all JSON files for description fields
- Identify missing or empty descriptions

**Python Script:**
```python
import json
from pathlib import Path

missing_descriptions = []

for json_file in Path('C:/Users/Dell/Dropbox/ENTITIES').rglob('*.json'):
    try:
        with open(json_file) as f:
            data = json.load(f)

        if 'description' not in data or not data['description']:
            missing_descriptions.append({
                'file': str(json_file),
                'has_field': 'description' in data,
                'is_empty': 'description' in data and not data['description']
            })
    except:
        pass

# Save results
with open('missing_descriptions.json', 'w') as f:
    json.dump(missing_descriptions, f, indent=2)
```

#### Step 3: Identify undocumented entities
- Find entities without any documentation
- Create documentation gap report

**Expected Output:**
- List of entities without README
- List of JSON files without descriptions
- Priority list for documentation updates

### Checklist:
- [ ] Check all README files
- [ ] Verify description fields in JSON
- [ ] Identify undocumented entities
- [ ] Create documentation gap report

---

## Expected Reports

1. **REP-004: Duplicate Content Report**
   - Location: `ANALYTICS/REPORTS/System_Analysis/`
   - Format: JSON + Markdown
   - Contains: Exact duplicates, partial duplicates, deduplication recommendations

2. **REP-005: Terminology Extraction Report**
   - Location: `ANALYTICS/REPORTS/System_Analysis/`
   - Format: Markdown
   - Contains: Complete terminology analysis, redundancy findings

3. **REP-006: terminology_standards.json**
   - Location: `ANALYTICS/REPORTS/System_Analysis/`
   - Format: JSON
   - Contains: Standardized terminology dictionary, normalization rules

---

## Success Criteria

- [ ] All duplicate content identified
- [ ] Complete terminology dictionary created
- [ ] Redundant variables identified
- [ ] Documentation gaps documented
- [ ] All reports generated and saved
- [ ] Standardization recommendations provided

---

## Notes

- **Terminology extraction is the KEY deliverable** of this milestone
- Use this terminology to identify redundant variables across the ecosystem
- This milestone can run in parallel with Milestones 1 and 2
- Results feed into Milestone 5 (Terminology Consolidation)
