#!/usr/bin/env python3
"""
Phase 5: Rollback Migration Script
Restores system to pre-migration state from backup if critical issues found

Author: Claude Code
Date: 2025-11-25
Version: 1.0
"""

import json
import os
import shutil
import zipfile
from datetime import datetime
from pathlib import Path
from typing import Optional

# Configuration
TOOLS_DIR = r"C:\Users\delir\Dropbox\Dropbox\ENTITIES\LIBRARIES\LBS_003_Tools"
LOG_DIR = r"C:\Users\delir\Dropbox\Dropbox\ENTITIES\DAILIES\LOG\Week_4"
REPORT_DIR = r"C:\Users\delir\Dropbox\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4"

# Create output directories
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

# Log file
LOG_FILE = os.path.join(LOG_DIR, f"rollback_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")


def log(message: str, level: str = "INFO"):
    """Log message to console and file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [{level}] {message}"
    print(log_line)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_line + '\n')


class MigrationRollback:
    def __init__(self):
        self.tools_dir = Path(TOOLS_DIR)
        self.log_dir = Path(LOG_DIR)
        self.report_dir = Path(REPORT_DIR)

        log("Migration Rollback Script Initialized")
        log(f"Tools Directory: {self.tools_dir}")

    def find_latest_backup(self) -> Optional[Path]:
        """Find the most recent backup directory or ZIP file"""
        log("=" * 80)
        log("Searching for Latest Backup")
        log("=" * 80)

        parent_dir = self.tools_dir.parent

        # Look for backup ZIPs
        backup_zips = list(parent_dir.glob("LBS_003_Tools_BACKUP_*.zip"))
        backup_zips.sort(key=lambda x: x.stat().st_mtime, reverse=True)

        if backup_zips:
            latest_zip = backup_zips[0]
            log(f"✓ Found backup ZIP: {latest_zip.name}")
            log(f"  Created: {datetime.fromtimestamp(latest_zip.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')}")
            return latest_zip

        # Look for backup directories
        backup_dirs = list(parent_dir.glob("LBS_003_Tools_BACKUP_*"))
        backup_dirs = [d for d in backup_dirs if d.is_dir()]
        backup_dirs.sort(key=lambda x: x.stat().st_mtime, reverse=True)

        if backup_dirs:
            latest_dir = backup_dirs[0]
            log(f"✓ Found backup directory: {latest_dir.name}")
            log(f"  Created: {datetime.fromtimestamp(latest_dir.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')}")
            return latest_dir

        log("✗ No backup found!", "ERROR")
        return None

    def verify_backup(self, backup_path: Path) -> bool:
        """Verify backup integrity"""
        log("=" * 80)
        log("Verifying Backup Integrity")
        log("=" * 80)

        try:
            if backup_path.suffix == '.zip':
                # Verify ZIP can be read
                with zipfile.ZipFile(backup_path, 'r') as zipf:
                    # Test ZIP integrity
                    corrupt = zipf.testzip()
                    if corrupt:
                        log(f"✗ Corrupt file in ZIP: {corrupt}", "ERROR")
                        return False

                    file_list = zipf.namelist()
                    json_files = [f for f in file_list if f.endswith('.json')]
                    log(f"✓ ZIP is valid: {len(json_files)} JSON files found")

                    # Check for manifest
                    manifest_files = [f for f in file_list if 'backup_manifest.json' in f]
                    if manifest_files:
                        manifest_data = zipf.read(manifest_files[0])
                        manifest = json.loads(manifest_data)
                        log(f"✓ Manifest found: {manifest.get('file_count', 0)} files backed up")

                    return True

            else:
                # Verify directory backup
                manifest_path = backup_path / "backup_manifest.json"
                if manifest_path.exists():
                    with open(manifest_path, 'r', encoding='utf-8') as f:
                        manifest = json.load(f)
                    log(f"✓ Manifest found: {manifest.get('file_count', 0)} files backed up")
                    return True
                else:
                    log("⚠ No manifest found, but backup directory exists", "WARNING")
                    # Count JSON files
                    json_files = list(backup_path.rglob('*.json'))
                    log(f"  Found {len(json_files)} JSON files in backup")
                    return len(json_files) > 0

        except Exception as e:
            log(f"✗ Backup verification failed: {str(e)}", "ERROR")
            return False

    def delete_migrated_files(self, dry_run: bool = False) -> int:
        """Delete all TOL-*.json files in root directory"""
        log("=" * 80)
        log(f"{'[DRY RUN] ' if dry_run else ''}Deleting Migrated Files")
        log("=" * 80)

        tol_files = list(self.tools_dir.glob("TOL-*.json"))
        deleted_count = 0

        for file in tol_files:
            if not dry_run:
                file.unlink()
            log(f"{'Would delete' if dry_run else 'Deleted'}: {file.name}")
            deleted_count += 1

        log(f"✓ {deleted_count} migrated files {'would be' if dry_run else ''} deleted")
        return deleted_count

    def restore_from_backup(self, backup_path: Path, dry_run: bool = False) -> bool:
        """Restore files from backup"""
        log("=" * 80)
        log(f"{'[DRY RUN] ' if dry_run else ''}Restoring from Backup")
        log("=" * 80)

        try:
            if backup_path.suffix == '.zip':
                # Restore from ZIP
                log(f"Extracting: {backup_path}")

                if not dry_run:
                    with zipfile.ZipFile(backup_path, 'r') as zipf:
                        # Extract to parent directory
                        zipf.extractall(self.tools_dir.parent)

                    # The ZIP extracts to a directory like LBS_003_Tools_BACKUP_YYYYMMDD_HHMMSS
                    # We need to move contents to LBS_003_Tools
                    extracted_dir = self.tools_dir.parent / backup_path.stem

                    if extracted_dir.exists():
                        # Remove current tools dir
                        if self.tools_dir.exists():
                            shutil.rmtree(self.tools_dir)

                        # Rename backup dir to tools dir
                        extracted_dir.rename(self.tools_dir)
                        log(f"✓ Restored from ZIP: {self.tools_dir}")
                    else:
                        log("✗ Extracted directory not found", "ERROR")
                        return False
                else:
                    log(f"✓ Would extract ZIP to: {self.tools_dir.parent}")

            else:
                # Restore from directory
                log(f"Copying from: {backup_path}")

                if not dry_run:
                    # Remove current tools dir
                    if self.tools_dir.exists():
                        shutil.rmtree(self.tools_dir)

                    # Copy backup to tools dir
                    shutil.copytree(backup_path, self.tools_dir)
                    log(f"✓ Restored from directory: {self.tools_dir}")
                else:
                    log(f"✓ Would copy directory to: {self.tools_dir}")

            return True

        except Exception as e:
            log(f"✗ Restore failed: {str(e)}", "ERROR")
            return False

    def verify_restoration(self) -> bool:
        """Verify restoration was successful"""
        log("=" * 80)
        log("Verifying Restoration")
        log("=" * 80)

        try:
            # Count files
            json_files = list(self.tools_dir.rglob('*.json'))
            json_files = [f for f in json_files if '_ARCHIVE' not in str(f)]

            log(f"✓ Found {len(json_files)} JSON files after restoration")

            # Check for original structure
            subdirs = ['AI_Tools', 'Cloud_Platforms', 'Data_Tools']
            found_subdirs = [d for d in subdirs if (self.tools_dir / d).exists()]

            if found_subdirs:
                log(f"✓ Found {len(found_subdirs)} original subdirectories")
            else:
                log("⚠ No original subdirectories found", "WARNING")

            # Check for TOL- files (should be none)
            tol_files = list(self.tools_dir.glob("TOL-*.json"))
            if tol_files:
                log(f"⚠ Found {len(tol_files)} TOL- files (should be 0)", "WARNING")
                return False

            log("✓ Restoration verification passed")
            return True

        except Exception as e:
            log(f"✗ Verification failed: {str(e)}", "ERROR")
            return False

    def cleanup_migration_artifacts(self, dry_run: bool = False):
        """Remove migration checkpoint and log files"""
        log("=" * 80)
        log(f"{'[DRY RUN] ' if dry_run else ''}Cleaning Up Migration Artifacts")
        log("=" * 80)

        artifacts = [
            self.log_dir / "migration_checkpoint.json",
            self.log_dir / "files_marked_for_deletion.txt",
        ]

        for artifact in artifacts:
            if artifact.exists():
                if not dry_run:
                    artifact.unlink()
                log(f"{'Would remove' if dry_run else 'Removed'}: {artifact.name}")

        log("✓ Migration artifacts cleaned up")

    def run_rollback(self, dry_run: bool = False, reason: str = ""):
        """Execute complete rollback process"""
        log("\n" + "=" * 80)
        log(f"⚠ MIGRATION ROLLBACK {'(DRY RUN)' if dry_run else ''}", "WARNING")
        log("=" * 80)
        log(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        if reason:
            log(f"Reason: {reason}")
        log("=" * 80)

        if not dry_run:
            # Confirm with user
            print("\n⚠ WARNING: This will restore the system to pre-migration state!")
            print("All migrated files will be deleted and replaced with backups.")
            response = input("\nAre you ABSOLUTELY SURE you want to rollback? (type 'ROLLBACK' to confirm): ").strip()

            if response != 'ROLLBACK':
                log("Rollback cancelled by user")
                return False

        # Step 1: Find latest backup
        backup_path = self.find_latest_backup()
        if not backup_path:
            return False

        # Step 2: Verify backup
        if not self.verify_backup(backup_path):
            return False

        # Step 3: Delete migrated files
        deleted_count = self.delete_migrated_files(dry_run=dry_run)

        # Step 4: Restore from backup
        if not self.restore_from_backup(backup_path, dry_run=dry_run):
            return False

        # Step 5: Verify restoration
        if not dry_run:
            if not self.verify_restoration():
                log("✗ Restoration verification failed", "ERROR")
                return False

        # Step 6: Cleanup migration artifacts
        self.cleanup_migration_artifacts(dry_run=dry_run)

        # Generate rollback report
        report = {
            "timestamp": datetime.now().isoformat(),
            "mode": "dry_run" if dry_run else "actual",
            "backup_used": str(backup_path),
            "files_deleted": deleted_count,
            "reason": reason,
            "status": "success"
        }

        report_path = self.report_dir / "rollback_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)

        log("\n" + "=" * 80)
        log("✓ ROLLBACK COMPLETE")
        log("=" * 80)
        log(f"Backup restored: {backup_path.name}")
        log(f"Files deleted: {deleted_count}")
        log(f"Report saved: {report_path}")

        return True


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description='Rollback migration to pre-migration state')
    parser.add_argument('--dry-run', action='store_true', help='Run in dry-run mode (no actual changes)')
    parser.add_argument('--reason', type=str, default='', help='Reason for rollback')

    args = parser.parse_args()

    if args.dry_run:
        print("\n⚠ Running in DRY RUN mode - no actual changes will be made\n")
    else:
        print("\n" + "=" * 80)
        print("⚠ WARNING: MIGRATION ROLLBACK")
        print("=" * 80)
        print("This script will restore the system to pre-migration state.")
        print("All migrated TOL-*.json files will be DELETED and replaced with backups.")
        print("=" * 80 + "\n")

    rollback = MigrationRollback()
    success = rollback.run_rollback(dry_run=args.dry_run, reason=args.reason)

    return 0 if success else 1


if __name__ == "__main__":
    exit(main())