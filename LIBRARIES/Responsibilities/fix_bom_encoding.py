"""
Fix UTF-8 BOM encoding issues in task template files
"""
import json
import os
from pathlib import Path
import time

# Files with UTF-8 BOM encoding issues
BOM_FILES = [
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates\TEMPLATE-TASK-HR-AUTO-001_Setup_n8n_for_CV_Screening.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates\TEMPLATE-TASK-HR-AUTO-002_Configure_Gemini_AI_Analysis.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates\TEMPLATE-TASK-HR-AUTO-003_Build_Notion_ATS_Database.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates\TEMPLATE-TASK-HR-AUTO-004_Setup_Interview_Scheduling.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates\TEMPLATE-TASK-HR-AUTO-005_Configure_LinkedIn_Automation.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates\TEMPLATE-TASK-HR-AUTO-006_Setup_Onboarding_Workflow.json",
    r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Task_Templates\TEMPLATE-TASK-RES-001_Research_AI_Video_Tools.json",
]

def fix_bom_encoding(file_path, max_retries=3):
    """Fix UTF-8 BOM encoding by reading with utf-8-sig and writing with utf-8"""
    for attempt in range(max_retries):
        try:
            # Read with utf-8-sig to handle BOM
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                content = f.read()

            # Parse JSON to validate
            data = json.loads(content)

            # Write back without BOM
            with open(file_path, 'w', encoding='utf-8', newline='') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            print(f"[OK] Fixed: {Path(file_path).name}")
            return True

        except PermissionError:
            if attempt < max_retries - 1:
                print(f"  File locked, waiting... (attempt {attempt + 1}/{max_retries})")
                time.sleep(2)
            else:
                print(f"[FAIL] Failed (locked): {Path(file_path).name}")
                return False
        except Exception as e:
            print(f"[ERROR] Error fixing {Path(file_path).name}: {e}")
            return False

    return False

def main():
    print("=" * 60)
    print("Fixing UTF-8 BOM Encoding Issues")
    print("=" * 60)

    fixed = 0
    failed = 0

    for file_path in BOM_FILES:
        if os.path.exists(file_path):
            if fix_bom_encoding(file_path):
                fixed += 1
            else:
                failed += 1
        else:
            print(f"[ERROR] Not found: {Path(file_path).name}")
            failed += 1

    print("\n" + "=" * 60)
    print(f"Summary: {fixed} fixed, {failed} failed")
    print("=" * 60)

if __name__ == "__main__":
    main()
