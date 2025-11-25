#!/usr/bin/env python3
"""
Migration Script: Deliverables to Checklist Items
Extracts deliverables from Project Templates and Project Instances,
creates Checklist Item files, and updates references.

Created: November 25, 2025
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Any

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


def load_json_file(file_path: Path) -> Dict[str, Any]:
    """Load JSON file, handling UTF-8 BOM if present."""
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        return json.load(f)


def save_json_file(file_path: Path, data: Dict[str, Any]):
    """Save JSON file with proper formatting."""
    os.makedirs(file_path.parent, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def create_checklist_item(
    checklist_item_id: str,
    item_name: str,
    associated_project: str,
    associated_milestone: str = None,
    phase: int = None,
    source_file: str = None,
    source_type: str = "project_template"
) -> Dict[str, Any]:
    """Create a checklist item JSON structure."""
    item = {
        "checklist_item_id": checklist_item_id,
        "item_name": item_name,
        "entity_type": "TASK_MANAGERS",
        "sub_entity": "Checklist_Item",
        "associated_project": associated_project,
        "status": "pending",
        "required": True,
        "item_type": "deliverable",
        "version": "1.0",
        "created": "2025-11-25",
        "last_updated": "2025-11-25"
    }
    
    if associated_milestone:
        item["associated_milestone"] = associated_milestone
    if phase is not None:
        item["phase"] = phase
    if source_file:
        item["migrated_from"] = {
            "source_type": source_type,
            "source_file": source_file,
            "original_field": "deliverables",
            "migration_date": "2025-11-25"
        }
    
    return item


def extract_project_template_deliverables():
    """Extract deliverables from all project templates."""
    checklist_items = []
    item_counter = {}
    
    for template_file in PROJECT_TEMPLATES:
        template_path = PROJECT_TEMPLATES_DIR / template_file
        if not template_path.exists():
            print(f"Warning: {template_file} not found")
            continue
        
        print(f"Processing {template_file}...")
        template_data = load_json_file(template_path)
        template_id = template_data.get("template_id", "")
        
        milestones = template_data.get("milestones", [])
        for milestone in milestones:
            milestone_id = milestone.get("milestone_id", "")
            phase = milestone.get("phase")
            deliverables = milestone.get("deliverables", [])
            
            if not deliverables:
                continue
            
            # Initialize counter for this milestone
            if milestone_id not in item_counter:
                item_counter[milestone_id] = 0
            
            for deliverable in deliverables:
                item_counter[milestone_id] += 1
                item_number = f"{item_counter[milestone_id]:03d}"
                
                # Extract milestone number from milestone_id (e.g., MIL-PROJ-HR-002-001 -> 001)
                milestone_num = milestone_id.split("-")[-1] if "-" in milestone_id else "001"
                checklist_item_id = f"CHK-{template_id}-MIL-{milestone_num}-{item_number}"
                
                checklist_item = create_checklist_item(
                    checklist_item_id=checklist_item_id,
                    item_name=deliverable,
                    associated_project=template_id,
                    associated_milestone=milestone_id,
                    phase=phase,
                    source_file=f"ENTITIES/TASK_MANAGERS/Project_Templates/{template_file}",
                    source_type="project_template"
                )
                
                checklist_items.append({
                    "item": checklist_item,
                    "checklist_item_id": checklist_item_id,
                    "file_path": f"ENTITIES/TASK_MANAGERS/Checklist_Items/By_Project/{template_id}/{checklist_item_id}.json"
                })
    
    return checklist_items


def extract_project_instance_deliverables():
    """Extract deliverables from project instances."""
    checklist_items = []
    
    for instance_file in PROJECT_INSTANCES:
        instance_path = PROJECT_INSTANCES_DIR / instance_file
        if not instance_path.exists():
            print(f"Warning: {instance_file} not found")
            continue
        
        print(f"Processing {instance_file}...")
        instance_data = load_json_file(instance_path)
        
        # Extract project ID from path or data
        project_id = "PROJ-LIB-001"  # Default based on path
        if "project_id" in instance_data:
            project_id = instance_data["project_id"]
        elif "template_id" in instance_data:
            project_id = instance_data["template_id"]
        
        deliverables = instance_data.get("deliverables", [])
        
        for idx, deliverable in enumerate(deliverables, 1):
            item_number = f"{idx:03d}"
            checklist_item_id = f"CHK-{project_id}-{item_number}"
            
            checklist_item = create_checklist_item(
                checklist_item_id=checklist_item_id,
                item_name=deliverable,
                associated_project=project_id,
                source_file=f"ENTITIES/TASK_MANAGERS/{instance_file}",
                source_type="project_instance"
            )
            
            checklist_items.append({
                "item": checklist_item,
                "checklist_item_id": checklist_item_id,
                "file_path": f"ENTITIES/TASK_MANAGERS/Checklist_Items/By_Project/{project_id}/{checklist_item_id}.json"
            })
    
    return checklist_items


def save_checklist_items(checklist_items: List[Dict]):
    """Save all checklist items to files."""
    print(f"\nSaving {len(checklist_items)} checklist items...")
    
    for item_data in checklist_items:
        item = item_data["item"]
        file_path = Path(item_data["file_path"].replace("ENTITIES/TASK_MANAGERS/", ""))
        full_path = BASE_DIR / file_path
        
        save_json_file(full_path, item)
        print(f"  Created: {file_path}")


def create_listing_json(checklist_items: List[Dict]):
    """Create the master Listing.json file."""
    listing = {
        "entity_type": "TASK_MANAGERS",
        "sub_entity": "Checklist_Items_Listing",
        "version": "1.0",
        "last_updated": "2025-11-25",
        "total_items": len(checklist_items),
        "items": [],
        "by_project": {},
        "by_status": {
            "pending": len(checklist_items),
            "completed": 0,
            "in_progress": 0
        }
    }
    
    # Group by project
    for item_data in checklist_items:
        item = item_data["item"]
        project = item["associated_project"]
        
        if project not in listing["by_project"]:
            listing["by_project"][project] = 0
        listing["by_project"][project] += 1
        
        listing["items"].append({
            "checklist_item_id": item["checklist_item_id"],
            "item_name": item["item_name"],
            "associated_project": project,
            "associated_milestone": item.get("associated_milestone"),
            "status": item["status"],
            "file_path": item_data["file_path"]
        })
    
    listing_path = CHECKLIST_DIR / "Listing.json"
    save_json_file(listing_path, listing)
    print(f"\nCreated Listing.json with {len(checklist_items)} items")


def main():
    """Main migration function."""
    print("=" * 60)
    print("Deliverables to Checklist Items Migration")
    print("=" * 60)
    
    # Create directory structure
    os.makedirs(CHECKLIST_DIR / "By_Project", exist_ok=True)
    
    # Extract deliverables
    template_items = extract_project_template_deliverables()
    instance_items = extract_project_instance_deliverables()
    
    all_items = template_items + instance_items
    
    print(f"\nTotal deliverables found: {len(all_items)}")
    print(f"  - From templates: {len(template_items)}")
    print(f"  - From instances: {len(instance_items)}")
    
    # Save checklist items
    save_checklist_items(all_items)
    
    # Create listing
    create_listing_json(all_items)
    
    print("\n" + "=" * 60)
    print("Migration complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Review generated checklist items")
    print("2. Update project templates to reference checklist_items")
    print("3. Remove deliverables arrays from project templates")


if __name__ == "__main__":
    main()

