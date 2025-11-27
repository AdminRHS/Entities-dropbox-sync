"""
Fix Restructuring - Move prompts from Core/ back to PROMPTS/ root
Keep original Core/ folder untouched
"""
import os
import shutil

PROMPTS_DIR = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS"
CORE_DIR = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\Core"

# Categories we created (to move back to root)
NEW_CATEGORIES = [
    'AUTOMATION',
    'CREATIVES',
    'DAILY_REPORTS',
    'DATA_ARCHITECTURE',
    'HR_OPERATIONS',
    'LIBRARY_PROCESSING',
    'MAIN_PROMPTS',
    'RESEARCH',
    'SYSTEM',
    'TAXONOMY',
    'UTILITIES',
    'VIDEO_PROCESSING',
    'WORKFLOWS',
]

def fix_structure():
    print("=" * 60)
    print("FIXING STRUCTURE")
    print("=" * 60)
    print("\nMoving prompts from Core/ back to PROMPTS/ root...")
    print("(Keeping original Core/ folder untouched)\n")

    moved_count = 0

    for category in NEW_CATEGORIES:
        source_dir = os.path.join(CORE_DIR, category)

        if os.path.exists(source_dir):
            # Get all .md files from this category
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    if file.endswith('.md') and file != 'README.md':
                        source_file = os.path.join(root, file)
                        dest_file = os.path.join(PROMPTS_DIR, file)

                        # Handle duplicates
                        counter = 1
                        original_dest = dest_file
                        while os.path.exists(dest_file):
                            name, ext = os.path.splitext(file)
                            dest_file = os.path.join(PROMPTS_DIR, f"{name}_{counter}{ext}")
                            counter += 1

                        try:
                            shutil.copy2(source_file, dest_file)
                            print(f"  Moved: {file}")
                            moved_count += 1
                        except Exception as e:
                            print(f"  ERROR: {file} - {str(e)}")

            # Remove the category folder from Core
            try:
                shutil.rmtree(source_dir)
                print(f"\n  [OK] Removed Core/{category}/\n")
            except Exception as e:
                print(f"\n  [ERROR] Could not remove Core/{category}/ - {str(e)}\n")

    print("\n" + "=" * 60)
    print(f"[SUCCESS] Moved {moved_count} prompts to PROMPTS/ root")
    print("=" * 60)

    # Show final structure
    print("\nFinal structure:")
    print("PROMPTS/")

    # Count files in root
    root_files = [f for f in os.listdir(PROMPTS_DIR) if os.path.isfile(os.path.join(PROMPTS_DIR, f)) and f.endswith('.md')]
    print(f"├── {len(root_files)} .md files in root")

    # Show folders
    for item in sorted(os.listdir(PROMPTS_DIR)):
        item_path = os.path.join(PROMPTS_DIR, item)
        if os.path.isdir(item_path):
            file_count = sum(len([f for f in files if f.endswith('.md')]) for _, _, files in os.walk(item_path))
            print(f"├── {item}/ ({file_count} .md files)")

    print("\n[SUCCESS] Structure fixed!")
    print("[SUCCESS] All prompts now in PROMPTS/ root")
    print("[SUCCESS] Original Core/ folder preserved")

if __name__ == '__main__':
    fix_structure()
