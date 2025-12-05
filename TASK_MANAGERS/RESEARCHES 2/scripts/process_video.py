"""
Process Video - Master Orchestrator
End-to-end automation for video transcription taxonomy integration
Coordinates all scripts: ID scanner → Gap analyzer → JSON updater → Reporter

Purpose: Automate complete video processing workflow (Phases 5-7)
Time Saved: 1.5-2 hours → 5-10 minutes per video

Usage:
    python process_video.py Video_024
    python process_video.py Video_024 --dry-run
    python process_video.py Video_024 --auto-approve --skip-report
    python process_video.py Video_024 --phase gap-analysis
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, Optional
from datetime import datetime

from config import *
from utils import logger, log_summary
from video_id_scanner import VideoIDScanner
from video_gap_analyzer import VideoGapAnalyzer
from video_json_updater import VideoJSONUpdater
from video_integration_reporter import VideoIntegrationReporter


class VideoProcessor:
    """Master orchestrator for end-to-end video processing"""

    def __init__(self, video_id: str, dry_run: bool = False):
        self.video_id = video_id
        self.dry_run = dry_run
        self.transcription_path = TRANSCRIPTIONS_PATH / f"{video_id}.md"

        # Processing results
        self.results = {
            "video_id": video_id,
            "start_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "end_time": None,
            "phases_completed": [],
            "id_scan": {},
            "gap_analysis": {},
            "updates": {},
            "report": {},
            "errors": []
        }

    def process(self,
                auto_approve: bool = False,
                skip_update: bool = False,
                skip_report: bool = False,
                phase: Optional[str] = None) -> Dict[str, any]:
        """
        Execute complete video processing workflow

        Args:
            auto_approve: Skip confirmation prompts
            skip_update: Skip JSON update phase
            skip_report: Skip report generation phase
            phase: Run specific phase only (id-scan, gap-analysis, update, report)

        Returns:
            Dictionary with processing results
        """
        logger.info(f"{'='*60}")
        logger.info(f"VIDEO PROCESSING WORKFLOW: {self.video_id}")
        logger.info(f"{'='*60}")

        if self.dry_run:
            logger.info("DRY RUN MODE - No files will be modified")

        # Validate transcription exists
        if not self.validate_transcription():
            return self.results

        try:
            # Phase 1: ID Scan
            if not phase or phase == "id-scan":
                self.phase_id_scan()

            # Phase 2: Gap Analysis
            if not phase or phase == "gap-analysis":
                self.phase_gap_analysis()

            # Phase 3: JSON Updates
            if not phase or phase == "update":
                if not skip_update:
                    self.phase_json_update(auto_approve=auto_approve)
                else:
                    logger.info("Skipping JSON update phase (--skip-update)")

            # Phase 4: Report Generation
            if not phase or phase == "report":
                if not skip_report:
                    self.phase_generate_report()
                else:
                    logger.info("Skipping report generation phase (--skip-report)")

            # Mark completion
            self.results['end_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.results['status'] = 'completed'

            # Final summary
            self.print_final_summary()

        except KeyboardInterrupt:
            logger.warning("\nProcess interrupted by user")
            self.results['status'] = 'interrupted'

        except Exception as e:
            logger.error(f"Processing error: {e}")
            self.results['errors'].append(str(e))
            self.results['status'] = 'failed'

        return self.results

    def validate_transcription(self) -> bool:
        """Validate that transcription file exists"""
        if not self.transcription_path.exists():
            error_msg = f"Transcription not found: {self.transcription_path}"
            logger.error(error_msg)
            self.results['errors'].append(error_msg)
            self.results['status'] = 'failed'
            return False

        logger.info(f"Transcription found: {self.transcription_path}")
        return True

    def phase_id_scan(self):
        """Phase 1: Scan for next available IDs"""
        logger.info("\n" + "="*60)
        logger.info("PHASE 1: ID SCAN")
        logger.info("="*60)

        try:
            scanner = VideoIDScanner()
            next_ids = scanner.scan_all()

            self.results['id_scan'] = next_ids
            self.results['phases_completed'].append('id_scan')

            logger.info("ID scan completed successfully")

            # Print summary
            logger.info("\nNext Available IDs:")
            for entity_type, id_value in next_ids.items():
                logger.info(f"  {entity_type}: {id_value}")

        except Exception as e:
            error_msg = f"ID scan failed: {e}"
            logger.error(error_msg)
            self.results['errors'].append(error_msg)
            raise

    def phase_gap_analysis(self):
        """Phase 2: Analyze gaps between transcription and LIBRARIES"""
        logger.info("\n" + "="*60)
        logger.info("PHASE 2: GAP ANALYSIS")
        logger.info("="*60)

        try:
            analyzer = VideoGapAnalyzer(self.video_id)
            analysis_results = analyzer.analyze()

            self.results['gap_analysis'] = analysis_results
            self.results['phases_completed'].append('gap_analysis')

            logger.info("Gap analysis completed successfully")

            # Print summary
            summary = analysis_results.get('summary', {})
            logger.info(f"\nGap Analysis Summary:")
            logger.info(f"  Total NEW entities: {summary.get('total_new', 0)}")
            logger.info(f"  Total EXISTING entities: {summary.get('total_exists', 0)}")
            logger.info(f"  Total UPDATE entities: {summary.get('total_update', 0)}")

            # Save gap analysis report
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            gap_report_path = ANALYSIS_PATH / f"gap_analysis_{self.video_id}_{timestamp}.md"
            analyzer.save_report(gap_report_path, format="markdown")

            logger.info(f"\nGap analysis report saved: {gap_report_path}")

        except Exception as e:
            error_msg = f"Gap analysis failed: {e}"
            logger.error(error_msg)
            self.results['errors'].append(error_msg)
            raise

    def phase_json_update(self, auto_approve: bool = False):
        """Phase 3: Update JSON files with new entities"""
        logger.info("\n" + "="*60)
        logger.info("PHASE 3: JSON UPDATE")
        logger.info("="*60)

        if self.dry_run:
            logger.info("DRY RUN - Simulating updates only")

        try:
            updater = VideoJSONUpdater(self.video_id, dry_run=self.dry_run)
            update_results = updater.update_all(auto_approve=auto_approve)

            self.results['updates'] = update_results
            self.results['phases_completed'].append('json_update')

            logger.info("JSON update completed successfully")

            # Print summary
            summary = update_results.get('summary', {})
            logger.info(f"\nUpdate Summary:")
            logger.info(f"  Total updates: {summary.get('total_updates', 0)}")
            logger.info(f"  Total errors: {summary.get('total_errors', 0)}")

            if summary.get('total_errors', 0) > 0:
                logger.warning(f"  Errors occurred during update:")
                for error in summary.get('errors', []):
                    logger.warning(f"    - {error}")

        except Exception as e:
            error_msg = f"JSON update failed: {e}"
            logger.error(error_msg)
            self.results['errors'].append(error_msg)
            raise

    def phase_generate_report(self):
        """Phase 4: Generate integration report"""
        logger.info("\n" + "="*60)
        logger.info("PHASE 4: REPORT GENERATION")
        logger.info("="*60)

        try:
            reporter = VideoIntegrationReporter(self.video_id)
            report_data = reporter.generate_report(include_cross_refs=True)

            self.results['report'] = report_data
            self.results['phases_completed'].append('report_generation')

            logger.info("Report generation completed successfully")

            # Save report
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            report_path = REPORTS_PATH / f"integration_report_{self.video_id}_{timestamp}.md"
            reporter.save_report(report_path, format="markdown")

            # Also save JSON version
            json_report_path = REPORTS_PATH / f"integration_report_{self.video_id}_{timestamp}.json"
            reporter.save_report(json_report_path, format="json")

            logger.info(f"\nReports saved:")
            logger.info(f"  Markdown: {report_path}")
            logger.info(f"  JSON: {json_report_path}")

        except Exception as e:
            error_msg = f"Report generation failed: {e}"
            logger.error(error_msg)
            self.results['errors'].append(error_msg)
            raise

    def print_final_summary(self):
        """Print final processing summary"""
        logger.info("\n" + "="*60)
        logger.info("PROCESSING COMPLETE")
        logger.info("="*60)

        logger.info(f"Video ID: {self.video_id}")
        logger.info(f"Status: {self.results.get('status', 'unknown')}")
        logger.info(f"Start Time: {self.results['start_time']}")
        logger.info(f"End Time: {self.results['end_time']}")
        logger.info(f"\nPhases Completed: {len(self.results['phases_completed'])}/4")

        for phase in self.results['phases_completed']:
            logger.info(f"  ✓ {phase}")

        # Summary statistics
        if self.results.get('gap_analysis'):
            summary = self.results['gap_analysis'].get('summary', {})
            logger.info(f"\nEntity Statistics:")
            logger.info(f"  New: {summary.get('total_new', 0)}")
            logger.info(f"  Existing: {summary.get('total_exists', 0)}")
            logger.info(f"  Updates: {summary.get('total_update', 0)}")

        if self.results.get('updates'):
            update_summary = self.results['updates'].get('summary', {})
            logger.info(f"\nUpdates Made:")
            logger.info(f"  Total: {update_summary.get('total_updates', 0)}")
            logger.info(f"  Errors: {update_summary.get('total_errors', 0)}")

        # Errors
        if self.results['errors']:
            logger.warning(f"\nErrors Encountered: {len(self.results['errors'])}")
            for error in self.results['errors']:
                logger.warning(f"  - {error}")

        logger.info("="*60)

        # Time saved estimate
        if self.results.get('status') == 'completed':
            logger.info("\n✓ Process automated successfully!")
            logger.info("  Time saved: ~1.5-2 hours → 5-10 minutes")


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(
        description="Master orchestrator for end-to-end video processing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Full processing with prompts
  python process_video.py Video_024

  # Dry run (preview only)
  python process_video.py Video_024 --dry-run

  # Automated processing (no prompts)
  python process_video.py Video_024 --auto-approve

  # Run specific phase only
  python process_video.py Video_024 --phase gap-analysis

  # Skip certain phases
  python process_video.py Video_024 --skip-update --skip-report
        """
    )

    parser.add_argument(
        'video_id',
        type=str,
        help='Video ID to process (e.g., Video_024)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without modifying files'
    )

    parser.add_argument(
        '--auto-approve',
        action='store_true',
        help='Skip all confirmation prompts'
    )

    parser.add_argument(
        '--skip-update',
        action='store_true',
        help='Skip JSON update phase'
    )

    parser.add_argument(
        '--skip-report',
        action='store_true',
        help='Skip report generation phase'
    )

    parser.add_argument(
        '--phase',
        choices=['id-scan', 'gap-analysis', 'update', 'report'],
        help='Run specific phase only'
    )

    args = parser.parse_args()

    # Validate arguments
    if args.skip_update and args.phase == 'update':
        print("Error: Cannot use --skip-update with --phase update")
        sys.exit(1)

    if args.skip_report and args.phase == 'report':
        print("Error: Cannot use --skip-report with --phase report")
        sys.exit(1)

    # Initialize processor
    processor = VideoProcessor(args.video_id, dry_run=args.dry_run)

    # Run processing
    results = processor.process(
        auto_approve=args.auto_approve,
        skip_update=args.skip_update,
        skip_report=args.skip_report,
        phase=args.phase
    )

    # Exit with appropriate code
    if results.get('status') == 'completed':
        sys.exit(0)
    elif results.get('status') == 'interrupted':
        sys.exit(130)  # Standard exit code for SIGINT
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
