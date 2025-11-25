#!/usr/bin/env python3
"""
Rename Project Templates: TEMPLATE-PROJ-* to Proj_Temp-*
Updates file names, template_id fields, and all references.

Created: November 25, 2025
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Base paths
BASE_DIR = Path(__file__).parent.parent
PROJECT_TEMPLATES_DIR = BASE_DIR / "Project_Templates"
CHECKLIST_ITEMS_DIR = BASE_DIR / "Checklist_Items"

# Mapping: old_name -> new_name
RENAME_MAP = {
    "TEMPLATE-PROJ-AI-002": "Proj_Temp-AI-002",
    "TEMPLATE-PROJ-DEV-001": "Proj_Temp-DEV-001",
    "TEMPLATE-PROJ-HR-002": "Proj_Temp-HR-002",
    "TEMPLATE-PROJ-LG-001": "Proj_Temp-LG-001",
    "TEMPLATE-PROJ-LG-002": "Proj_Temp-LG-002",
    "TEMPLATE-PROJ-RES-001": "Proj_Temp-RES-001",
    "TEMPLATE_System_Analysis": "Proj_Temp-System_Analysis"  # Special case
}

# File name mappings (with extensions and suffixes)
FILE_RENAME_MAP = {
    "TEMPLATE-PROJ-AI-002.json": "Proj_Temp-AI-002.json",
    "TEMPLATE-PROJ-DEV-001.json": "Proj_Temp-DEV-001.json",
    "TEMPLATE-PROJ-HR-002_HR_Automation_Implementation.json": "Proj_Temp-HR-002.json",
    "TEMPLATE-PROJ-LG-001.json": "Proj_Temp-LG-001.json",
    "TEMPLATE-PROJ-LG-002.json": "Proj_Temp-LG-002.json",
    "TEMPLATE-PROJ-RES-001_Research_to_Taxonomy_Pipeline.json": "Proj_Temp-RES-001.json",
    "TEMPLATE_System_Analysis.json": "Proj_Temp-System_Analysis.json"
}


def load_json_file(file_path: Path) -> Dict:
    """Load JSON file, handling UTF-8 BOM if present."""
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        return json.load(f)


def save_json_file(file_path: Path, data: Dict):
    """Save JSON file with proper formatting."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def update_template_id_in_json(file_path: Path, old_id: str, new_id: str):
    """Update template_id field in a JSON file."""
    data = load_json_file(file_path)
    
    if "template_id" in data and data["template_id"] == old_id:
        data["template_id"] = new_id
        save_json_file(file_path, data)
        print(f"  Updated template_id: {old_id} -> {new_id}")
        return True
    return False


def rename_project_template_file(old_name: str, new_name: str) -> bool:
    """Rename a project template file."""
    old_path = PROJECT_TEMPLATES_DIR / old_name
    new_path = PROJECT_TEMPLATES_DIR / new_name
    
    if not old_path.exists():
        print(f"Warning: {old_name} not found")
        return False
    
    # Extract template ID from old name
    old_id = old_name.replace(".json", "").replace("_HR_Automation_Implementation", "").replace("_Research_to_Taxonomy_Pipeline", "")
    new_id = new_name.replace(".json", "")
    
    # Update template_id inside the file
    update_template_id_in_json(old_path, old_id, new_id)
    
    # Rename the file
    os.rename(old_path, new_path)
    print(f"Renamed: {old_name} -> {new_name}")
    return True


def update_checklist_items_references():
    """Update all checklist item files to reference new template IDs."""
    print("\nUpdating checklist items...")
    
    # Update By_Project folder names
    for old_id, new_id in RENAME_MAP.items():
        old_folder = CHECKLIST_ITEMS_DIR / "By_Project" / old_id
        new_folder = CHECKLIST_ITEMS_DIR / "By_Project" / new_id
        
        if old_folder.exists():
            os.rename(old_folder, new_folder)
            print(f"  Renamed folder: {old_id} -> {new_id}")
            
            # Update all JSON files in the folder
            for item_file in new_folder.glob("*.json"):
                data = load_json_file(item_file)
                
                # Update associated_project
                if data.get("associated_project") == old_id:
                    data["associated_project"] = new_id
                
                # Update checklist_item_id
                old_item_id = data.get("checklist_item_id", "")
                if old_item_id.startswith(f"CHK-{old_id}"):
                    new_item_id = old_item_id.replace(f"CHK-{old_id}", f"CHK-{new_id}")
                    data["checklist_item_id"] = new_item_id
                
                # Update migrated_from source_file
                if "migrated_from" in data and "source_file" in data["migrated_from"]:
                    old_file_ref = data["migrated_from"]["source_file"]
                    if old_id in old_file_ref:
                        data["migrated_from"]["source_file"] = old_file_ref.replace(old_id, new_id)
                
                save_json_file(item_file, data)
                
                # Rename the file if checklist_item_id changed
                if old_item_id != new_item_id:
                    new_file_name = f"{new_item_id}.json"
                    new_file_path = new_folder / new_file_name
                    os.rename(item_file, new_file_path)
                    print(f"    Updated: {item_file.name} -> {new_file_name}")
    
    # Update Listing.json
    listing_path = CHECKLIST_ITEMS_DIR / "Listing.json"
    if listing_path.exists():
        data = load_json_file(listing_path)
        
        updated_count = 0
        for item in data.get("items", []):
            old_project = item.get("associated_project", "")
            if old_project in RENAME_MAP:
                new_project = RENAME_MAP[old_project]
                item["associated_project"] = new_project
                
                # Update checklist_item_id
                old_item_id = item.get("checklist_item_id", "")
                if old_item_id.startswith(f"CHK-{old_project}"):
                    new_item_id = old_item_id.replace(f"CHK-{old_project}", f"CHK-{new_project}")
                    item["checklist_item_id"] = new_item_id
                
                # Update file_path
                old_path = item.get("file_path", "")
                if old_project in old_path:
                    new_path = old_path.replace(old_project, new_project)
                    if old_item_id in new_path:
                        new_path = new_path.replace(old_item_id, new_item_id)
                    item["file_path"] = new_path
                
                updated_count += 1
        
        # Update by_project counts
        if "by_project" in data:
            new_by_project = {}
            for old_id, count in data["by_project"].items():
                if old_id in RENAME_MAP:
                    new_by_project[RENAME_MAP[old_id]] = count
                else:
                    new_by_project[old_id] = count
            data["by_project"] = new_by_project
        
        save_json_file(listing_path, data)
        print(f"  Updated Listing.json ({updated_count} items)")


def update_other_references():
    """Update references in other files (migration scripts, docs, etc.)."""
    print("\nUpdating other references...")
    
    files_to_update = [
        CHECKLIST_ITEMS_DIR / "migrate_deliverables.py",
        CHECKLIST_ITEMS_DIR / "MIGRATION_REPORT.md",
        CHECKLIST_ITEMS_DIR / "MIGRATION_SCRIPT.md",
        CHECKLIST_ITEMS_DIR / "Checklist_Item_Schema.md",
        CHECKLIST_ITEMS_DIR / "README.md"
    ]
    
    for file_path in files_to_update:
        if not file_path.exists():
            continue
        
        if file_path.suffix == ".py":
            # Python file - update string literals
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            for old_id, new_id in FILE_RENAME_MAP.items():
                content = content.replace(old_id, new_id)
            for old_id, new_id in RENAME_MAP.items():
                content = content.replace(old_id, new_id)
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  Updated: {file_path.name}")
        
        elif file_path.suffix == ".md":
            # Markdown file - update text references
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            for old_id, new_id in FILE_RENAME_MAP.items():
                content = content.replace(old_id, new_id)
            for old_id, new_id in RENAME_MAP.items():
                content = content.replace(old_id, new_id)
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  Updated: {file_path.name}")


def main():
    """Main renaming function."""
    print("=" * 60)
    print("Project Template Renaming: TEMPLATE-PROJ-* to Proj_Temp-*")
    print("=" * 60)
    
    # Step 1: Rename files
    print("\nStep 1: Renaming project template files...")
    for old_name, new_name in FILE_RENAME_MAP.items():
        rename_project_template_file(old_name, new_name)
    
    # Step 2: Update checklist items
    update_checklist_items_references()
    
    # Step 3: Update other references
    update_other_references()
    
    print("\n" + "=" * 60)
    print("Renaming complete!")
    print("=" * 60)
    print("\nSummary:")
    print(f"  - Renamed {len(FILE_RENAME_MAP)} project template files")
    print(f"  - Updated template_id fields in JSON files")
    print(f"  - Updated checklist items references")
    print(f"  - Updated documentation and scripts")


if __name__ == "__main__":
    main()

