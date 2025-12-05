"""
Video Integration Reporter - Script 4
Generate comprehensive integration reports after video processing
Includes statistics, cross-references, and validation results

Purpose: Create detailed reports of video taxonomy integration
Time Saved: 20-30 minutes per video

Usage:
    python video_integration_reporter.py Video_023
    python video_integration_reporter.py Video_023 --format json
    python video_integration_reporter.py Video_023 --include-cross-refs
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List, Set
from datetime import datetime

from config import *
from utils import logger, log_summary, load_json, create_markdown_table
from video_gap_analyzer import VideoGapAnalyzer
from markdown_parser import MarkdownTranscriptionParser


class VideoIntegrationReporter:
    """Generates comprehensive integration reports"""

    def __init__(self, video_id: str):
        self.video_id = video_id
        self.transcription_path = TRANSCRIPTIONS_PATH / f"{video_id}.md"
        self.parser = None
        self.analyzer = None

        # Report data
        self.report_data = {}

    def generate_report(self, include_cross_refs: bool = False) -> Dict[str, any]:
        """
        Generate comprehensive integration report

        Args:
            include_cross_refs: Whether to include cross-reference validation

        Returns:
            Dictionary with report data
        """
        logger.info(f"Generating integration report for {self.video_id}...")

        # Step 1: Load transcription
        if not self.load_transcription():
            return {}

        # Step 2: Run gap analysis
        self.analyzer = VideoGapAnalyzer(self.video_id)
        analysis_results = self.analyzer.analyze()

        # Step 3: Collect statistics
        stats = self.collect_statistics(analysis_results)

        # Step 4: Generate entity summaries
        entity_summaries = self.generate_entity_summaries(analysis_results)

        # Step 5: Cross-reference validation (if requested)
        cross_ref_report = {}
        if include_cross_refs:
            cross_ref_report = self.validate_cross_references()

        # Step 6: Generate recommendations
        recommendations = self.generate_recommendations(analysis_results)

        # Build report data
        self.report_data = {
            "video_id": self.video_id,
            "report_date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "statistics": stats,
            "entity_summaries": entity_summaries,
            "cross_references": cross_ref_report,
            "recommendations": recommendations,
            "next_ids": analysis_results.get('next_ids', {})
        }

        log_summary("Integration Report Generated", {
            "Video": self.video_id,
            "Total Entities": stats['total_entities'],
            "New Entities": stats['total_new'],
            "Existing Entities": stats['total_existing']
        })

        return self.report_data

    def load_transcription(self) -> bool:
        """Load and parse markdown transcription file"""
        try:
            if not self.transcription_path.exists():
                logger.error(f"Transcription not found: {self.transcription_path}")
                return False

            logger.info(f"Loading transcription: {self.transcription_path}")
            self.parser = MarkdownTranscriptionParser(self.transcription_path)
            self.parser.parse_all_sections()

            return True

        except Exception as e:
            logger.error(f"Error loading transcription: {e}")
            return False

    def collect_statistics(self, analysis_results: Dict) -> Dict[str, any]:
        """Collect overall statistics"""
        summary = analysis_results.get('summary', {})

        stats = {
            "total_entities": summary.get('total_new', 0) + summary.get('total_exists', 0),
            "total_new": summary.get('total_new', 0),
            "total_existing": summary.get('total_exists', 0),
            "total_updates": summary.get('total_update', 0),
            "by_type": summary.get('by_type', {}),
            "integration_rate": 0.0
        }

        # Calculate integration rate (new entities / total entities)
        if stats['total_entities'] > 0:
            stats['integration_rate'] = (stats['total_new'] / stats['total_entities']) * 100

        return stats

    def generate_entity_summaries(self, analysis_results: Dict) -> Dict[str, List[Dict]]:
        """Generate detailed summaries for each entity type"""
        gaps = analysis_results.get('gaps', {})
        summaries = {}

        for entity_type, entities in gaps.items():
            type_summary = {
                "new": [],
                "existing": [],
                "update": []
            }

            # Summarize new entities
            for entity in entities.get('new', []):
                type_summary['new'].append({
                    "name": entity.get('name'),
                    "next_id": entity.get('next_id'),
                    "category": entity.get('category', 'N/A')
                })

            # Summarize existing entities
            for entity in entities.get('exists', []):
                type_summary['existing'].append({
                    "name": entity.get('name'),
                    "id": entity.get('id'),
                    "status": "Already in LIBRARIES"
                })

            # Summarize updates
            for entity in entities.get('update', []):
                type_summary['update'].append({
                    "name": entity.get('name'),
                    "id": entity.get('id'),
                    "reason": entity.get('reason', 'Review needed')
                })

            summaries[entity_type] = type_summary

        return summaries

    def validate_cross_references(self) -> Dict[str, any]:
        """Validate cross-references between entities"""
        logger.info("Validating cross-references...")

        validation_results = {
            "workflows": [],
            "tools": [],
            "skills": [],
            "professions": [],
            "issues_found": []
        }

        # Validate workflow cross-references
        workflows = self.parser.sections.get('workflows', [])

        for workflow in workflows:
            workflow_name = workflow.get('name')
            tools = workflow.get('tools', [])
            skills = workflow.get('skills_required', [])

            # Check if all referenced tools exist
            for tool in tools:
                if not self.tool_exists(tool):
                    validation_results['issues_found'].append({
                        "type": "missing_tool",
                        "workflow": workflow_name,
                        "tool": tool,
                        "severity": "medium"
                    })

            # Check if all referenced skills exist
            for skill in skills:
                if not self.skill_exists(skill):
                    validation_results['issues_found'].append({
                        "type": "missing_skill",
                        "workflow": workflow_name,
                        "skill": skill,
                        "severity": "low"
                    })

        validation_results['total_issues'] = len(validation_results['issues_found'])

        return validation_results

    def tool_exists(self, tool_name: str) -> bool:
        """Check if tool exists in LIBRARIES"""
        tool_name_lower = tool_name.lower()

        tool_categories = {
            "AI": TOOLS_PATH / "AI_Tools",
            "CLOUD": TOOLS_PATH / "Cloud_Platforms",
            "SMM": TOOLS_PATH / "Social_Media_Platforms",
            "VID": TOOLS_PATH / "Video_Editing_Tools",
            "DEV": TOOLS_PATH / "Development_Tools"
        }

        for category_dir in tool_categories.values():
            if category_dir.exists():
                for file in category_dir.glob("*.json"):
                    try:
                        data = load_json(file)
                        if data.get('tool_name', '').lower() == tool_name_lower:
                            return True
                    except:
                        continue

        return False

    def skill_exists(self, skill_name: str) -> bool:
        """Check if skill exists in LIBRARIES"""
        skill_name_lower = skill_name.lower()

        skills_file = SKILLS_PATH / "Master" / "all_skills.json"

        if skills_file.exists():
            try:
                data = load_json(skills_file)
                for skill in data:
                    if skill.get('skill_name', '').lower() == skill_name_lower:
                        return True
            except:
                pass

        return False

    def generate_recommendations(self, analysis_results: Dict) -> List[str]:
        """Generate recommendations based on analysis"""
        recommendations = []

        summary = analysis_results.get('summary', {})
        total_new = summary.get('total_new', 0)

        # Recommendation: Entity integration
        if total_new > 0:
            recommendations.append(
                f"Integration recommended: {total_new} new entities identified. "
                f"Run video_json_updater.py to integrate into LIBRARIES."
            )

        # Recommendation: Cross-reference updates
        by_type = summary.get('by_type', {})
        if by_type.get('workflows', {}).get('new', 0) > 0:
            recommendations.append(
                "After integration: Update workflow cross-references to link tools, "
                "actions, and skills."
            )

        # Recommendation: Documentation
        if total_new >= 10:
            recommendations.append(
                "High entity count detected. Consider updating master documentation "
                "and taxonomy index files."
            )

        # Recommendation: Quality check
        if by_type.get('professions', {}).get('new', 0) > 0:
            recommendations.append(
                "New professions identified. Manually review and add detailed "
                "responsibilities, skills, and workflows."
            )

        return recommendations

    def save_report(self, output_path: Path, format: str = "markdown"):
        """
        Save integration report to file

        Args:
            output_path: Path to output file
            format: Output format ('markdown' or 'json')
        """
        if format == "json":
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(self.report_data, f, indent=2, ensure_ascii=False)

            logger.info(f"Saved JSON report: {output_path}")

        elif format == "markdown":
            lines = self.generate_markdown_report()

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))

            logger.info(f"Saved markdown report: {output_path}")

    def generate_markdown_report(self) -> List[str]:
        """Generate markdown formatted report"""
        lines = []

        # Header
        lines.append(f"# Video Integration Report: {self.video_id}")
        lines.append("")
        lines.append(f"**Report Date:** {self.report_data['report_date']}")
        lines.append("")

        # Executive Summary
        stats = self.report_data['statistics']
        lines.append("## Executive Summary")
        lines.append("")
        lines.append(f"- **Total Entities Identified:** {stats['total_entities']}")
        lines.append(f"- **New Entities:** {stats['total_new']}")
        lines.append(f"- **Existing Entities:** {stats['total_existing']}")
        lines.append(f"- **Updates Required:** {stats['total_updates']}")
        lines.append(f"- **Integration Rate:** {stats['integration_rate']:.1f}%")
        lines.append("")

        # Statistics by Type
        lines.append("## Entity Statistics by Type")
        lines.append("")

        headers = ["Entity Type", "Total", "New", "Existing", "Updates"]
        rows = []

        for entity_type, counts in stats['by_type'].items():
            rows.append([
                entity_type.title(),
                str(counts.get('total', 0)),
                str(counts.get('new', 0)),
                str(counts.get('exists', 0)),
                str(counts.get('update', 0))
            ])

        lines.append(create_markdown_table(headers, rows))
        lines.append("")

        # Entity Summaries
        lines.append("## Detailed Entity Summaries")
        lines.append("")

        entity_summaries = self.report_data['entity_summaries']

        for entity_type, summary in entity_summaries.items():
            if summary['new'] or summary['update']:
                lines.append(f"### {entity_type.title()}")
                lines.append("")

                # New entities
                if summary['new']:
                    lines.append("**NEW:**")
                    for entity in summary['new']:
                        name = entity['name']
                        next_id = entity.get('next_id', 'TBD')
                        category = entity.get('category', 'N/A')
                        lines.append(f"- {name} (ID: {next_id}, Category: {category})")
                    lines.append("")

                # Updates
                if summary['update']:
                    lines.append("**UPDATE:**")
                    for entity in summary['update']:
                        name = entity['name']
                        ent_id = entity.get('id', 'N/A')
                        reason = entity.get('reason', 'Review needed')
                        lines.append(f"- {name} ({ent_id}) - {reason}")
                    lines.append("")

        # Next Available IDs
        lines.append("## Next Available IDs")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(self.report_data['next_ids'], indent=2))
        lines.append("```")
        lines.append("")

        # Cross-Reference Validation
        if self.report_data.get('cross_references'):
            cross_refs = self.report_data['cross_references']
            lines.append("## Cross-Reference Validation")
            lines.append("")
            lines.append(f"**Total Issues Found:** {cross_refs.get('total_issues', 0)}")
            lines.append("")

            if cross_refs.get('issues_found'):
                lines.append("**Issues:**")
                for issue in cross_refs['issues_found']:
                    issue_type = issue['type']
                    severity = issue['severity']
                    lines.append(f"- [{severity.upper()}] {issue_type}: {issue}")
                lines.append("")

        # Recommendations
        recommendations = self.report_data['recommendations']
        if recommendations:
            lines.append("## Recommendations")
            lines.append("")
            for i, rec in enumerate(recommendations, 1):
                lines.append(f"{i}. {rec}")
            lines.append("")

        # Footer
        lines.append("---")
        lines.append("")
        lines.append(f"*Report generated by video_integration_reporter.py on {self.report_data['report_date']}*")

        return lines


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(
        description="Generate comprehensive integration report for video transcription"
    )
    parser.add_argument(
        'video_id',
        type=str,
        help='Video ID (e.g., Video_023)'
    )
    parser.add_argument(
        '--format',
        choices=['json', 'markdown'],
        default='markdown',
        help='Output format (default: markdown)'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='Output file path (optional)'
    )
    parser.add_argument(
        '--include-cross-refs',
        action='store_true',
        help='Include cross-reference validation in report'
    )

    args = parser.parse_args()

    # Initialize reporter
    reporter = VideoIntegrationReporter(args.video_id)

    # Generate report
    report_data = reporter.generate_report(include_cross_refs=args.include_cross_refs)

    if not report_data:
        logger.error("Report generation failed")
        return

    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"integration_report_{args.video_id}_{timestamp}.{args.format}"
        output_path = REPORTS_PATH / filename

    # Save report
    reporter.save_report(output_path, format=args.format)

    # Print summary to console
    print("\n" + "="*60)
    print("INTEGRATION REPORT SUMMARY")
    print("="*60)
    print(f"Video: {args.video_id}")
    print(f"Total Entities: {report_data['statistics']['total_entities']}")
    print(f"New Entities: {report_data['statistics']['total_new']}")
    print(f"Existing Entities: {report_data['statistics']['total_existing']}")
    print(f"Integration Rate: {report_data['statistics']['integration_rate']:.1f}%")
    print(f"\nReport saved to: {output_path}")
    print("="*60)


if __name__ == "__main__":
    main()
