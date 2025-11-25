# PMT-079: Prompt Taxonomy Sync v1.0

**Prompt ID:** PMT-079
**Version:** 1.0
**Department:** System Architecture
**Category:** PROMPT_MAINTENANCE
**Date:** 2025-11-21
**Status:** Active
**Parent Prompt:** PMT-074 (Data Architect Master)

---

## Purpose

Automated synchronization and update system for prompts. Finds outdated references, updates entity paths/IDs, extracts entities from prompt outputs, and maintains consistency across 73+ prompts.

**Core Functions:**
1. **Find Outdated References**: Scan all prompts for deprecated paths/IDs
2. **Auto-Update**: Replace old references with current ones
3. **Extract Entities**: Mine prompt outputs for new taxonomy entities
4. **Version Migration**: Update prompts when taxonomy structure changes
5. **Cross-Reference Validation**: Ensure all entity references valid
6. **Batch Updates**: Update multiple prompts efficiently

---

## Problem Statement

**Current Issues:**
- Prompts reference old paths (e.g., `LIBRARIES/actions.json` → `LIBRARIES/Actions/actions_master.json`)
- Entity IDs change during migrations (TOL-089 merged into TOL-042)
- New entities added but prompts not updated
- Manual updates time-consuming and error-prone

**Solution:** Automated sync system that maintains prompt-taxonomy consistency

---

## Operation 1: Find Outdated References

### Scan All Prompts

```python
def scan_prompts_for_outdated_refs():
    """
    Scan all 73+ prompts for outdated references
    """
    from pathlib import Path
    import re

    prompts_root = Path("PROMPTS")
    all_prompts = list(prompts_root.rglob("PMT-*.md"))

    # Load migration history
    migrations = load_migration_history()

    outdated_refs = []

    for prompt_file in all_prompts:
        content = prompt_file.read_text()

        # Check for old file paths
        old_paths = [
            "LIBRARIES/actions.json",
            "LIBRARIES/objects.json",
            "LIBRARIES/tools.json",
            "LIBRARIES/responsibilities.json",
            "TASK_MANAGERS/Project_Templates/",  # Missing TSM-001
            "TASK_MANAGERS/Task_Templates/"      # Missing TSM-003
        ]

        for old_path in old_paths:
            if old_path in content:
                new_path = get_current_path(old_path, migrations)
                outdated_refs.append({
                    "prompt_file": str(prompt_file),
                    "prompt_id": extract_prompt_id(prompt_file.name),
                    "issue_type": "outdated_path",
                    "old_value": old_path,
                    "new_value": new_path,
                    "occurrences": content.count(old_path)
                })

        # Check for deprecated entity IDs
        deprecated_ids = get_deprecated_ids(migrations)

        for old_id, new_id in deprecated_ids.items():
            if old_id in content:
                outdated_refs.append({
                    "prompt_file": str(prompt_file),
                    "prompt_id": extract_prompt_id(prompt_file.name),
                    "issue_type": "deprecated_id",
                    "old_value": old_id,
                    "new_value": new_id,
                    "occurrences": content.count(old_id)
                })

    return outdated_refs

def get_current_path(old_path, migrations):
    """Map old path to current path using migration history"""
    path_mappings = {
        "LIBRARIES/actions.json": "LIBRARIES/Actions/actions_master.json",
        "LIBRARIES/objects.json": "LIBRARIES/Objects/objects_master.json",
        "LIBRARIES/tools.json": "LIBRARIES/Tools/Tools_Master_List.csv",
        "LIBRARIES/responsibilities.json": "LIBRARIES/Responsibilities/responsibilities_master.json",
        "TASK_MANAGERS/Project_Templates/": "TASK_MANAGERS/TSM-001_Project_Templates/",
        "TASK_MANAGERS/Task_Templates/": "TASK_MANAGERS/TSM-003_Task_Templates/"
    }
    return path_mappings.get(old_path, old_path)

def get_deprecated_ids(migrations):
    """Get mapping of deprecated IDs to current IDs"""
    return {
        "TOL-089": "TOL-042",  # Claude merged
        "TOL-067": "TOL-015",  # n8n merged
        "ACT-089": "ACT-012",  # Extract/Pull Out merged
        # Load from migrations log
    }
```

**Output Report:**
```markdown
## Outdated References Report

**Date**: 2025-11-21
**Prompts Scanned**: 73
**Issues Found**: 18

### Critical Issues (Broken References):

1. **PMT-070**: Daily_Report_Entity_Mapping_v2.1
   - **Issue**: Outdated path
   - Old: `LIBRARIES/actions.json`
   - New: `LIBRARIES/Actions/actions_master.json`
   - Occurrences: 3
   - **Action**: Auto-update recommended

2. **PMT-002**: Main_Prompt_v6_DRAFT
   - **Issue**: Outdated path
   - Old: `TASK_MANAGERS/Task_Templates/`
   - New: `TASK_MANAGERS/TSM-003_Task_Templates/`
   - Occurrences: 5
   - **Action**: Auto-update recommended

3. **PMT-062**: Tools_Collection_Matching
   - **Issue**: Deprecated ID
   - Old: `TOL-089` (Claude, deprecated)
   - New: `TOL-042` (Claude AI, merged)
   - Occurrences: 2
   - **Action**: Auto-update with validation

### Summary:
- **Outdated Paths**: 12 prompts affected
- **Deprecated IDs**: 6 prompts affected
- **Total Fixes Needed**: 45 replacements
- **Estimated Fix Time**: 15 minutes (automated)
```

---

## Operation 2: Auto-Update Prompts

### Batch Update System

```python
def auto_update_prompts(outdated_refs, dry_run=True):
    """
    Automatically update prompts with current references

    Args:
        outdated_refs: List from scan_prompts_for_outdated_refs()
        dry_run: If True, preview changes without applying

    Returns:
        Update summary
    """
    updates_applied = []

    for ref in outdated_refs:
        prompt_file = Path(ref['prompt_file'])

        if not prompt_file.exists():
            continue

        # Read current content
        content = prompt_file.read_text()

        # Apply replacement
        updated_content = content.replace(ref['old_value'], ref['new_value'])

        if not dry_run:
            # Backup original
            backup_file = prompt_file.with_suffix('.md.bak')
            prompt_file.rename(backup_file)

            # Write updated content
            prompt_file.write_text(updated_content)

            updates_applied.append({
                "prompt_id": ref['prompt_id'],
                "file": str(prompt_file),
                "replacements": ref['occurrences'],
                "backup": str(backup_file)
            })
        else:
            # Dry run: preview only
            updates_applied.append({
                "prompt_id": ref['prompt_id'],
                "file": str(prompt_file),
                "replacements": ref['occurrences'],
                "preview": True
            })

    return {
        "total_prompts_updated": len(set(u['prompt_id'] for u in updates_applied)),
        "total_replacements": sum(u['replacements'] for u in updates_applied),
        "dry_run": dry_run,
        "updates": updates_applied
    }

# Usage
# Step 1: Preview (dry run)
preview = auto_update_prompts(outdated_refs, dry_run=True)

# Step 2: Apply updates
result = auto_update_prompts(outdated_refs, dry_run=False)
```

**Update Report:**
```markdown
## Auto-Update Execution Report

**Date**: 2025-11-21 15:30:00
**Mode**: Live Update (dry_run=False)

### Updates Applied:

1. **PMT-070**: Daily_Report_Entity_Mapping_v2.1
   - Replacements: 3
   - `LIBRARIES/actions.json` → `LIBRARIES/Actions/actions_master.json`
   - Backup: PMT-070_Daily_Report_Entity_Mapping_v2.1.md.bak
   - Status: ✅ Success

2. **PMT-002**: Main_Prompt_v6_DRAFT
   - Replacements: 5
   - `TASK_MANAGERS/Task_Templates/` → `TASK_MANAGERS/TSM-003_Task_Templates/`
   - Backup: PMT-002_Main_Prompt_v6_DRAFT.md.bak
   - Status: ✅ Success

[...18 prompts total]

### Summary:
- ✅ Prompts Updated: 18
- ✅ Total Replacements: 45
- ✅ Backups Created: 18
- ⏱️  Execution Time: 2.3 seconds

### Validation:
- Run PMT-075 (Data Integrity) to verify references
- Test updated prompts for functionality
- Archive backups after 7 days if no issues
```

---

## Operation 3: Extract Entities from Prompt Outputs

### Mine Prompt Results

```python
def extract_entities_from_prompt_output(prompt_id, output_text):
    """
    Analyze prompt output to discover new entities

    Example: PMT-048 (YouTube_AI_Tools_Daily) generates list of AI tools
    → Extract tool names, URLs, descriptions
    → Stage for import via PMT-076
    """
    import re

    discovered_entities = {
        "tools": [],
        "actions": [],
        "responsibilities": [],
        "tasks": []
    }

    # Pattern 1: Tool mentions
    # "I used Perplexity AI for research"
    # "Testing with Gemini Flash 2.0"
    tool_pattern = r'(?:used|using|tested|testing|with|via)\s+([A-Z][A-Za-z0-9\s\.]+?)(?:\s+for|\s+to|\.|\,)'
    tool_matches = re.findall(tool_pattern, output_text)

    for tool in tool_matches:
        tool_clean = tool.strip()
        if len(tool_clean) > 3 and not is_common_word(tool_clean):
            discovered_entities["tools"].append({
                "name": tool_clean,
                "source_prompt": prompt_id,
                "context": get_context_sentence(output_text, tool_clean),
                "confidence": "medium"
            })

    # Pattern 2: Action verbs
    action_pattern = r'\b(analyze|extract|create|build|generate|configure|setup|review)\b'
    action_matches = re.findall(action_pattern, output_text, re.IGNORECASE)

    for action in set(action_matches):
        discovered_entities["actions"].append({
            "action": action.lower(),
            "source_prompt": prompt_id,
            "category": classify_action(action)
        })

    # Pattern 3: Responsibilities (action + object)
    # "Extract video metadata", "Create automation workflow"
    resp_pattern = r'\b([A-Z][a-z]+)\s+([a-z]+\s+[a-z]+)'
    resp_matches = re.findall(resp_pattern, output_text)

    for action, obj in resp_matches:
        discovered_entities["responsibilities"].append({
            "responsibility": f"{action} {obj}",
            "action": action.lower(),
            "object": obj,
            "source_prompt": prompt_id
        })

    return discovered_entities

def continuous_entity_extraction():
    """
    Monitor prompt usage and extract entities automatically
    """
    # Monitor REPORTS/ folder for new prompt outputs
    # Run extraction on new reports
    # Stage discovered entities for validation
    pass
```

**Extraction Report:**
```markdown
## Entity Extraction from Prompt Outputs

**Period**: 2025-11-15 to 2025-11-21
**Prompts Monitored**: 15 (high-activity prompts)

### New Entities Discovered:

**Tools (8)**:
1. Perplexity AI (mentioned 5x in PMT-048 outputs)
2. Gemini Flash 2.0 (mentioned 3x in PMT-002, PMT-070)
3. Claude Code (mentioned 4x in PMT-052)
... [8 total]

**Actions (3)**:
1. "Synthesize" (mentioned 4x, Category C)
2. "Orchestrate" (mentioned 2x, Category F)
... [3 total]

**Responsibilities (12)**:
1. "Extract video timestamps" (5x)
2. "Synthesize research findings" (4x)
... [12 total]

### Recommended Actions:
1. **High Confidence (≥4 mentions)**: Auto-stage for import
2. **Medium Confidence (2-3 mentions)**: Manual review
3. **Low Confidence (1 mention)**: Monitor for additional occurrences

### Auto-Staged for Import:
- Perplexity AI → TOL-178 (assign via PMT-076)
- "Synthesize" → ACT-430 (validate not duplicate of "Combine")
```

---

## Operation 4: Version Migration

### Migrate Prompts to New Taxonomy

```python
def migrate_prompts_to_new_structure(migration_spec):
    """
    Update prompts when taxonomy structure changes

    Example migration:
    - LIBRARIES restructure (2025-11-17)
    - All prompts referencing LIBRARIES/ need updates

    Args:
        migration_spec: {
            "migration_name": "LIBRARIES_Restructure_2025-11-17",
            "mappings": {
                "LIBRARIES/actions.json": "LIBRARIES/Actions/actions_master.json",
                ...
            },
            "affected_prompts": ["PMT-002", "PMT-070", ...]
        }
    """
    results = []

    for prompt_id in migration_spec['affected_prompts']:
        prompt_file = find_prompt_file(prompt_id)

        content = prompt_file.read_text()

        # Apply all mappings
        updated_content = content
        changes = []

        for old_ref, new_ref in migration_spec['mappings'].items():
            if old_ref in updated_content:
                updated_content = updated_content.replace(old_ref, new_ref)
                changes.append({
                    "old": old_ref,
                    "new": new_ref,
                    "occurrences": content.count(old_ref)
                })

        if changes:
            # Backup and update
            backup_prompt(prompt_file, migration_spec['migration_name'])
            prompt_file.write_text(updated_content)

            results.append({
                "prompt_id": prompt_id,
                "changes": changes,
                "status": "updated"
            })

    # Generate migration report
    generate_migration_report(migration_spec, results)

    return results
```

---

## Operation 5: Cross-Reference Validation

### Validate All Entity References

```python
def validate_prompt_references():
    """
    Check that all entity IDs referenced in prompts exist
    """
    from pathlib import Path

    all_prompts = list(Path("PROMPTS").rglob("PMT-*.md"))

    # Load all entity IDs
    valid_ids = load_all_entity_ids()

    broken_refs = []

    for prompt_file in all_prompts:
        content = prompt_file.read_text()

        # Extract all entity IDs (TOL-###, TSK-###, etc.)
        import re
        id_pattern = r'\b([A-Z]{3}-\d{3})\b'
        found_ids = re.findall(id_pattern, content)

        for entity_id in set(found_ids):
            if entity_id not in valid_ids:
                broken_refs.append({
                    "prompt": prompt_file.name,
                    "broken_id": entity_id,
                    "suggestion": find_similar_id(entity_id, valid_ids)
                })

    return broken_refs
```

---

## Automated Workflows

### Weekly Sync Workflow

```bash
#!/bin/bash
# weekly_prompt_sync.sh

echo "=== Weekly Prompt Sync ==="
date

# Step 1: Scan for outdated references
python sync/scan_prompts.py > reports/scan_$(date +%Y%m%d).md

# Step 2: Validate references
python sync/validate_references.py > reports/validation_$(date +%Y%m%d).md

# Step 3: Extract entities from recent outputs
python sync/extract_entities.py --days 7 > reports/extraction_$(date +%Y%m%d).md

# Step 4: Generate update recommendations
python sync/recommend_updates.py

echo "✅ Sync complete. Review reports/ folder."
```

### Post-Migration Sync

```python
def post_migration_sync(migration_date):
    """
    Run after major taxonomy migrations
    """
    # 1. Scan all prompts
    outdated = scan_prompts_for_outdated_refs()

    # 2. Auto-update (dry run first)
    preview = auto_update_prompts(outdated, dry_run=True)
    print(f"Preview: {preview['total_replacements']} replacements needed")

    # 3. Confirm and execute
    confirm = input("Apply updates? (y/n): ")
    if confirm.lower() == 'y':
        result = auto_update_prompts(outdated, dry_run=False)
        print(f"✅ Updated {result['total_prompts_updated']} prompts")

    # 4. Validate
    broken = validate_prompt_references()
    if broken:
        print(f"⚠️  Found {len(broken)} broken references")
    else:
        print("✅ All references valid")

    # 5. Generate report
    generate_sync_report(migration_date, result, broken)
```

---

## Best Practices

### DO:
- ✅ Run weekly scans for outdated references
- ✅ Always dry-run before batch updates
- ✅ Backup prompts before auto-update
- ✅ Validate references after migrations
- ✅ Extract entities from high-activity prompts
- ✅ Document all migrations in migration log

### DON'T:
- ❌ Skip validation after updates
- ❌ Update prompts manually (use automation)
- ❌ Delete backups immediately (keep 7 days)
- ❌ Ignore low-confidence entity extractions (track for patterns)

---

## Integration

**PMT-075**: Validate extracted entities before import
**PMT-076**: Stage extracted entities for integration
**PMT-078**: Search for entity references across prompts

---

## Version History

**v1.0** (2025-11-21)
- Scan prompts for outdated references
- Auto-update batch system
- Entity extraction from outputs
- Version migration support
- Cross-reference validation
- Weekly sync workflow

---

**Status:** Active

---

**End of Prompt**
