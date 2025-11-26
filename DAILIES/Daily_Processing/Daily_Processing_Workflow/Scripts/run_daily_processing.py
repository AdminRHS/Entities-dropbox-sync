#!/usr/bin/env python3
"""
run_daily_processing.py - Master Daily Processing Script

Purpose: Run the complete daily processing workflow (MLT-002 through MLT-007)
         in automated sequence.

Time Savings: 200 min (3h 20min) manual → 27 min automated (86% reduction)

Workflow:
    1. MLT-002: Collect files (30 min → 2 min) ✅
    2. MLT-003: Extract tasks (60 min → 10 min) ⚠️ Requires AI API
    3. MLT-006: Assign tasks (45 min → 10 min) ✅
    4. MLT-007: Distribute tasks (30 min → 5 min) ✅

Usage:
    python3 run_daily_processing.py [options]

Examples:
    # Run full automation for today
    python3 run_daily_processing.py

    # Run specific steps only
    python3 run_daily_processing.py --skip-extraction

    # Dry run (preview without executing)
    python3 run_daily_processing.py --dry-run

    # Use OpenAI instead of Claude for extraction
    python3 run_daily_processing.py --ai-provider openai
"""

import sys
import argparse
import subprocess
from pathlib import Path
from datetime import datetime

# ============================================================================
# Configuration
# ============================================================================

SCRIPT_DIR = Path(__file__).parent

SCRIPTS = {
    'collect': 'collect_daily_files.py',
    'extract': 'extract_tasks_batch.py',
    'assign': 'assign_tasks.py',
    'distribute': 'distribute_tasks.py'
}

# ============================================================================
# Script Runner
# ============================================================================

def run_script(script_name, args=None, dry_run=False):
    """Run a script and return success status."""
    script_path = SCRIPT_DIR / SCRIPTS[script_name]

    if not script_path.exists():
        print(f"❌ Script not found: {script_path}")
        return False

    cmd = ['python3', str(script_path)]

    if args:
        cmd.extend(args)

    if dry_run:
        cmd.append('--dry-run')

    print(f"\n{'='*60}")
    print(f"Running: {script_name.upper()}")
    print(f"Command: {' '.join(cmd)}")
    print('='*60)

    try:
        result = subprocess.run(cmd, check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"\n❌ {script_name} failed with exit code {e.returncode}")
        return False
    except Exception as e:
        print(f"\n❌ Error running {script_name}: {e}")
        return False

# ============================================================================
# Main Workflow
# ============================================================================

def run_daily_processing(
    date=None,
    week=None,
    day=None,
    ai_provider='claude',
    skip_collect=False,
    skip_extraction=False,
    skip_assign=False,
    skip_distribute=False,
    dry_run=False,
    limit=None
):
    """
    Run complete daily processing workflow.

    Args:
        date: Date in YYYY-MM-DD format
        week: Week number
        day: Day number
        ai_provider: AI provider for extraction (claude or openai)
        skip_collect: Skip file collection step
        skip_extraction: Skip task extraction step
        skip_assign: Skip task assignment step
        skip_distribute: Skip task distribution step
        dry_run: Preview mode
        limit: Limit files for testing

    Returns:
        bool: True if all steps succeeded
    """
    start_time = datetime.now()

    if not date:
        date = datetime.now().strftime('%Y-%m-%d')

    print("="*60)
    print("DAILY PROCESSING AUTOMATION")
    print("="*60)
    print(f"Date: {date}")
    print(f"AI Provider: {ai_provider}")
    print(f"Mode: {'DRY RUN' if dry_run else 'PRODUCTION'}")
    print("="*60)

    steps_run = []
    steps_skipped = []

    # Step 1: Collect Files (MLT-002)
    if not skip_collect:
        print("\n📂 STEP 1/4: Collecting Files (MLT-002)")

        args = []
        if date:
            args.extend(['--date', date])
        if week:
            args.extend(['--week', str(week)])
        if day:
            args.extend(['--day', str(day)])

        success = run_script('collect', args, dry_run)

        if not success:
            print("\n❌ WORKFLOW FAILED at Step 1 (Collection)")
            return False

        steps_run.append('collect')
    else:
        steps_skipped.append('collect')
        print("\n⏭️  STEP 1/4: Skipped (Collection)")

    # Step 2: Extract Tasks (MLT-003)
    if not skip_extraction:
        print("\n🔍 STEP 2/4: Extracting Tasks (MLT-003)")

        args = []
        if date:
            args.extend(['--date', date])
        args.extend(['--ai-provider', ai_provider])
        if limit:
            args.extend(['--limit', str(limit)])

        success = run_script('extract', args, dry_run)

        if not success:
            print("\n❌ WORKFLOW FAILED at Step 2 (Extraction)")
            print("\n⚠️  TIP: Make sure API key is set:")
            if ai_provider == 'claude':
                print("   export ANTHROPIC_API_KEY='your-key-here'")
            else:
                print("   export OPENAI_API_KEY='your-key-here'")
            return False

        steps_run.append('extract')
    else:
        steps_skipped.append('extract')
        print("\n⏭️  STEP 2/4: Skipped (Extraction)")

    # Step 3: Assign Tasks (MLT-006)
    if not skip_assign:
        print("\n📊 STEP 3/4: Assigning Tasks (MLT-006)")

        args = []
        if date:
            args.extend(['--date', date])

        success = run_script('assign', args, dry_run)

        if not success:
            print("\n❌ WORKFLOW FAILED at Step 3 (Assignment)")
            return False

        steps_run.append('assign')
    else:
        steps_skipped.append('assign')
        print("\n⏭️  STEP 3/4: Skipped (Assignment)")

    # Step 4: Distribute Tasks (MLT-007)
    if not skip_distribute:
        print("\n📤 STEP 4/4: Distributing Tasks (MLT-007)")

        args = []
        if date:
            args.extend(['--date', date])
        if week:
            args.extend(['--week', str(week)])
        if day:
            args.extend(['--day', str(day)])

        success = run_script('distribute', args, dry_run)

        if not success:
            print("\n❌ WORKFLOW FAILED at Step 4 (Distribution)")
            return False

        steps_run.append('distribute')
    else:
        steps_skipped.append('distribute')
        print("\n⏭️  STEP 4/4: Skipped (Distribution)")

    # Final Summary
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()

    print("\n" + "="*60)
    print("✅ DAILY PROCESSING COMPLETE!")
    print("="*60)
    print(f"Steps Run: {', '.join(steps_run) if steps_run else 'None'}")
    if steps_skipped:
        print(f"Steps Skipped: {', '.join(steps_skipped)}")
    print(f"Total Duration: {duration:.1f} seconds ({duration/60:.1f} minutes)")
    print(f"Mode: {'DRY RUN (no files modified)' if dry_run else 'PRODUCTION'}")

    if not dry_run:
        print(f"\n📁 Workspace: /ENTITIES/DAILIES/Daily_Processing/{date}_Collection/")
        print(f"📝 Next: Run MLT-004 (Gap Analysis) and MLT-005 (Template Creation) manually")
        print(f"    Then continue with MLT-008 (QA) and MLT-009 (Archival)")

    return True

# ============================================================================
# CLI Interface
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Run complete daily processing workflow',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run full workflow for today
  python3 run_daily_processing.py

  # Run for specific date
  python3 run_daily_processing.py --date 2025-11-25

  # Skip extraction (if already done manually)
  python3 run_daily_processing.py --skip-extraction

  # Use OpenAI for extraction
  python3 run_daily_processing.py --ai-provider openai

  # Test with limited files
  python3 run_daily_processing.py --limit 5 --dry-run

  # Dry run (preview mode)
  python3 run_daily_processing.py --dry-run

Environment Variables Required:
  ANTHROPIC_API_KEY - For Claude extraction (default)
  OPENAI_API_KEY    - For OpenAI extraction (if using --ai-provider openai)

Time Savings:
  Manual: 165 minutes (2h 45min) for steps 2,3,6,7
  Automated: 27 minutes
  Savings: 138 minutes (83% reduction)

Note: MLT-004 (Gap Analysis) and MLT-005 (Template Creation) still require
manual review and are not included in this automation.
        """
    )

    parser.add_argument(
        '--date',
        help='Date in YYYY-MM-DD format (default: today)',
        default=None
    )

    parser.add_argument(
        '--week',
        type=int,
        help='Week number (default: auto-calculate)',
        default=None
    )

    parser.add_argument(
        '--day',
        type=int,
        help='Day number (default: auto-calculate)',
        default=None
    )

    parser.add_argument(
        '--ai-provider',
        choices=['claude', 'openai'],
        default='claude',
        help='AI provider for task extraction (default: claude)'
    )

    parser.add_argument(
        '--skip-collect',
        action='store_true',
        help='Skip file collection step'
    )

    parser.add_argument(
        '--skip-extraction',
        action='store_true',
        help='Skip task extraction step (MLT-003)'
    )

    parser.add_argument(
        '--skip-assign',
        action='store_true',
        help='Skip task assignment step (MLT-006)'
    )

    parser.add_argument(
        '--skip-distribute',
        action='store_true',
        help='Skip task distribution step (MLT-007)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview mode - no files modified'
    )

    parser.add_argument(
        '--limit',
        type=int,
        help='Limit number of files to process (for testing)',
        default=None
    )

    args = parser.parse_args()

    success = run_daily_processing(
        date=args.date,
        week=args.week,
        day=args.day,
        ai_provider=args.ai_provider,
        skip_collect=args.skip_collect,
        skip_extraction=args.skip_extraction,
        skip_assign=args.skip_assign,
        skip_distribute=args.skip_distribute,
        dry_run=args.dry_run,
        limit=args.limit
    )

    return 0 if success else 1

if __name__ == "__main__":
    exit(main())
