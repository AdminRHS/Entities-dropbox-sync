"""
Video Gap Analyzer - Script 2
Compare transcription entities against existing LIBRARIES
Identify NEW, EXISTING, and UPDATE entities

Purpose: Analyze what's in transcription vs what's already in LIBRARIES
Time Saved: 30-45 minutes per video

Usage:
    python video_gap_analyzer.py Video_023
    python video_gap_analyzer.py Video_023 --output json
    python video_gap_analyzer.py Video_023 --detailed
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List, Set, Tuple
from datetime import datetime

from config import *
from utils import logger, log_summary, load_json
from markdown_parser import MarkdownTranscriptionParser
from video_id_scanner import VideoIDScanner


class VideoGapAnalyzer:
    """Analyzes gaps between transcription and existing LIBRARIES"""

    def __init__(self, video_id: str):
        self.video_id = video_id
        self.transcription_path = TRANSCRIPTIONS_PATH / f"{video_id}.md"
        self.parser = None
        self.scanner = VideoIDScanner()

        # Analysis results
        self.gaps = {
            "workflows": {"new": [], "exists": [], "update": []},
            "actions": {"new": [], "exists": [], "update": []},
            "objects": {"new": [], "exists": [], "update": []},
            "skills": {"new": [], "exists": [], "update": []},
            "tools": {"new": [], "exists": [], "update": []},
            "professions": {"new": [], "exists": [], "update": []}
        }

        # Next available IDs
        self.next_ids = {}

        # Existing entity lookups
        self.existing_workflows = {}
        self.existing_actions = set()
        self.existing_objects = {}
        self.existing_skills = {}
        self.existing_tools = {}
        self.existing_professions = set()

    def analyze(self) -> Dict[str, any]:
        """
        Run complete gap analysis

        Returns:
            Dictionary with gap analysis results
        """
        logger.info(f"Starting gap analysis for {self.video_id}...")

        # Step 1: Load and parse transcription
        if not self.load_transcription():
            return {}

        # Step 2: Load existing LIBRARIES data
        self.load_existing_entities()

        # Step 3: Get next available IDs
        self.next_ids = self.scanner.scan_all()

        # Step 4: Analyze each entity type
        self.analyze_workflows()
        self.analyze_actions()
        self.analyze_objects()
        self.analyze_skills()
        self.analyze_tools()
        self.analyze_professions()

        # Step 5: Generate summary
        summary = self.generate_summary()

        log_summary("Gap Analysis Complete", summary)
        return {
            "video_id": self.video_id,
            "gaps": self.gaps,
            "next_ids": self.next_ids,
            "summary": summary
        }

    def load_transcription(self) -> bool:
        """Load and parse markdown transcription file"""
        try:
            if not self.transcription_path.exists():
                logger.error(f"Transcription not found: {self.transcription_path}")
                return False

            logger.info(f"Loading transcription: {self.transcription_path}")
            self.parser = MarkdownTranscriptionParser(self.transcription_path)
            self.parser.parse_all_sections()

            logger.info(f"Parsed {len(self.parser.sections)} sections from transcription")
            return True

        except Exception as e:
            logger.error(f"Error loading transcription: {e}")
            return False

    def load_existing_entities(self):
        """Load all existing entities from LIBRARIES"""
        logger.info("Loading existing entities from LIBRARIES...")

        # Load workflows
        self.load_existing_workflows()

        # Load actions
        self.load_existing_actions()

        # Load objects
        self.load_existing_objects()

        # Load skills
        self.load_existing_skills()

        # Load tools
        self.load_existing_tools()

        # Load professions
        self.load_existing_professions()

    def load_existing_workflows(self):
        """Load existing workflows from TSM-006_Workflows"""
        try:
            workflow_files = list(WORKFLOWS_PATH.glob("WRF-*.json"))

            for file in workflow_files:
                data = load_json(file)
                workflow_id = data.get('workflow_id')
                workflow_name = data.get('workflow_name', '').lower()

                if workflow_id:
                    self.existing_workflows[workflow_id] = {
                        'name': workflow_name,
                        'file': file,
                        'data': data
                    }

            logger.info(f"Loaded {len(self.existing_workflows)} existing workflows")

        except Exception as e:
            logger.error(f"Error loading workflows: {e}")

    def load_existing_actions(self):
        """Load existing actions from actions_master.json"""
        try:
            master_file = ACTIONS_PATH / "Master" / "actions_master.json"

            if master_file.exists():
                data = load_json(master_file)

                for action in data.get('actions', []):
                    action_name = action.get('action_name', '').lower()
                    self.existing_actions.add(action_name)

            logger.info(f"Loaded {len(self.existing_actions)} existing actions")

        except Exception as e:
            logger.error(f"Error loading actions: {e}")

    def load_existing_objects(self):
        """Load existing objects from Objects directory"""
        try:
            object_files = {
                "SMM": OBJECTS_PATH / "Social_Media_Deliverables.json",
                "VID": OBJECTS_PATH / "Video_Deliverables.json",
                "DEV": OBJECTS_PATH / "Development_Objects.json",
                "DES": OBJECTS_PATH / "Design_Deliverables.json",
                "AI": OBJECTS_PATH / "AI_Automation_Objects.json"
            }

            for category, file_path in object_files.items():
                if file_path.exists():
                    data = load_json(file_path)

                    for obj in data.get('objects', []):
                        obj_name = obj.get('object_name', '').lower()
                        obj_id = obj.get('object_id')

                        if obj_id:
                            self.existing_objects[obj_id] = {
                                'name': obj_name,
                                'category': category,
                                'file': file_path
                            }

            logger.info(f"Loaded {len(self.existing_objects)} existing objects")

        except Exception as e:
            logger.error(f"Error loading objects: {e}")

    def load_existing_skills(self):
        """Load existing skills from all_skills.json"""
        try:
            skills_file = SKILLS_PATH / "Master" / "all_skills.json"

            if skills_file.exists():
                data = load_json(skills_file)

                for skill in data:
                    skill_id = skill.get('skill_id')
                    skill_name = skill.get('skill_name', '').lower()

                    if skill_id:
                        self.existing_skills[skill_id] = {
                            'name': skill_name,
                            'file': skills_file
                        }

            logger.info(f"Loaded {len(self.existing_skills)} existing skills")

        except Exception as e:
            logger.error(f"Error loading skills: {e}")

    def load_existing_tools(self):
        """Load existing tools from Tools directory"""
        try:
            tool_categories = {
                "AI": TOOLS_PATH / "AI_Tools",
                "CLOUD": TOOLS_PATH / "Cloud_Platforms",
                "SMM": TOOLS_PATH / "Social_Media_Platforms",
                "VID": TOOLS_PATH / "Video_Editing_Tools",
                "DEV": TOOLS_PATH / "Development_Tools"
            }

            for category, dir_path in tool_categories.items():
                if dir_path.exists():
                    tool_files = list(dir_path.glob("*.json"))

                    for file in tool_files:
                        data = load_json(file)
                        tool_id = data.get('tool_id')
                        tool_name = data.get('tool_name', '').lower()

                        if tool_id:
                            self.existing_tools[tool_id] = {
                                'name': tool_name,
                                'category': category,
                                'file': file
                            }

            logger.info(f"Loaded {len(self.existing_tools)} existing tools")

        except Exception as e:
            logger.error(f"Error loading tools: {e}")

    def load_existing_professions(self):
        """Load existing professions (name-based)"""
        try:
            if PROFESSIONS_PATH.exists():
                profession_files = list(PROFESSIONS_PATH.glob("*.json"))

                for file in profession_files:
                    # Profession files are named by profession name
                    prof_name = file.stem.lower()
                    self.existing_professions.add(prof_name)

            logger.info(f"Loaded {len(self.existing_professions)} existing professions")

        except Exception as e:
            logger.error(f"Error loading professions: {e}")

    def analyze_workflows(self):
        """Analyze workflows from transcription"""
        try:
            workflows = self.parser.sections.get('workflows', [])
            logger.info(f"Analyzing {len(workflows)} workflows from transcription...")

            for workflow in workflows:
                workflow_name = workflow.get('name', '').lower()
                workflow_id = workflow.get('workflow_id')

                # Check if exists
                if workflow_id and workflow_id in self.existing_workflows:
                    self.gaps['workflows']['exists'].append({
                        'id': workflow_id,
                        'name': workflow_name,
                        'status': 'EXISTS',
                        'file': str(self.existing_workflows[workflow_id]['file'])
                    })
                else:
                    # Check for name match (potential duplicate)
                    name_match = False
                    for existing_id, existing_data in self.existing_workflows.items():
                        if existing_data['name'] == workflow_name:
                            name_match = True
                            self.gaps['workflows']['update'].append({
                                'id': existing_id,
                                'name': workflow_name,
                                'status': 'UPDATE',
                                'reason': 'Name match, review for updates',
                                'transcription_data': workflow
                            })
                            break

                    if not name_match:
                        self.gaps['workflows']['new'].append({
                            'name': workflow_name,
                            'status': 'NEW',
                            'next_id': self.next_ids.get('workflows'),
                            'transcription_data': workflow
                        })

            logger.info(f"Workflows: {len(self.gaps['workflows']['new'])} NEW, "
                       f"{len(self.gaps['workflows']['exists'])} EXISTS, "
                       f"{len(self.gaps['workflows']['update'])} UPDATE")

        except Exception as e:
            logger.error(f"Error analyzing workflows: {e}")

    def analyze_actions(self):
        """Analyze actions from transcription"""
        try:
            actions_dict = self.parser.sections.get('actions', {})
            all_actions = []

            # Flatten all action categories
            for category, actions in actions_dict.items():
                for action in actions:
                    all_actions.append({
                        'name': action,
                        'category': category
                    })

            logger.info(f"Analyzing {len(all_actions)} actions from transcription...")

            for action in all_actions:
                action_name = action['name'].lower()

                if action_name in self.existing_actions:
                    self.gaps['actions']['exists'].append({
                        'name': action_name,
                        'category': action['category'],
                        'status': 'EXISTS'
                    })
                else:
                    self.gaps['actions']['new'].append({
                        'name': action_name,
                        'category': action['category'],
                        'status': 'NEW',
                        'next_id': self.next_ids.get('actions', {}).get('master')
                    })

            logger.info(f"Actions: {len(self.gaps['actions']['new'])} NEW, "
                       f"{len(self.gaps['actions']['exists'])} EXISTS")

        except Exception as e:
            logger.error(f"Error analyzing actions: {e}")

    def analyze_objects(self):
        """Analyze objects from transcription"""
        try:
            objects = self.parser.sections.get('objects', [])
            logger.info(f"Analyzing {len(objects)} objects from transcription...")

            for obj in objects:
                obj_name = obj.get('name', '').lower()
                obj_category = obj.get('category', 'UNKNOWN')

                # Check for name match in existing objects
                name_match = False
                for existing_id, existing_data in self.existing_objects.items():
                    if existing_data['name'] == obj_name:
                        name_match = True
                        self.gaps['objects']['exists'].append({
                            'id': existing_id,
                            'name': obj_name,
                            'category': obj_category,
                            'status': 'EXISTS'
                        })
                        break

                if not name_match:
                    next_id = self.next_ids.get('objects', {}).get(obj_category)
                    self.gaps['objects']['new'].append({
                        'name': obj_name,
                        'category': obj_category,
                        'status': 'NEW',
                        'next_id': next_id,
                        'transcription_data': obj
                    })

            logger.info(f"Objects: {len(self.gaps['objects']['new'])} NEW, "
                       f"{len(self.gaps['objects']['exists'])} EXISTS")

        except Exception as e:
            logger.error(f"Error analyzing objects: {e}")

    def analyze_skills(self):
        """Analyze skills from transcription"""
        try:
            # Skills might be in workflows or separate section
            workflows = self.parser.sections.get('workflows', [])
            all_skills = set()

            for workflow in workflows:
                skills = workflow.get('skills_required', [])
                for skill in skills:
                    all_skills.add(skill.lower())

            logger.info(f"Analyzing {len(all_skills)} skills from transcription...")

            for skill_name in all_skills:
                # Check for name match
                name_match = False
                for existing_id, existing_data in self.existing_skills.items():
                    if existing_data['name'] == skill_name:
                        name_match = True
                        self.gaps['skills']['exists'].append({
                            'id': existing_id,
                            'name': skill_name,
                            'status': 'EXISTS'
                        })
                        break

                if not name_match:
                    self.gaps['skills']['new'].append({
                        'name': skill_name,
                        'status': 'NEW',
                        'next_id': self.next_ids.get('skills')
                    })

            logger.info(f"Skills: {len(self.gaps['skills']['new'])} NEW, "
                       f"{len(self.gaps['skills']['exists'])} EXISTS")

        except Exception as e:
            logger.error(f"Error analyzing skills: {e}")

    def analyze_tools(self):
        """Analyze tools from transcription"""
        try:
            tools = self.parser.sections.get('tools', [])
            logger.info(f"Analyzing {len(tools)} tools from transcription...")

            for tool in tools:
                tool_name = tool.get('name', '').lower()
                tool_category = tool.get('category', 'UNKNOWN')

                # Check for name match
                name_match = False
                for existing_id, existing_data in self.existing_tools.items():
                    if existing_data['name'] == tool_name:
                        name_match = True
                        self.gaps['tools']['exists'].append({
                            'id': existing_id,
                            'name': tool_name,
                            'category': tool_category,
                            'status': 'EXISTS'
                        })
                        break

                if not name_match:
                    next_id = self.next_ids.get('tools', {}).get(tool_category)
                    self.gaps['tools']['new'].append({
                        'name': tool_name,
                        'category': tool_category,
                        'status': 'NEW',
                        'next_id': next_id,
                        'transcription_data': tool
                    })

            logger.info(f"Tools: {len(self.gaps['tools']['new'])} NEW, "
                       f"{len(self.gaps['tools']['exists'])} EXISTS")

        except Exception as e:
            logger.error(f"Error analyzing tools: {e}")

    def analyze_professions(self):
        """Analyze professions from transcription"""
        try:
            # Extract professions from department distribution or workflows
            workflows = self.parser.sections.get('workflows', [])
            all_professions = set()

            # Look for profession mentions in workflow context
            # This is a simplified approach - may need refinement
            for workflow in workflows:
                departments = workflow.get('departments', [])
                for dept in departments:
                    # Map departments to potential professions
                    if dept == 'AID':
                        all_professions.add('ai automation specialist')
                    elif dept == 'SMM':
                        all_professions.add('social media manager')
                    elif dept == 'VID':
                        all_professions.add('video editor')

            logger.info(f"Analyzing {len(all_professions)} professions from transcription...")

            for prof_name in all_professions:
                if prof_name in self.existing_professions:
                    self.gaps['professions']['exists'].append({
                        'name': prof_name,
                        'status': 'EXISTS'
                    })
                else:
                    self.gaps['professions']['new'].append({
                        'name': prof_name,
                        'status': 'NEW'
                    })

            logger.info(f"Professions: {len(self.gaps['professions']['new'])} NEW, "
                       f"{len(self.gaps['professions']['exists'])} EXISTS")

        except Exception as e:
            logger.error(f"Error analyzing professions: {e}")

    def generate_summary(self) -> Dict[str, any]:
        """Generate summary statistics"""
        summary = {
            "total_new": 0,
            "total_exists": 0,
            "total_update": 0,
            "by_type": {}
        }

        for entity_type, gaps in self.gaps.items():
            new_count = len(gaps['new'])
            exists_count = len(gaps['exists'])
            update_count = len(gaps['update'])

            summary['total_new'] += new_count
            summary['total_exists'] += exists_count
            summary['total_update'] += update_count

            summary['by_type'][entity_type] = {
                'new': new_count,
                'exists': exists_count,
                'update': update_count,
                'total': new_count + exists_count + update_count
            }

        return summary

    def save_report(self, output_path: Path, format: str = "markdown"):
        """
        Save gap analysis report to file

        Args:
            output_path: Path to output file
            format: Output format ('markdown' or 'json')
        """
        if format == "json":
            report_data = {
                "video_id": self.video_id,
                "analysis_date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "gaps": self.gaps,
                "next_ids": self.next_ids,
                "summary": self.generate_summary()
            }

            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, indent=2, ensure_ascii=False)

            logger.info(f"Saved JSON report: {output_path}")

        elif format == "markdown":
            lines = [f"# Gap Analysis Report: {self.video_id}", ""]
            lines.append(f"**Analysis Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            lines.append("")

            # Summary section
            summary = self.generate_summary()
            lines.append("## Summary")
            lines.append("")
            lines.append(f"- **Total NEW entities:** {summary['total_new']}")
            lines.append(f"- **Total EXISTING entities:** {summary['total_exists']}")
            lines.append(f"- **Total UPDATE entities:** {summary['total_update']}")
            lines.append("")

            # By type breakdown
            lines.append("## Breakdown by Entity Type")
            lines.append("")
            for entity_type, counts in summary['by_type'].items():
                lines.append(f"### {entity_type.title()}")
                lines.append(f"- NEW: {counts['new']}")
                lines.append(f"- EXISTS: {counts['exists']}")
                lines.append(f"- UPDATE: {counts['update']}")
                lines.append("")

            # Next IDs
            lines.append("## Next Available IDs")
            lines.append("")
            lines.append("```json")
            lines.append(json.dumps(self.next_ids, indent=2))
            lines.append("```")
            lines.append("")

            # Detailed gaps
            lines.append("## Detailed Gap Analysis")
            lines.append("")

            for entity_type, gaps in self.gaps.items():
                if gaps['new'] or gaps['update']:
                    lines.append(f"### {entity_type.title()}")
                    lines.append("")

                    if gaps['new']:
                        lines.append("**NEW:**")
                        for item in gaps['new']:
                            lines.append(f"- {item.get('name')} (ID: {item.get('next_id', 'TBD')})")
                        lines.append("")

                    if gaps['update']:
                        lines.append("**UPDATE:**")
                        for item in gaps['update']:
                            lines.append(f"- {item.get('name')} ({item.get('id')}) - {item.get('reason', 'Review needed')}")
                        lines.append("")

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))

            logger.info(f"Saved markdown report: {output_path}")


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(
        description="Analyze gaps between transcription and existing LIBRARIES"
    )
    parser.add_argument(
        'video_id',
        type=str,
        help='Video ID (e.g., Video_023)'
    )
    parser.add_argument(
        '--output',
        choices=['json', 'markdown', 'console'],
        default='console',
        help='Output format (default: console)'
    )
    parser.add_argument(
        '--file',
        type=str,
        help='Output file path (optional)'
    )
    parser.add_argument(
        '--detailed',
        action='store_true',
        help='Include detailed transcription data in output'
    )

    args = parser.parse_args()

    # Initialize analyzer
    analyzer = VideoGapAnalyzer(args.video_id)

    # Run analysis
    results = analyzer.analyze()

    if not results:
        logger.error("Analysis failed - see errors above")
        return

    # Output results
    if args.output == 'console':
        print(json.dumps(results['summary'], indent=2))

    elif args.file:
        output_path = Path(args.file)
        analyzer.save_report(output_path, args.output)

    else:
        # Default file output
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_path = ANALYSIS_PATH / f"gap_analysis_{args.video_id}_{timestamp}.{args.output}"
        analyzer.save_report(output_path, args.output)


if __name__ == "__main__":
    main()
