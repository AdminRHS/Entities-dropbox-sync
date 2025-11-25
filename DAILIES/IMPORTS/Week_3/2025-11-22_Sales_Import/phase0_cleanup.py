"""
Phase 0: Cleanup & Archive
Purpose: Archive existing BUSINESSES data and create fresh folder structure

IMPORTANT: Read-only operation on source files
         All modifications are in BUSINESSES/ and IMPORTS/ folders only
"""

import os
import sys
import shutil
from datetime import datetime
import json

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Configuration
BASE_DIR = r"C:\Users\Dell\Dropbox\ENTITIES"
BUSINESSES_DIR = os.path.join(BASE_DIR, "BUSINESSES")
IMPORTS_DIR = os.path.join(BASE_DIR, "IMPORTS", "2025-11-22_Sales_Import")
ARCHIVE_DIR = os.path.join(IMPORTS_DIR, "archive_2025-11-22")
CHECKPOINT_DIR = os.path.join(IMPORTS_DIR, "checkpoints", "phase_0")

# Timestamp
TIMESTAMP = datetime.now().isoformat()

def create_directories():
    """Create necessary directories"""
    print("Creating directory structure...")

    # Create imports directory
    os.makedirs(IMPORTS_DIR, exist_ok=True)
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    os.makedirs(CHECKPOINT_DIR, exist_ok=True)

    print(f"✓ Created IMPORTS directory: {IMPORTS_DIR}")
    print(f"✓ Created ARCHIVE directory: {ARCHIVE_DIR}")
    print(f"✓ Created CHECKPOINT directory: {CHECKPOINT_DIR}")

def archive_existing_data():
    """Archive existing BUSINESSES data"""
    print("\nArchiving existing data...")

    archived_items = []

    # Items to archive
    items_to_archive = [
        "Clients",
        "Prospects",
        "Ex_Clients",
        "BUSINESSES_Master.json"
    ]

    for item in items_to_archive:
        source_path = os.path.join(BUSINESSES_DIR, item)

        if os.path.exists(source_path):
            dest_path = os.path.join(ARCHIVE_DIR, item)

            if os.path.isdir(source_path):
                shutil.copytree(source_path, dest_path)
                print(f"✓ Archived folder: {item}")
            else:
                shutil.copy2(source_path, dest_path)
                print(f"✓ Archived file: {item}")

            archived_items.append({
                "item": item,
                "type": "directory" if os.path.isdir(source_path) else "file",
                "archived_at": TIMESTAMP,
                "original_path": source_path,
                "archive_path": dest_path
            })
        else:
            print(f"⚠ Not found (skipping): {item}")

    return archived_items

def create_folder_structure():
    """Create fresh folder structure for BUSINESSES"""
    print("\nCreating folder structure...")

    folders = [
        # Entity folders
        "Clients",
        "Prospects",
        "Ex_Clients",

        # Schema folder
        "schemas",

        # Root lookup folders
        "Industries",
        "SubIndustries",
        "Positions",
        "CompanySizes",
        "LeadStatuses",
        "LeadSources",
        "Countries",
        "ContactTypes",
        "Templates",

        # JobRequests nested folders
        "JobRequests",
        "JobRequests/Professions",
        "JobRequests/Rates",
        "JobRequests/Shifts",
        "JobRequests/Tools",
        "JobRequests/Languages",
        "JobRequests/LanguageLevels"
    ]

    created_folders = []

    for folder in folders:
        folder_path = os.path.join(BUSINESSES_DIR, folder)
        os.makedirs(folder_path, exist_ok=True)
        created_folders.append(folder)
        print(f"✓ Created: {folder}")

    return created_folders

def create_readme_files():
    """Create README files for key folders"""
    print("\nCreating README files...")

    readmes = {
        "schemas/README.md": """# BUSINESSES Schemas

This folder contains JSON schemas and validation rules for the BUSINESSES entity.

## Files
- `BUSINESSES_SCHEMA.json` - Main JSON schema (Phase 1)
- `field_definitions.md` - Human-readable field documentation
- `validation_rules.json` - Validation specifications
""",

        "JobRequests/README.md": """# Job Requests Lookup Tables

This folder contains lookup tables for job request-related data.

## Subfolders
- `Professions/` - Job professions/roles
- `Rates/` - Rate levels (Junior, Mid, Senior, etc.)
- `Shifts/` - Shift types (Full-time, Part-time, etc.)
- `Tools/` - Required tools/technologies
- `Languages/` - Languages
- `LanguageLevels/` - Language proficiency levels
""",

        "Templates/README.md": """# Templates

This folder contains reusable templates for communication.

## Template Types
- Message templates (LinkedIn, SMS)
- Email templates
- Call summary templates
- First call event templates
"""
    }

    for filepath, content in readmes.items():
        full_path = os.path.join(BUSINESSES_DIR, filepath)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Created: {filepath}")

def generate_report(archived_items, created_folders):
    """Generate Phase 0 cleanup report"""
    print("\nGenerating report...")

    report = {
        "phase": "Phase 0 - Cleanup & Archive",
        "executed_at": TIMESTAMP,
        "status": "completed",
        "summary": {
            "archived_items": len(archived_items),
            "folders_created": len(created_folders)
        },
        "archived_items": archived_items,
        "created_folders": created_folders,
        "archive_location": ARCHIVE_DIR,
        "businesses_location": BUSINESSES_DIR
    }

    # Save JSON report
    report_json_path = os.path.join(IMPORTS_DIR, "phase0_cleanup_report.json")
    with open(report_json_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)

    # Save Markdown report
    report_md_path = os.path.join(IMPORTS_DIR, "phase0_cleanup_report.md")
    with open(report_md_path, 'w', encoding='utf-8') as f:
        f.write(f"# Phase 0: Cleanup & Archive Report\n\n")
        f.write(f"**Executed:** {TIMESTAMP}\n")
        f.write(f"**Status:** Completed\n\n")

        f.write(f"## Summary\n\n")
        f.write(f"- **Archived Items:** {len(archived_items)}\n")
        f.write(f"- **Folders Created:** {len(created_folders)}\n")
        f.write(f"- **Archive Location:** `{ARCHIVE_DIR}`\n\n")

        f.write(f"## Archived Items\n\n")
        for item in archived_items:
            f.write(f"- **{item['item']}** ({item['type']})\n")
            f.write(f"  - Original: `{item['original_path']}`\n")
            f.write(f"  - Archived: `{item['archive_path']}`\n\n")

        f.write(f"## Created Folders\n\n")
        for folder in created_folders:
            f.write(f"- `BUSINESSES/{folder}/`\n")

        f.write(f"\n## Next Step\n\n")
        f.write(f"Proceed to **Phase 1: Schema Definition**\n")

    print(f"✓ JSON report: {report_json_path}")
    print(f"✓ Markdown report: {report_md_path}")

    return report

def create_checkpoint():
    """Create checkpoint for rollback capability"""
    print("\nCreating checkpoint...")

    checkpoint = {
        "phase": "phase_0",
        "timestamp": TIMESTAMP,
        "status": "completed",
        "can_rollback": True,
        "rollback_instructions": f"Restore from {ARCHIVE_DIR}"
    }

    checkpoint_path = os.path.join(CHECKPOINT_DIR, "checkpoint.json")
    with open(checkpoint_path, 'w', encoding='utf-8') as f:
        json.dump(checkpoint, f, indent=2)

    print(f"✓ Checkpoint saved: {checkpoint_path}")

def main():
    """Main execution"""
    print("="*60)
    print("PHASE 0: CLEANUP & ARCHIVE")
    print("="*60)
    print(f"Timestamp: {TIMESTAMP}\n")

    try:
        # Step 1: Create directories
        create_directories()

        # Step 2: Archive existing data
        archived_items = archive_existing_data()

        # Step 3: Create folder structure
        created_folders = create_folder_structure()

        # Step 4: Create README files
        create_readme_files()

        # Step 5: Generate report
        report = generate_report(archived_items, created_folders)

        # Step 6: Create checkpoint
        create_checkpoint()

        print("\n" + "="*60)
        print("PHASE 0 COMPLETED SUCCESSFULLY")
        print("="*60)
        print(f"\n✓ Archived {len(archived_items)} items")
        print(f"✓ Created {len(created_folders)} folders")
        print(f"✓ Reports saved to: {IMPORTS_DIR}")
        print(f"\nNext: Review phase0_cleanup_report.md and proceed to Phase 1")

    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        raise

if __name__ == "__main__":
    main()
