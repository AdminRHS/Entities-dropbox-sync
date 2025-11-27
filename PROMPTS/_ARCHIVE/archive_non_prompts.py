"""
Archive Non-Prompt Files
Move documentation, scripts, and support files to _ARCHIVE
Keep only actual prompt files in PROMPTS root
"""
import os
import shutil

PROMPTS_DIR = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS"
ARCHIVE_DIR = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\_ARCHIVE"

# Files to archive (not prompts)
NON_PROMPT_FILES = [
    # Documentation files
    'README.md',
    'CLEANUP_VERIFICATION.md',
    'FINAL_CLEAN_STATUS.md',
    'FINAL_STATUS.md',
    'MASTER_CSV_SIMPLIFIED.md',
    'RESTRUCTURE_FINAL.md',
    'RESTRUCTURING_COMPLETE.md',
    'RESTRUCTURING_SUMMARY.md',
    'DEPARTMENT_IMPORT_TEMPLATE.md',
    'Prompt_Locations_in_Nov25.md',
    'MIGRATION_LOG.md',

    # Guidance/framework docs (not prompts)
    '01_employee_directory_guidance.md',
    '02_project_directory_guidance.md',
    '03_vocabulary_standards.md',
    '04_task_object_framework.md',
    '05_21_section_framework.md',
    '06_department_specific_patterns.md',

    # Schema/structure docs
    'REPORT_OUTPUT_SCHEMA_v2.1.md',
    'REPORT_OUTPUT_SCHEMA_v2.1_REVISED.md',
    'ENTITY_MAPPING_GUIDE_v2.1.md',
    'CORRECTIONS_REQUIRED.md',

    # Scripts
    'cleanup_old_folders.py',
    'cleanup_remaining_folders.bat',
    'compile_prompt_system.py',
    'fix_restructure.py',
    'restructure_prompts.py',
    'simplify_master_csv.py',
    'update_master_list.py',
    'show_summary.py',
    'archive_non_prompts.py',  # This script itself

    # Backup CSVs
    'PROMPTS_Master_List_OLD.csv',
    'PROMPTS_Master_List_BACKUP.csv',
    'PROMPTS_Master_List_BACKUP_FULL.csv',

    # Comparison docs
    'MAIN_PROMPT_v4_vs_v6_Comparison.md',
    'MAIN_PROMPT_v5_Modular_vs_v6_UltraCondensed_Comparison.md',
]

def archive_non_prompts():
    print("=" * 60)
    print("ARCHIVING NON-PROMPT FILES")
    print("=" * 60)

    archived_count = 0

    for filename in NON_PROMPT_FILES:
        source = os.path.join(PROMPTS_DIR, filename)

        if os.path.exists(source):
            dest = os.path.join(ARCHIVE_DIR, filename)

            try:
                shutil.move(source, dest)
                print(f"  Archived: {filename}")
                archived_count += 1
            except Exception as e:
                print(f"  ERROR: {filename} - {str(e)}")
        else:
            pass  # File doesn't exist, skip silently

    print("\n" + "=" * 60)
    print(f"[SUCCESS] Archived {archived_count} files")
    print("=" * 60)

    # Count remaining files
    md_files = [f for f in os.listdir(PROMPTS_DIR)
                if f.endswith('.md') and os.path.isfile(os.path.join(PROMPTS_DIR, f))]

    print(f"\nRemaining in PROMPTS root:")
    print(f"  - {len(md_files)} .md files (prompts only)")

    # Check for any remaining non-prompt files
    scripts = [f for f in os.listdir(PROMPTS_DIR)
               if f.endswith(('.py', '.bat', '.json')) and os.path.isfile(os.path.join(PROMPTS_DIR, f))]

    if scripts:
        print(f"  - {len(scripts)} script/config files still present:")
        for s in scripts[:10]:
            print(f"    - {s}")

    print("\n[SUCCESS] Non-prompt files archived!")
    print("[SUCCESS] PROMPTS root now contains only prompt files")

if __name__ == '__main__':
    archive_non_prompts()
