#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validation Script: Validate checklist_items references in Project Templates
Verifies that all checklist_item_ids referenced in templates exist in the Checklist Items listing.

Created: November 25, 2025
"""

import json
import sys
from pathlib import Path
from typing import Set, Dict, List, Any

# Fix Windows console encoding
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Base paths
BASE_DIR = Path(__file__).parent.parent
CHECKLIST_DIR = BASE_DIR / "Checklist_Items"
PROJECT_TEMPLATES_DIR = BASE_DIR / "Project_Templates"
PROJECT_INSTANCES_DIR = BASE_DIR

LISTING_FILE = CHECKLIST_DIR / "Listing.json"

PROJECT_TEMPLATES = [
    "Proj_Temp-HR-002.json",
    "Proj_Temp-AI-002.json",
    "Proj_Temp-DEV-001.json",
    "Proj_Temp-LG-001.json",
    "Proj_Temp-LG-002.json"
]

PROJECT_INSTANCES = [
    "PROJ-LIB-001_Responsibilities_Ecosystem/project_instance.json"
]


def load_json_file(file_path: Path) -> Dict[str, Any]:
    """Load JSON file, handling UTF-8 BOM if present."""
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        return json.load(f)


def get_all_checklist_item_ids(listing_data: Dict[str, Any]) -> Set[str]:
    """Extract all checklist_item_ids from the listing."""
    item_ids = set()
    for item in listing_data.get("items", []):
        item_id = item.get("checklist_item_id")
        if item_id:
            item_ids.add(item_id)
    return item_ids


def validate_project_template(template_file: str, valid_ids: Set[str]) -> Dict[str, Any]:
    """Validate checklist_items references in a project template."""
    template_path = PROJECT_TEMPLATES_DIR / template_file
    if not template_path.exists():
        return {"error": f"File not found: {template_file}"}
    
    template_data = load_json_file(template_path)
    template_id = template_data.get("template_id", "")
    
    results = {
        "template_id": template_id,
        "milestones_checked": 0,
        "references_found": 0,
        "invalid_references": [],
        "valid": True
    }
    
    milestones = template_data.get("milestones", [])
    for milestone in milestones:
        milestone_id = milestone.get("milestone_id", "")
        checklist_items = milestone.get("checklist_items", [])
        
        if not checklist_items:
            continue
        
        results["milestones_checked"] += 1
        
        for item_id in checklist_items:
            results["references_found"] += 1
            if item_id not in valid_ids:
                results["invalid_references"].append({
                    "milestone": milestone_id,
                    "checklist_item_id": item_id
                })
                results["valid"] = False
    
    return results


def validate_project_instance(instance_file: str, valid_ids: Set[str]) -> Dict[str, Any]:
    """Validate checklist_items references in a project instance."""
    instance_path = PROJECT_INSTANCES_DIR / instance_file
    if not instance_path.exists():
        return {"error": f"File not found: {instance_file}"}
    
    instance_data = load_json_file(instance_path)
    project_id = instance_data.get("project_id") or instance_data.get("template_id") or "PROJ-LIB-001"
    
    results = {
        "project_id": project_id,
        "references_found": 0,
        "invalid_references": [],
        "valid": True
    }
    
    checklist_items = instance_data.get("checklist_items", [])
    
    for item_id in checklist_items:
        results["references_found"] += 1
        if item_id not in valid_ids:
            results["invalid_references"].append(item_id)
            results["valid"] = False
    
    return results


def main():
    """Main validation function."""
    print("=" * 60)
    print("Validation: Checklist Items References")
    print("=" * 60)
    
    # Load checklist items listing
    if not LISTING_FILE.exists():
        print(f"Error: Listing file not found: {LISTING_FILE}")
        return
    
    listing_data = load_json_file(LISTING_FILE)
    valid_ids = get_all_checklist_item_ids(listing_data)
    print(f"\nLoaded {len(valid_ids)} valid checklist item IDs from Listing.json")
    
    # Validate project templates
    print("\n" + "-" * 60)
    print("Validating Project Templates")
    print("-" * 60)
    
    template_results = []
    for template_file in PROJECT_TEMPLATES:
        result = validate_project_template(template_file, valid_ids)
        if "error" not in result:
            template_results.append(result)
            status = "✅ Valid" if result["valid"] else "❌ Invalid"
            print(f"\n{template_file}: {status}")
            print(f"  Milestones checked: {result['milestones_checked']}")
            print(f"  References found: {result['references_found']}")
            if result["invalid_references"]:
                print(f"  Invalid references: {len(result['invalid_references'])}")
                for invalid in result["invalid_references"][:3]:  # Show first 3
                    print(f"    - {invalid['checklist_item_id']} in {invalid['milestone']}")
    
    # Validate project instances
    print("\n" + "-" * 60)
    print("Validating Project Instances")
    print("-" * 60)
    
    instance_results = []
    for instance_file in PROJECT_INSTANCES:
        result = validate_project_instance(instance_file, valid_ids)
        if "error" not in result:
            instance_results.append(result)
            status = "✅ Valid" if result["valid"] else "❌ Invalid"
            print(f"\n{instance_file}: {status}")
            print(f"  References found: {result['references_found']}")
            if result["invalid_references"]:
                print(f"  Invalid references: {len(result['invalid_references'])}")
                for invalid in result["invalid_references"][:3]:  # Show first 3
                    print(f"    - {invalid}")
    
    # Summary
    print("\n" + "=" * 60)
    print("Validation Summary")
    print("=" * 60)
    
    all_valid = all(r["valid"] for r in template_results + instance_results)
    total_references = sum(r["references_found"] for r in template_results + instance_results)
    total_invalid = sum(len(r.get("invalid_references", [])) for r in template_results + instance_results)
    
    if all_valid:
        print("\n[OK] All references are valid!")
        print(f"   Total references checked: {total_references}")
    else:
        print(f"\n[ERROR] Found {total_invalid} invalid references")
        print(f"   Total references checked: {total_references}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()

