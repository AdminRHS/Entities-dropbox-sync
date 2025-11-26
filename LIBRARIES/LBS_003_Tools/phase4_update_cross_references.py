#!/usr/bin/env python3
"""
Phase 4: Cross-Reference Update Script
Updates all TOOL-[CAT]-### IDs to new TOL-### IDs in dependent systems

Author: Claude Code
Date: 2025-11-25
Version: 1.0
"""

import json
import os
import csv
from datetime import datetime
from pathlib import Path
from typing import Dict, List
import re

# Configuration
BASE_DIR = r"C:\Users\delir\Dropbox\Dropbox\ENTITIES"
MAPPING_CSV = r"C:\Users\delir\Dropbox\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4\migration_mapping_table.csv"
LOG_DIR = r"C:\Users\delir\Dropbox\Dropbox\ENTITIES\DAILIES\LOG\Week_4"
REPORT_DIR = r"C:\Users\delir\Dropbox\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4"

# Directories to scan for references
SCAN_DIRS = [
    os.path.join(BASE_DIR, "TASK_MANAGERS", "Task_Templates"),
    os.path.join(BASE_DIR, "TASK_MANAGERS", "Workflows"),
    os.path.join(BASE_DIR, "TASK_MANAGERS", "Step_Templates"),
    os.path.join(BASE_DIR, "LIBRARIES", "Responsibilities"),
    os.path.join(BASE_DIR, "LIBRARIES", "Skills"),
]

# Create output directories
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

# Log file
LOG_FILE = os.path.join(LOG_DIR, f"references_updated_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")


def log(message: str, level: str = "INFO"):
    """Log message to console and file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [{level}] {message}"
    print(log_line)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_line + '\n')


class CrossReferenceUpdater:
    def __init__(self):
        self.mapping_csv = Path(MAPPING_CSV)
        self.id_mapping: Dict[str, str] = {}
        self.files_scanned = 0
        self.files_updated = 0
        self.total_references_updated = 0
        self.update_details: List[Dict] = []

        log("Cross-Reference Update Script Initialized")

    def load_id_mapping(self) -> bool:
        """Load ID mapping from migration mapping table"""
        log("=" * 80)
        log("Loading ID Mapping from Migration Table")
        log("=" * 80)

        try:
            if not self.mapping_csv.exists():
                log(f"✗ Mapping CSV not found: {self.mapping_csv}", "ERROR")
                return False

            with open(self.mapping_csv, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    old_id = row.get('current_tool_id', '').strip()
                    new_id = row.get('new_tol_id', '').strip()

                    if old_id and new_id and new_id != 'UNMAPPED':
                        self.id_mapping[old_id] = new_id

            log(f"✓ Loaded {len(self.id_mapping)} ID mappings")

            # Show sample mappings
            log("Sample mappings:")
            for i, (old, new) in enumerate(list(self.id_mapping.items())[:5]):
                log(f"  {old} → {new}")

            return True

        except Exception as e:
            log(f"✗ Failed to load ID mapping: {str(e)}", "ERROR")
            return False

    def update_json_file(self, filepath: str, dry_run: bool = False) -> int:
        """
        Update tool IDs in a single JSON file
        Returns: number of references updated
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content
            updates_in_file = 0

            # Replace each old ID with new ID
            for old_id, new_id in self.id_mapping.items():
                # Count occurrences
                count = content.count(old_id)
                if count > 0:
                    # Replace all occurrences
                    content = content.replace(old_id, new_id)
                    updates_in_file += count

                    log(f"  → Replaced {count}x: {old_id} → {new_id}")

            # If changes were made, write back
            if updates_in_file > 0 and not dry_run:
                # Validate JSON before writing
                try:
                    json.loads(content)
                except json.JSONDecodeError as e:
                    log(f"✗ JSON validation failed after replacement: {filepath}", "ERROR")
                    log(f"  Error: {str(e)}", "ERROR")
                    return 0

                # Write updated content
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

            return updates_in_file

        except json.JSONDecodeError:
            log(f"⚠ Skipping invalid JSON: {filepath}", "WARNING")
            return 0
        except Exception as e:
            log(f"✗ Error updating {filepath}: {str(e)}", "ERROR")
            return 0

    def scan_directory(self, directory: str, dry_run: bool = False):
        """Scan directory recursively and update all JSON files"""
        if not os.path.exists(directory):
            log(f"⚠ Directory not found, skipping: {directory}", "WARNING")
            return

        log(f"\nScanning: {directory}")

        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.json'):
                    filepath = os.path.join(root, file)
                    rel_path = os.path.relpath(filepath, BASE_DIR)

                    self.files_scanned += 1

                    # Update file
                    updates = self.update_json_file(filepath, dry_run=dry_run)

                    if updates > 0:
                        self.files_updated += 1
                        self.total_references_updated += updates

                        status = "DRY RUN" if dry_run else "UPDATED"
                        log(f"✓ [{status}] {rel_path}: {updates} reference(s)")

                        self.update_details.append({
                            'file': rel_path,
                            'references_updated': updates
                        })

    def run_update(self, dry_run: bool = False):
        """Run complete cross-reference update"""
        log("\n" + "=" * 80)
        log(f"PHASE 4: CROSS-REFERENCE UPDATE {'(DRY RUN)' if dry_run else ''}")
        log("=" * 80)
        log(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        log("=" * 80)

        if dry_run:
            log("⚠ DRY RUN MODE - No actual changes will be made", "WARNING")

        # Load ID mapping
        if not self.load_id_mapping():
            return False

        # Scan each directory
        for scan_dir in SCAN_DIRS:
            self.scan_directory(scan_dir, dry_run=dry_run)

        # Generate summary report
        summary = {
            "timestamp": datetime.now().isoformat(),
            "mode": "dry_run" if dry_run else "actual",
            "files_scanned": self.files_scanned,
            "files_updated": self.files_updated,
            "total_references_updated": self.total_references_updated,
            "id_mappings_used": len(self.id_mapping),
            "update_details": self.update_details
        }

        # Save summary report
        summary_path = os.path.join(REPORT_DIR, "reference_update_summary.json")
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)

        # Save detailed log
        log_path = os.path.join(LOG_DIR, "references_updated_log.txt")
        with open(log_path, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write(f"Cross-Reference Update Report\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")

            f.write(f"Files Scanned: {self.files_scanned}\n")
            f.write(f"Files Updated: {self.files_updated}\n")
            f.write(f"Total References Updated: {self.total_references_updated}\n\n")

            f.write("Updated Files:\n")
            f.write("-" * 80 + "\n")
            for detail in self.update_details:
                f.write(f"  {detail['file']}: {detail['references_updated']} reference(s)\n")

        log("\n" + "=" * 80)
        log("✓ CROSS-REFERENCE UPDATE COMPLETE")
        log("=" * 80)
        log(f"Files scanned: {self.files_scanned}")
        log(f"Files updated: {self.files_updated}")
        log(f"Total references updated: {self.total_references_updated}")
        log(f"Summary saved: {summary_path}")
        log(f"Detailed log saved: {log_path}")

        return True


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description='Update cross-references from TOOL-[CAT]-### to TOL-###')
    parser.add_argument('--dry-run', action='store_true', help='Run in dry-run mode (no actual changes)')

    args = parser.parse_args()

    if args.dry_run:
        print("\n⚠ Running in DRY RUN mode - no actual changes will be made\n")

    updater = CrossReferenceUpdater()
    success = updater.run_update(dry_run=args.dry_run)

    return 0 if success else 1


if __name__ == "__main__":
    exit(main())