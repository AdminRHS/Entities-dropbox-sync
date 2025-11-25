#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rename Checklist Items: Change ID format from CHK-{PROJECT}-{MILESTONE}-{NUM} to CHK-{NUM}
Updates all checklist item files, Listing.json, and project template references.

Created: November 25, 2025
"""

import json
import os
import shutil
from pathlib import Path
from typing import Dict, List, Any, Tuple

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


def save_json_file(file_path: Path, data: Dict[str, Any]):
    """Save JSON file with proper formatting."""
    os.makedirs(file_path.parent, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def build_id_mapping(listing_data: Dict[str, Any]) -> Tuple[Dict[str, str], List[Dict[str, Any]]]:
    """
    Build mapping from old IDs to new IDs (CHK-001, CHK-002, etc.).
    Returns (mapping_dict, sorted_items_list)
    """
    items = listing_data.get("items", [])
    
    # Sort items to ensure consistent ordering
    # Sort by project, then milestone, then original item number
    def sort_key(item):
        project = item.get("associated_project", "")
        milestone = item.get("associated_milestone") or ""
        old_id = item.get("checklist_item_id", "")
        # Extract number from old ID for sorting
        try:
            num_part = old_id.split("-")[-1]
            return (project, milestone, int(num_part))
        except:
            return (project, milestone, 0)
    
    sorted_items = sorted(items, key=sort_key)
    
    # Create mapping
    mapping = {}
    for idx, item in enumerate(sorted_items, 1):
        old_id = item.get("checklist_item_id", "")
        new_id = f"CHK-{idx:03d}"
        mapping[old_id] = new_id
    
    return mapping, sorted_items


def rename_checklist_item_file(old_id: str, new_id: str, project_dir: Path) -> bool:
    """Rename checklist item file from old_id to new_id."""
    old_file = project_dir / f"{old_id}.json"
    new_file = project_dir / f"{new_id}.json"
    
    if not old_file.exists():
        return False
    
    # Read and update the file content
    item_data = load_json_file(old_file)
    item_data["checklist_item_id"] = new_id
    
    # Save with new name
    save_json_file(new_file, item_data)
    
    # Delete old file
    if old_file != new_file:
        old_file.unlink()
    
    return True


def update_listing_json(mapping: Dict[str, str], sorted_items: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Update Listing.json with new IDs."""
    listing_data = load_json_file(LISTING_FILE)
    
    # Update items
    updated_items = []
    for item in sorted_items:
        old_id = item.get("checklist_item_id", "")
        new_id = mapping.get(old_id, old_id)
        
        updated_item = item.copy()
        updated_item["checklist_item_id"] = new_id
        
        # Update file_path
        old_path = item.get("file_path", "")
        if old_path:
            # Extract project from old path
            parts = old_path.split("/")
            project_part = None
            for part in parts:
                if part.startswith("Proj_Temp-") or part.startswith("PROJ-"):
                    project_part = part
                    break
            
            if project_part:
                updated_item["file_path"] = f"ENTITIES/TASK_MANAGERS/Checklist_Items/By_Project/{project_part}/{new_id}.json"
        
        updated_items.append(updated_item)
    
    listing_data["items"] = updated_items
    listing_data["last_updated"] = "2025-11-25"
    
    return listing_data


def update_project_template(template_file: str, mapping: Dict[str, str]) -> Dict[str, Any]:
    """Update checklist_items references in a project template."""
    template_path = PROJECT_TEMPLATES_DIR / template_file
    if not template_path.exists():
        return {"error": f"File not found: {template_file}"}
    
    template_data = load_json_file(template_path)
    
    stats = {
        "template_id": template_data.get("template_id", ""),
        "milestones_updated": 0,
        "references_updated": 0
    }
    
    milestones = template_data.get("milestones", [])
    for milestone in milestones:
        checklist_items = milestone.get("checklist_items", [])
        
        if not checklist_items:
            continue
        
        # Update references
        updated_items = []
        for old_id in checklist_items:
            new_id = mapping.get(old_id, old_id)
            updated_items.append(new_id)
            if old_id != new_id:
                stats["references_updated"] += 1
        
        milestone["checklist_items"] = updated_items
        stats["milestones_updated"] += 1
    
    # Save updated template
    save_json_file(template_path, template_data)
    
    return stats


def update_project_instance(instance_file: str, mapping: Dict[str, str]) -> Dict[str, Any]:
    """Update checklist_items references in a project instance."""
    instance_path = PROJECT_INSTANCES_DIR / instance_file
    if not instance_path.exists():
        return {"error": f"File not found: {instance_file}"}
    
    instance_data = load_json_file(instance_path)
    
    stats = {
        "project_id": instance_data.get("project_id") or instance_data.get("template_id", ""),
        "references_updated": 0
    }
    
    checklist_items = instance_data.get("checklist_items", [])
    
    if checklist_items:
        updated_items = []
        for old_id in checklist_items:
            new_id = mapping.get(old_id, old_id)
            updated_items.append(new_id)
            if old_id != new_id:
                stats["references_updated"] += 1
        
        instance_data["checklist_items"] = updated_items
        save_json_file(instance_path, instance_data)
    
    return stats


def main():
    """Main migration function."""
    print("=" * 60)
    print("Rename Checklist Items: CHK-{PROJECT}-{MILESTONE}-{NUM} -> CHK-{NUM}")
    print("=" * 60)
    
    # Load listing
    if not LISTING_FILE.exists():
        print(f"Error: Listing file not found: {LISTING_FILE}")
        return
    
    listing_data = load_json_file(LISTING_FILE)
    print(f"\nLoaded {listing_data.get('total_items', 0)} checklist items")
    
    # Build ID mapping
    print("Building ID mapping...")
    mapping, sorted_items = build_id_mapping(listing_data)
    print(f"Created mapping for {len(mapping)} items")
    print(f"  Example: {list(mapping.items())[0]}")
    
    # Rename all checklist item files
    print("\n" + "-" * 60)
    print("Renaming checklist item files...")
    print("-" * 60)
    
    files_renamed = 0
    files_failed = 0
    
    for old_id, new_id in mapping.items():
        # Find project directory
        project_dir = None
        for item in sorted_items:
            if item.get("checklist_item_id") == old_id:
                file_path = item.get("file_path", "")
                if file_path:
                    # Extract project directory
                    parts = file_path.split("/")
                    for part in parts:
                        if part.startswith("Proj_Temp-") or part.startswith("PROJ-"):
                            project_dir = CHECKLIST_DIR / "By_Project" / part
                            break
                break
        
        if project_dir and project_dir.exists():
            if rename_checklist_item_file(old_id, new_id, project_dir):
                files_renamed += 1
            else:
                files_failed += 1
                print(f"  Warning: Failed to rename {old_id}")
        else:
            files_failed += 1
            print(f"  Warning: Project directory not found for {old_id}")
    
    print(f"\nFiles renamed: {files_renamed}")
    if files_failed > 0:
        print(f"Files failed: {files_failed}")
    
    # Update Listing.json
    print("\n" + "-" * 60)
    print("Updating Listing.json...")
    print("-" * 60)
    
    updated_listing = update_listing_json(mapping, sorted_items)
    save_json_file(LISTING_FILE, updated_listing)
    print("Listing.json updated")
    
    # Update project templates
    print("\n" + "-" * 60)
    print("Updating Project Templates...")
    print("-" * 60)
    
    template_stats = []
    for template_file in PROJECT_TEMPLATES:
        stats = update_project_template(template_file, mapping)
        if "error" not in stats:
            template_stats.append(stats)
            print(f"  {template_file}: {stats['references_updated']} references updated")
    
    # Update project instances
    print("\n" + "-" * 60)
    print("Updating Project Instances...")
    print("-" * 60)
    
    instance_stats = []
    for instance_file in PROJECT_INSTANCES:
        stats = update_project_instance(instance_file, mapping)
        if "error" not in stats:
            instance_stats.append(stats)
            print(f"  {instance_file}: {stats['references_updated']} references updated")
    
    # Summary
    print("\n" + "=" * 60)
    print("Migration Summary")
    print("=" * 60)
    
    total_refs = sum(s["references_updated"] for s in template_stats + instance_stats)
    
    print(f"\nFiles renamed: {files_renamed}")
    print(f"Project templates updated: {len(template_stats)}")
    print(f"Project instances updated: {len(instance_stats)}")
    print(f"Total references updated: {total_refs}")
    
    print("\n" + "=" * 60)
    print("Migration complete!")
    print("=" * 60)
    print("\nNew ID format: CHK-001, CHK-002, ..., CHK-098")


if __name__ == "__main__":
    main()

