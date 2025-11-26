#!/usr/bin/env python3
"""
Complete Migration Orchestrator
Runs all migration phases in sequence: Phases 1-5

Author: Claude Code
Date: 2025-11-25
Version: 1.0
"""

import sys
import os
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from migrate_tools_to_tol import ToolMigration
from phase4_update_cross_references import CrossReferenceUpdater


def print_banner(text: str):
    """Print formatted banner"""
    print("\n" + "=" * 80)
    print(text.center(80))
    print("=" * 80 + "\n")


def main():
    """Run complete migration process"""
    import argparse

    parser = argparse.ArgumentParser(description='Run complete tool migration (all phases)')
    parser.add_argument('--dry-run', action='store_true', help='Run in dry-run mode (no actual changes)')
    parser.add_argument('--skip-phase4', action='store_true', help='Skip Phase 4 (cross-reference updates)')

    args = parser.parse_args()

    print_banner("TOOL ID MIGRATION: COMPLETE PROCESS")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'ACTUAL EXECUTION'}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if not args.dry_run:
        print("\n⚠ WARNING: This will modify your tool files and dependent systems!")
        response = input("\nProceed with migration? (yes/no): ").strip().lower()
        if response != 'yes':
            print("Migration cancelled.")
            return 1

    # PHASES 1-3: Main Migration
    print_banner("PHASES 1-3: Tool File Migration")
    migration = ToolMigration()
    success = migration.run_full_migration(dry_run=args.dry_run)

    if not success:
        print("\n✗ Migration failed. Check logs for details.")
        return 1

    # PHASE 4: Cross-Reference Updates
    if not args.skip_phase4 and not args.dry_run:
        print_banner("PHASE 4: Cross-Reference Updates")

        # Ask user if they want to proceed with Phase 4
        response = input("\nProceed with cross-reference updates? (yes/no): ").strip().lower()
        if response == 'yes':
            updater = CrossReferenceUpdater()
            success = updater.run_update(dry_run=False)

            if not success:
                print("\n⚠ Cross-reference updates failed. Migration files are still valid.")
                print("You can run phase4_update_cross_references.py separately later.")
        else:
            print("\nSkipping cross-reference updates.")
            print("Run 'python phase4_update_cross_references.py' when ready.")

    print_banner("MIGRATION COMPLETE")
    print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\nNext Steps:")
    print("1. Review validation reports in REPORTS/Week_4/")
    print("2. Spot-check migrated files")
    if args.skip_phase4 or args.dry_run:
        print("3. Run Phase 4: python phase4_update_cross_references.py")
    print("4. Update README.md documentation")
    print("5. Generate final migration report")
    print("\nIf issues found, run: python phase5_rollback_migration.py")

    return 0


if __name__ == "__main__":
    sys.exit(main())