import os
import json
import re
from collections import defaultdict
from datetime import datetime

# Configuration
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_FILE = os.path.join(ROOT_DIR, "analysis_report.md")
TAXONOMY_MAP_FILE = os.path.join(ROOT_DIR, "TAXONOMY/TASK_MANAGERS__Taxonomy/Taxonomy_Migration_Map.json")

# Global stores
entities = {}  # id -> {type, path, data}
files_scanned = 0
errors = []
warnings = []
schema_violations = []
missing_references = []
taxonomy_violations = []

# Taxonomy Data
taxonomy_data = {}

def log_error(path, msg):
    errors.append(f"- **Error** in `{os.path.relpath(path, ROOT_DIR)}`: {msg}")

def log_warning(path, msg):
    warnings.append(f"- **Warning** in `{os.path.relpath(path, ROOT_DIR)}`: {msg}")

def log_taxonomy_violation(path, msg):
    taxonomy_violations.append(f"- **Taxonomy Violation** in `{os.path.relpath(path, ROOT_DIR)}`: {msg}")

def load_json_file(path):
    try:
        # Use utf-8-sig to handle BOM
        with open(path, 'r', encoding='utf-8-sig') as f:
            return json.load(f)
    except UnicodeDecodeError:
        try:
            with open(path, 'r', encoding='cp1252') as f:
                return json.load(f)
        except UnicodeDecodeError:
            try:
                # Fallback to latin-1 which reads bytes as-is
                with open(path, 'r', encoding='latin-1') as f:
                    return json.load(f)
            except Exception as e:
                log_error(path, f"Encoding error (tried utf-8-sig, cp1252, latin-1): {e}")
                return None
    except json.JSONDecodeError as e:
        log_error(path, f"Invalid JSON: {e}")
        return None
    except Exception as e:
        log_error(path, f"Could not read file: {e}")
        return None

def load_taxonomy_rules():
    global taxonomy_data
    if os.path.exists(TAXONOMY_MAP_FILE):
        data = load_json_file(TAXONOMY_MAP_FILE)
        if data:
            taxonomy_data = data
            print(f"Loaded taxonomy rules from {TAXONOMY_MAP_FILE}")
        else:
            print(f"Failed to load taxonomy rules from {TAXONOMY_MAP_FILE}")
    else:
        print(f"Taxonomy file not found: {TAXONOMY_MAP_FILE}")

def validate_id_format(entity_id, path):
    if not taxonomy_data:
        return

    # Check if ID matches the general pattern (3 letters - numbers)
    # e.g. PRT-001, TST-050
    if not isinstance(entity_id, str):
        entity_id = str(entity_id)
        
    match = re.match(r"^([A-Z]{3})-([A-Z0-9]+)(?:_.*)?$", entity_id)
    if match:
        prefix = match.group(1)
        
        # Check if prefix is in allowed codes
        allowed_codes = taxonomy_data.get("entity_type_iso_codes", {}).get("codes", {}).values()
        if prefix not in allowed_codes:
            # It might be a LIBRARIES ID (RSP, ACT, etc.) which are not in this specific map
            # So we only strictly validate if it LOOKS like a TASK_MANAGERS ID or if we want to be strict about all
            # For now, let's check if it's a known prefix in the map
            pass
    
    # Check against specific migration maps
    # The map has "project_templates": { "PRT-001": "PRT-001_..." }
    # We want to see if the current ID is a key in any of these maps
    
    # Reverse lookup: Check if the ID is a legacy ID that should be migrated
    # The map structure is: "project_templates": { "PRT-001": "PRT-001_..." }
    # This maps Short ID -> Long ID. 
    # If the entity_id is "Task-Template-001", we need to see if it's a valid legacy ID.
    # But the map provided seems to map NEW Short IDs to NEW Long IDs.
    # Wait, looking at the file content:
    # "task_templates": { "TST-001": "TST-001_AI_Powered_HTML_Parsing", ... }
    # This looks like a registry of valid IDs.
    
    # If the ID is something like "Task-Template-001", it is NOT in the map keys.
    # We should flag IDs that do not follow the 3-letter code format if they are in TASK_MANAGERS.
    
    if "TASK_MANAGERS" in path:
        if not re.match(r"^[A-Z]{3}-[0-9]+.*$", entity_id):
             # Exception for some legacy IDs if needed, but user wants compliance
             # Check if it looks like "Task-Template-..."
             if "Template" in entity_id:
                 log_taxonomy_violation(path, f"ID `{entity_id}` does not follow ISO format (e.g., TST-001).")

def scan_directory(directory):
    global files_scanned
    for root, dirs, files in os.walk(directory):
        # Skip hidden directories and backup folders
        dirs[:] = [d for d in dirs if not d.startswith('.') and "backup" not in d.lower() and "archive" not in d.lower()]
        
        for file in files:
            if file.endswith(".json") and not file.endswith("_schema.json") and not file.endswith("_report.json"):
                path = os.path.join(root, file)
                files_scanned += 1
                data = load_json_file(path)
                
                if data:
                    # Handle list of entities or single entity
                    items_to_process = []
                    if isinstance(data, list):
                        # If it's a list, treat each item as a potential entity if it's a dict
                        for item in data:
                            if isinstance(item, dict):
                                items_to_process.append(item)
                    elif isinstance(data, dict):
                        items_to_process.append(data)
                    
                    for item_data in items_to_process:
                        # Index entity by ID if possible
                        # Heuristic: find field that looks like a primary key (often matches filename without ext)
                        filename_no_ext = os.path.splitext(file)[0]
                        
                        # specific check for ACCOUNTS and other types
                        primary_id = None
                        
                        # List of potential ID fields in order of preference
                        id_fields = [
                            "tool_id", 
                            "verification_id",
                            "candidate_id", 
                            "responsibility_id",
                            "task_id",
                            "milestone_id",
                            "project_id",
                            "account_id",
                            "entity_id", 
                            "id"
                        ]
                        
                        for field in id_fields:
                            if field in item_data and item_data[field]:
                                primary_id = item_data[field]
                                break
                        
                        # Fallback: check if any value matches filename (only for single-object files)
                        if not primary_id and isinstance(data, dict):
                            for k, v in item_data.items():
                                if isinstance(v, str) and v == filename_no_ext:
                                    primary_id = v
                                    break
                        
                        if primary_id:
                            if primary_id in entities:
                                log_error(path, f"Duplicate ID found: `{primary_id}`. Also in `{os.path.relpath(entities[primary_id]['path'], ROOT_DIR)}`")
                            else:
                                entities[primary_id] = {
                                    "path": path,
                                    "data": item_data,
                                    "type": item_data.get("entity_type", "UNKNOWN")
                                }
                                
                            # Consistency check: filename should match ID (only if file contains single entity)
                            if isinstance(data, dict) and primary_id != filename_no_ext:
                                log_warning(path, f"Filename `{file}` does not match ID `{primary_id}`")
                            
                            # Taxonomy Validation
                            validate_id_format(primary_id, path)
                            
                        else:
                            # Only warn if it's a dict (single entity file) and we couldn't find ID
                            if isinstance(data, dict):
                                log_warning(path, "Could not identify a primary ID for this file.")

def check_references():
    for entity_id, info in entities.items():
        data = info["data"]
        path = info["path"]
        
        # Recursive function to find keys ending in _id
        def check_dict_references(d, context=""):
            for k, v in d.items():
                if isinstance(v, dict):
                    check_dict_references(v, f"{context}.{k}" if context else k)
                elif isinstance(v, list):
                    for i, item in enumerate(v):
                        if isinstance(item, dict):
                            check_dict_references(item, f"{context}.{k}[{i}]" if context else f"{k}[{i}]")
                        elif isinstance(item, str) and (k.endswith("_id") or k == "id"):
                             validate_reference(path, k, item, f"{context}.{k}[{i}]" if context else f"{k}[{i}]")
                elif isinstance(v, str):
                    if k.endswith("_id") or k == "id":
                        # Skip self-references (like account_id in the account file)
                        if v == entity_id:
                            continue
                        # Skip some common non-reference IDs if necessary, or refine logic
                        # For now, assume anything ending in _id is a ref
                        validate_reference(path, k, v, f"{context}.{k}" if context else k)

        check_dict_references(data)

def validate_reference(source_path, field, target_id, context):
    # Ignore some specific fields that might not be direct FKs or are external
    if field in ["inner_client_id", "login"]: 
        return

    # If target_id is null or empty, skip
    if not target_id:
        return

    # Check if target_id exists in our index
    if target_id not in entities:
        # Heuristic: maybe it's a reference to a file we haven't scanned or an external system?
        # For this report, we'll flag it as missing reference
        missing_references.append(f"- `{os.path.relpath(source_path, ROOT_DIR)}`: Field `{context}` references missing ID `{target_id}`")

def generate_report():
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(f"# ENTITIES Data Structure Analysis Report\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Files Scanned:** {files_scanned}\n")
        f.write(f"**Entities Found:** {len(entities)}\n\n")
        
        f.write("## 1. Structural & Consistency Checks\n")
        if errors:
            f.write("### Errors\n")
            for e in errors:
                f.write(f"{e}\n")
        else:
            f.write("No structural errors found.\n")
            
        if warnings:
            f.write("\n### Warnings\n")
            for w in warnings:
                f.write(f"{w}\n")
        else:
            f.write("\nNo structural warnings found.\n")

        f.write("\n## 2. Taxonomy Validation\n")
        if taxonomy_violations:
            f.write("### Violations\n")
            for v in taxonomy_violations:
                f.write(f"{v}\n")
        else:
            f.write("No taxonomy violations found.\n")

        f.write("\n## 3. Referential Integrity\n")
        if missing_references:
            f.write(f"Found {len(missing_references)} missing references:\n")
            # Limit output if too many
            for i, ref in enumerate(missing_references):
                if i >= 50:
                    f.write(f"- ... and {len(missing_references) - 50} more\n")
                    break
                f.write(f"{ref}\n")
        else:
            f.write("All references appear valid (within the scanned scope).\n")

        f.write("\n## 4. Schema Analysis\n")
        f.write("*(Note: Full JSON schema validation requires `jsonschema` library. This analysis focused on structural consistency and references.)*\n")
        
        # Add some stats
        type_counts = defaultdict(int)
        for e in entities.values():
            type_counts[e['type']] += 1
            
        f.write("\n### Entity Distribution\n")
        f.write("| Entity Type | Count |\n")
        f.write("|---|---|\n")
        for t, c in type_counts.items():
            f.write(f"| {t} | {c} |\n")

if __name__ == "__main__":
    print("Starting analysis...")
    load_taxonomy_rules()
    scan_directory(ROOT_DIR)
    check_references()
    generate_report()
    print(f"Analysis complete. Report generated at {REPORT_FILE}")
