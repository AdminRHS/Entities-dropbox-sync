#!/usr/bin/env python3
"""Fix remaining TEMPLATE-PROJ-AI-002 references in checklist items."""

import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
CHECKLIST_DIR = BASE_DIR / "Checklist_Items"
AI002_FOLDER = CHECKLIST_DIR / "By_Project" / "Proj_Temp-AI-002"

OLD_ID = "TEMPLATE-PROJ-AI-002"
NEW_ID = "Proj_Temp-AI-002"

def load_json_file(file_path: Path) -> dict:
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        return json.load(f)

def save_json_file(file_path: Path, data: dict):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# Update all files in AI-002 folder
for item_file in AI002_FOLDER.glob("*.json"):
    data = load_json_file(item_file)
    updated = False
    
    # Update associated_project
    if data.get("associated_project") == OLD_ID:
        data["associated_project"] = NEW_ID
        updated = True
    
    # Update checklist_item_id
    old_item_id = data.get("checklist_item_id", "")
    if OLD_ID in old_item_id:
        new_item_id = old_item_id.replace(OLD_ID, NEW_ID)
        data["checklist_item_id"] = new_item_id
        updated = True
        
        # Rename file
        new_file_name = f"{new_item_id}.json"
        new_file_path = AI002_FOLDER / new_file_name
        os.rename(item_file, new_file_path)
        print(f"Renamed: {item_file.name} -> {new_file_name}")
        item_file = new_file_path
    
    # Update migrated_from source_file
    if "migrated_from" in data and "source_file" in data["migrated_from"]:
        old_file_ref = data["migrated_from"]["source_file"]
        if OLD_ID in old_file_ref:
            data["migrated_from"]["source_file"] = old_file_ref.replace(OLD_ID, NEW_ID)
            updated = True
    
    if updated:
        save_json_file(item_file, data)
        print(f"Updated: {item_file.name}")

# Update Listing.json
listing_path = CHECKLIST_DIR / "Listing.json"
if listing_path.exists():
    data = load_json_file(listing_path)
    updated_count = 0
    
    for item in data.get("items", []):
        if item.get("associated_project") == OLD_ID:
            item["associated_project"] = NEW_ID
            old_item_id = item.get("checklist_item_id", "")
            if OLD_ID in old_item_id:
                new_item_id = old_item_id.replace(OLD_ID, NEW_ID)
                item["checklist_item_id"] = new_item_id
                item["file_path"] = item["file_path"].replace(OLD_ID, NEW_ID).replace(old_item_id, new_item_id)
            updated_count += 1
    
    # Update by_project
    if "by_project" in data and OLD_ID in data["by_project"]:
        count = data["by_project"].pop(OLD_ID)
        data["by_project"][NEW_ID] = count
    
    if updated_count > 0:
        save_json_file(listing_path, data)
        print(f"\nUpdated Listing.json ({updated_count} items)")

print("Done!")

