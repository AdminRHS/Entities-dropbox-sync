"""
Cleanup Script - Remove old folder structure
Removes old folders now that all prompts are in Core/
"""
import os
import shutil

PROMPTS_DIR = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS"

# Folders to DELETE (old structure)
FOLDERS_TO_REMOVE = [
    'CREATIVES',
    'DEPARTMENTS',
    'SYSTEM',
    'WORKFLOWS',
    'UTILITIES',
    'Automation',
    'DATA_FIELDS',
    '_INDEX',
]

# Folders to KEEP
FOLDERS_TO_KEEP = [
    'Core',
    '_ARCHIVE',
]

def cleanup_old_folders():
    """Remove old folder structure"""
    print("=" * 60)
    print("CLEANUP: REMOVING OLD FOLDER STRUCTURE")
    print("=" * 60)

    print("\nFolders that will be KEPT:")
    for folder in FOLDERS_TO_KEEP:
        folder_path = os.path.join(PROMPTS_DIR, folder)
        if os.path.exists(folder_path):
            print(f"  [KEEP] {folder}")

    print("\nFolders that will be REMOVED:")
    removed_count = 0

    for folder in FOLDERS_TO_REMOVE:
        folder_path = os.path.join(PROMPTS_DIR, folder)

        if os.path.exists(folder_path):
            try:
                # Check if folder is empty or has files
                file_count = sum(len(files) for _, _, files in os.walk(folder_path))

                print(f"\n  Removing: {folder}/")
                print(f"    Files in folder: {file_count}")

                # Remove folder and all contents
                shutil.rmtree(folder_path)
                print(f"    [OK] Removed successfully")
                removed_count += 1

            except Exception as e:
                print(f"    [ERROR] Error: {str(e)}")
        else:
            print(f"  - {folder}/ (not found)")

    print("\n" + "=" * 60)
    print(f"[SUCCESS] Removed {removed_count} old folders")
    print("=" * 60)

    print("\nCurrent PROMPTS folder structure:")
    print("PROMPTS/")
    for item in sorted(os.listdir(PROMPTS_DIR)):
        item_path = os.path.join(PROMPTS_DIR, item)
        if os.path.isdir(item_path):
            # Count files in folder
            file_count = sum(len(files) for _, _, files in os.walk(item_path))
            print(f"├── {item}/ ({file_count} files)")

    print("\n[SUCCESS] Cleanup complete!")
    print("[SUCCESS] All prompts are now in Core/ folder")
    print("[SUCCESS] Old folders have been removed")

if __name__ == '__main__':
    cleanup_old_folders()
