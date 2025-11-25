#!/usr/bin/env python3
"""
Update all references from TASK_MANAGERS/PROMPTS to ENTITIES/PROMPTS
"""

import os
import re
from pathlib import Path

# Files to update based on grep results
files_to_update = [
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Taxonomy\Taxonomy_Master_List.csv",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\RESEARCHES\oa-y_Research_Data_Flow_Notes.md",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Project_Templates\Project-Template-007_System_Analysis.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates\Task-Template-058_Create_Update_Tool_Entries.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates\Task-Template-057_Transcribe_Video.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates\Task-Template-055_Update_Mappings.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates\Task-Template-056_Gap_Analysis.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates\Task-Template-053_Validate_Taxonomy.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates\Task-Template-054_Validate_Tools.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates\Task-Template-052_Extract_Taxonomy.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates\Task-Template-051_Select_Videos.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates\Task-Template-050_Search_Score_Videos.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\ARCHITECTURE_LOG.md",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates_BACKUP\TASK-TEMPLATE-VIDEO-007_Gap_Analysis.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates_BACKUP\TASK-TEMPLATE-VIDEO-001_Search_Score_Videos.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates_BACKUP\TASK-TEMPLATE-VIDEO-002_Select_Videos.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates_BACKUP\TASK-TEMPLATE-VIDEO-003_Extract_Taxonomy.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates_BACKUP\TASK-TEMPLATE-VIDEO-004_Validate_Taxonomy.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates_BACKUP\TASK-TEMPLATE-VIDEO-005_Validate_Tools.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates_BACKUP\TASK-TEMPLATE-VIDEO-006_Update_Mappings.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates_BACKUP\TASK-TEMPLATE-VIDEO-101_Transcribe_Video.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates_BACKUP\TASK-TEMPLATE-VIDEO-301_Create_Update_Tool_Entries.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Project_Templates_BACKUP\Proj_Temp-System_Analysis.json",
]

def update_file(file_path):
    """Update PROMPTS references in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Replace various forms of the path
        content = content.replace('TASK_MANAGERS/PROMPTS', 'PROMPTS')
        content = content.replace('TASK_MANAGERS\\PROMPTS', 'PROMPTS')
        content = content.replace('TASK_MANAGERS\\\\PROMPTS', 'PROMPTS')

        # Only write if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Updated: {Path(file_path).name}")
            return True
        else:
            print(f"[-] No changes: {Path(file_path).name}")
            return False

    except Exception as e:
        print(f"[ERROR] Error updating {Path(file_path).name}: {str(e)}")
        return False

def main():
    print("=" * 60)
    print("PROMPTS PATH REFERENCE UPDATE SCRIPT")
    print("=" * 60)
    print(f"\nUpdating references in {len(files_to_update)} files...")
    print(f"FROM: TASK_MANAGERS/PROMPTS")
    print(f"TO:   PROMPTS")
    print("\n" + "-" * 60 + "\n")

    updated_count = 0
    error_count = 0

    for file_path in files_to_update:
        if os.path.exists(file_path):
            if update_file(file_path):
                updated_count += 1
        else:
            print(f"[ERROR] File not found: {Path(file_path).name}")
            error_count += 1

    print("\n" + "-" * 60)
    print(f"\nSUMMARY:")
    print(f"  Total files processed: {len(files_to_update)}")
    print(f"  Files updated: {updated_count}")
    print(f"  Files with errors: {error_count}")
    print(f"  Files unchanged: {len(files_to_update) - updated_count - error_count}")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
