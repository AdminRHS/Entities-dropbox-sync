#!/usr/bin/env python3
"""
Update Project Templates Script: Replace deliverables with checklist_items references
Updates Project Templates and Project Instances to reference checklist_items instead of deliverables.

Created: November 25, 2025
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Any, Optional

# Base paths
BASE_DIR = Path(__file__).parent.parent
CHECKLIST_DIR = BASE_DIR / "Checklist_Items"
PROJECT_TEMPLATES_DIR = BASE_DIR / "Project_Templates"
PROJECT_INSTANCES_DIR = BASE_DIR

# Project templates to process
PROJECT_TEMPLATES = [
    "Proj_Temp-HR-002.json",
    "Proj_Temp-AI-002.json",
    "Proj_Temp-DEV-001.json",
    "Proj_Temp-LG-001.json",
    "Proj_Temp-LG-002.json"
]

# Project instances to process
PROJECT_INSTANCES = [
    "PROJ-LIB-001_Responsibilities_Ecosystem/project_instance.json"
]

LISTING_FILE = CHECKLIST_DIR / "Listing.json"


def load_json_file(file_path: Path) -> Dict[str, Any]:
    """Load JSON file, handling UTF-8 BOM if present."""
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        return json.load(f)


def save_json_file(file_path: Path, data: Dict[str, Any]):
    """Save JSON file with proper formatting."""
    os.makedirs(file_path.parent, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def build_checklist_mapping(listing_data: Dict[str, Any]) -> Dict[str, str]:
    """
    Build a mapping from (project_id, milestone_id, item_name) to checklist_item_id.
    
    Returns a dictionary with keys like: "Proj_Temp-HR-002|MIL-PROJ-HR-002-001|n8n workflow..."
    """
    mapping = {}
    
    for item in listing_data.get("items", []):
        project_id = item.get("associated_project", "")
        milestone_id = item.get("associated_milestone") or ""
        item_name = item.get("item_name", "")
        checklist_item_id = item.get("checklist_item_id", "")
        
        # Create composite key
        key = f"{project_id}|{milestone_id}|{item_name}"
        mapping[key] = checklist_item_id
    
    return mapping


def update_project_template(template_file: str, checklist_mapping: Dict[str, str]) -> Dict[str, Any]:
    """
    Update a project template to replace deliverables with checklist_items.
    
    Returns a dictionary with update statistics.
    """
    template_path = PROJECT_TEMPLATES_DIR / template_file
    if not template_path.exists():
        return {"error": f"File not found: {template_file}"}
    
    print(f"\nProcessing {template_file}...")
    template_data = load_json_file(template_path)
    template_id = template_data.get("template_id", "")
    
    stats = {
        "template_id": template_id,
        "milestones_updated": 0,
        "items_added": 0,
        "items_not_found": []
    }
    
    milestones = template_data.get("milestones", [])
    for milestone in milestones:
        milestone_id = milestone.get("milestone_id", "")
        deliverables = milestone.get("deliverables", [])
        
        if not deliverables:
            continue
        
        # Build checklist_items array
        checklist_items = []
        for deliverable in deliverables:
            # Try to find matching checklist item
            key = f"{template_id}|{milestone_id}|{deliverable}"
            checklist_item_id = checklist_mapping.get(key)
            
            if checklist_item_id:
                checklist_items.append(checklist_item_id)
                stats["items_added"] += 1
            else:
                stats["items_not_found"].append({
                    "milestone": milestone_id,
                    "deliverable": deliverable
                })
                print(f"  Warning: No checklist item found for '{deliverable}' in {milestone_id}")
        
        # Replace deliverables with checklist_items
        if checklist_items:
            milestone["checklist_items"] = checklist_items
            # Keep deliverables for backward compatibility (commented out - remove if desired)
            # milestone.pop("deliverables", None)
            stats["milestones_updated"] += 1
    
    # Save updated template
    save_json_file(template_path, template_data)
    print(f"  Updated {stats['milestones_updated']} milestones, added {stats['items_added']} checklist items")
    
    return stats


def update_project_instance(instance_file: str, checklist_mapping: Dict[str, str]) -> Dict[str, Any]:
    """
    Update a project instance to replace deliverables with checklist_items.
    
    Returns a dictionary with update statistics.
    """
    instance_path = PROJECT_INSTANCES_DIR / instance_file
    if not instance_path.exists():
        return {"error": f"File not found: {instance_file}"}
    
    print(f"\nProcessing {instance_file}...")
    instance_data = load_json_file(instance_path)
    
    # Extract project ID
    project_id = instance_data.get("project_id") or instance_data.get("template_id") or "PROJ-LIB-001"
    
    stats = {
        "project_id": project_id,
        "items_added": 0,
        "items_not_found": []
    }
    
    deliverables = instance_data.get("deliverables", [])
    
    if deliverables:
        # Build checklist_items array
        checklist_items = []
        for deliverable in deliverables:
            # Try to find matching checklist item (no milestone for project instances)
            key = f"{project_id}||{deliverable}"
            checklist_item_id = checklist_mapping.get(key)
            
            if checklist_item_id:
                checklist_items.append(checklist_item_id)
                stats["items_added"] += 1
            else:
                stats["items_not_found"].append(deliverable)
                print(f"  Warning: No checklist item found for '{deliverable}'")
        
        # Replace deliverables with checklist_items
        if checklist_items:
            instance_data["checklist_items"] = checklist_items
            # Keep deliverables for backward compatibility (commented out - remove if desired)
            # instance_data.pop("deliverables", None)
    
    # Save updated instance
    save_json_file(instance_path, instance_data)
    print(f"  Added {stats['items_added']} checklist items")
    
    return stats


def main():
    """Main update function."""
    print("=" * 60)
    print("Update Project Templates: Replace deliverables with checklist_items")
    print("=" * 60)
    
    # Load checklist items listing
    if not LISTING_FILE.exists():
        print(f"Error: Listing file not found: {LISTING_FILE}")
        return
    
    listing_data = load_json_file(LISTING_FILE)
    print(f"\nLoaded {listing_data.get('total_items', 0)} checklist items from Listing.json")
    
    # Build mapping
    checklist_mapping = build_checklist_mapping(listing_data)
    print(f"Built mapping for {len(checklist_mapping)} items")
    
    # Update project templates
    template_stats = []
    for template_file in PROJECT_TEMPLATES:
        stats = update_project_template(template_file, checklist_mapping)
        if "error" not in stats:
            template_stats.append(stats)
    
    # Update project instances
    instance_stats = []
    for instance_file in PROJECT_INSTANCES:
        stats = update_project_instance(instance_file, checklist_mapping)
        if "error" not in stats:
            instance_stats.append(stats)
    
    # Print summary
    print("\n" + "=" * 60)
    print("Update Summary")
    print("=" * 60)
    
    total_milestones = sum(s["milestones_updated"] for s in template_stats)
    total_items = sum(s["items_added"] for s in template_stats + instance_stats)
    total_not_found = sum(len(s.get("items_not_found", [])) for s in template_stats + instance_stats)
    
    print(f"\nProject Templates Updated: {len(template_stats)}")
    print(f"  Milestones updated: {total_milestones}")
    print(f"  Checklist items added: {total_items}")
    
    if total_not_found > 0:
        print(f"\n⚠️  Warning: {total_not_found} deliverables could not be mapped to checklist items")
        print("   These may need manual review or the deliverables may have changed.")
    
    print("\n" + "=" * 60)
    print("Update complete!")
    print("=" * 60)
    print("\nNote: deliverables arrays have been kept for backward compatibility.")
    print("      Remove them manually if desired after validating the migration.")


if __name__ == "__main__":
    main()

