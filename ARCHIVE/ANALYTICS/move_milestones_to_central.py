#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Move Milestones Script: Move milestone files from project folders to central Milestones folder
Moves milestone files from Projects/*/Milestones/ to ANALYTICS/Milestones/

Created: November 25, 2025
"""

import json
import os
import shutil
from pathlib import Path
from typing import Dict, List

# Base paths
BASE_DIR = Path(__file__).parent
PROJECTS_DIR = BASE_DIR / "Projects"
MILESTONES_DIR = BASE_DIR / "Milestones"


def load_json_file(file_path: Path) -> Dict:
    """Load JSON file, handling UTF-8 BOM if present."""
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"  Error parsing {file_path.name}: {e}")
        print(f"    Line {e.lineno}, column {e.colno}")
        # Try reading raw content to see the issue
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            content = f.read()
            lines = content.split('\n')
            if e.lineno <= len(lines):
                print(f"    Problem line: {lines[e.lineno - 1]}")
        raise


def save_json_file(file_path: Path, data: Dict):
    """Save JSON file with proper formatting."""
    os.makedirs(file_path.parent, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_project_id_from_folder(folder_name: str) -> str:
    """Extract project ID from folder name."""
    # Example: "PROJ-AI-NMP-001_Next_Main_Prompt_Version" -> "PROJ-AI-NMP-001"
    if "_" in folder_name:
        return folder_name.split("_")[0]
    return folder_name


def move_milestones_from_project(project_folder: Path) -> List[Dict]:
    """Move milestone files from a project folder to central Milestones folder."""
    project_milestones_dir = project_folder / "Milestones"
    
    if not project_milestones_dir.exists():
        return []
    
    project_id = get_project_id_from_folder(project_folder.name)
    moved_files = []
    
    # Get all JSON files in the Milestones folder
    milestone_files = list(project_milestones_dir.glob("*.json"))
    
    for milestone_file in milestone_files:
        # Load milestone data
        milestone_data = load_json_file(milestone_file)
        
        # Get milestone ID
        milestone_id = milestone_data.get("milestone_id", "")
        milestone_name = milestone_data.get("milestone_name", "")
        
        # Create new filename with project prefix
        # Format: PROJ-AI-NMP-001_MIL-001_Folder_Structure_Creation.json
        if milestone_id:
            # Extract the descriptive part from original filename
            original_name = milestone_file.stem  # e.g., "MIL-001_Folder_Structure_Creation"
            if original_name.startswith("MIL-"):
                descriptive_part = original_name[4:]  # Remove "MIL-" prefix
                new_filename = f"{project_id}_MIL-{milestone_id}_{descriptive_part}.json"
            else:
                new_filename = f"{project_id}_{milestone_id}_{milestone_name.replace(' ', '_')}.json"
        else:
            # Fallback: use original name with project prefix
            new_filename = f"{project_id}_{milestone_file.name}"
        
        # Ensure milestone_data has project_id
        milestone_data["project_id"] = project_id
        
        # Create destination path
        dest_path = MILESTONES_DIR / new_filename
        
        # Check if file already exists
        if dest_path.exists():
            print(f"  Warning: {new_filename} already exists, skipping...")
            continue
        
        # Save to new location
        save_json_file(dest_path, milestone_data)
        
        # Delete original file
        milestone_file.unlink()
        
        moved_files.append({
            "original": str(milestone_file),
            "new": str(dest_path),
            "milestone_id": milestone_id
        })
    
    # Remove empty Milestones folder
    try:
        if project_milestones_dir.exists() and not any(project_milestones_dir.iterdir()):
            project_milestones_dir.rmdir()
            print(f"  Removed empty Milestones folder")
    except:
        pass
    
    return moved_files


def main():
    """Main migration function."""
    print("=" * 60)
    print("Move Milestones to Central Location")
    print("=" * 60)
    
    if not PROJECTS_DIR.exists():
        print(f"Error: Projects directory not found: {PROJECTS_DIR}")
        return
    
    if not MILESTONES_DIR.exists():
        os.makedirs(MILESTONES_DIR, exist_ok=True)
        print(f"Created Milestones directory: {MILESTONES_DIR}")
    
    # Find all project folders
    project_folders = [p for p in PROJECTS_DIR.iterdir() if p.is_dir() and not p.name.startswith(".")]
    
    print(f"\nFound {len(project_folders)} project folders")
    
    total_moved = 0
    
    for project_folder in project_folders:
        milestones_dir = project_folder / "Milestones"
        
        if not milestones_dir.exists():
            continue
        
        print(f"\nProcessing {project_folder.name}...")
        
        moved = move_milestones_from_project(project_folder)
        
        if moved:
            print(f"  Moved {len(moved)} milestone files")
            total_moved += len(moved)
            for item in moved:
                print(f"    - {Path(item['original']).name} -> {Path(item['new']).name}")
        else:
            print(f"  No milestones to move")
    
    print("\n" + "=" * 60)
    print("Migration Summary")
    print("=" * 60)
    print(f"\nTotal milestone files moved: {total_moved}")
    print(f"Central location: {MILESTONES_DIR}")
    print("\n" + "=" * 60)
    print("Migration complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()

