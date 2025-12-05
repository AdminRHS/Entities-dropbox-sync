"""
Video ID Scanner - Script 1
Automatically discover next available entity IDs across all LIBRARIES

Purpose: Scan all entity directories and return next sequential IDs
Time Saved: 15-30 minutes per video

Usage:
    python video_id_scanner.py
    python video_id_scanner.py --output json
    python video_id_scanner.py --entity-type workflows
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List
import re

from config import *
from utils import logger, log_summary

class VideoIDScanner:
    """Scans LIBRARIES and returns next available entity IDs"""

    def __init__(self):
        self.next_ids = {}

    def scan_all(self) -> Dict[str, any]:
        """
        Scan all entity types and return next available IDs

        Returns:
            Dictionary with next IDs for all entity types
        """
        logger.info("Starting comprehensive ID scan...")

        self.next_ids = {
            "workflows": self.scan_workflows(),
            "actions": self.scan_actions(),
            "objects": self.scan_objects(),
            "skills": self.scan_skills(),
            "tools": self.scan_tools(),
            "professions": self.scan_professions()
        }

        log_summary("Next Available IDs", self.next_ids)
        return self.next_ids

    def scan_workflows(self) -> str:
        """
        Scan TSM-006_Workflows directory for next workflow ID

        Returns:
            Next available workflow ID (e.g., 'WRF-025')
        """
        try:
            workflow_files = list(WORKFLOWS_PATH.glob("WRF-*.json"))

            if not workflow_files:
                return f"{WORKFLOW_PREFIX}-001"

            # Extract IDs
            ids = []
            for file in workflow_files:
                match = re.search(r'WRF-(\d{3})', file.name)
                if match:
                    ids.append(int(match.group(1)))

            next_num = max(ids) + 1 if ids else 1
            next_id = f"{WORKFLOW_PREFIX}-{next_num:03d}"

            logger.info(f"Workflows: {len(ids)} existing → Next: {next_id}")
            return next_id

        except Exception as e:
            logger.error(f"Error scanning workflows: {e}")
            return f"{WORKFLOW_PREFIX}-001"

    def scan_actions(self) -> Dict[str, str]:
        """
        Scan Actions directory for next action IDs

        Returns:
            Dictionary with next IDs for command and master actions
        """
        try:
            result = {}

            # Scan actions_command_verbs.json
            command_file = ACTIONS_PATH / "Master" / "actions_command_verbs.json"
            if command_file.exists():
                with open(command_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    total = data.get('total_actions', 0)
                    result['command'] = f"{ACTION_PREFIX}-{total + 1:03d}"
                    result['command_total'] = total
            else:
                result['command'] = f"{ACTION_PREFIX}-001"
                result['command_total'] = 0

            # Scan actions_master.json
            master_file = ACTIONS_PATH / "Master" / "actions_master.json"
            if master_file.exists():
                with open(master_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    total = data.get('total_actions', 0)
                    result['master'] = f"{ACTION_PREFIX}-{total + 1:03d}"
                    result['master_total'] = total
            else:
                result['master'] = f"{ACTION_PREFIX}-001"
                result['master_total'] = 0

            logger.info(f"Actions: Command({result['command_total']}) → {result['command']}, Master({result['master_total']}) → {result['master']}")
            return result

        except Exception as e:
            logger.error(f"Error scanning actions: {e}")
            return {
                'command': f"{ACTION_PREFIX}-001",
                'master': f"{ACTION_PREFIX}-001"
            }

    def scan_objects(self) -> Dict[str, str]:
        """
        Scan Objects directory for next object IDs by category

        Returns:
            Dictionary with next IDs for each object category
        """
        try:
            result = {}

            # Object files and their prefixes
            object_files = {
                "SMM": OBJECTS_PATH / "Social_Media_Deliverables.json",
                "VID": OBJECTS_PATH / "Video_Deliverables.json",
                "DEV": OBJECTS_PATH / "Development_Objects.json",
                "DES": OBJECTS_PATH / "Design_Deliverables.json",
                "AI": OBJECTS_PATH / "AI_Automation_Objects.json"
            }

            for category, file_path in object_files.items():
                if file_path.exists():
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                            total = data.get('total_objects', 0)

                            if total == 0:
                                # Count objects in array
                                total = len(data.get('objects', []))

                            next_num = total + 1
                            prefix = OBJECT_PREFIXES.get(category, f"OBJ-{category}")
                            next_id = f"{prefix}-{next_num:03d}"
                            result[category] = next_id

                            logger.info(f"Objects ({category}): {total} existing → {next_id}")

                    except Exception as e:
                        logger.warning(f"Error reading {file_path}: {e}")
                        result[category] = f"{OBJECT_PREFIXES.get(category, f'OBJ-{category}')}-001"
                else:
                    result[category] = f"{OBJECT_PREFIXES.get(category, f'OBJ-{category}')}-001"

            return result

        except Exception as e:
            logger.error(f"Error scanning objects: {e}")
            return {}

    def scan_skills(self) -> str:
        """
        Scan Skills directory for next skill ID

        Returns:
            Next available skill ID (e.g., 'SKL-065')
        """
        try:
            skills_file = SKILLS_PATH / "Master" / "all_skills.json"

            if not skills_file.exists():
                return f"{SKILL_PREFIX}-001"

            with open(skills_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

                # Find max skill ID
                max_num = 0
                for skill in data:
                    skill_id = skill.get('skill_id', '')
                    match = re.search(r'SKL-(\d{3})', skill_id)
                    if match:
                        max_num = max(max_num, int(match.group(1)))

                next_num = max_num + 1
                next_id = f"{SKILL_PREFIX}-{next_num:03d}"

                logger.info(f"Skills: {max_num} existing → {next_id}")
                return next_id

        except Exception as e:
            logger.error(f"Error scanning skills: {e}")
            return f"{SKILL_PREFIX}-001"

    def scan_tools(self) -> Dict[str, str]:
        """
        Scan Tools directory for next tool IDs by category

        Returns:
            Dictionary with next IDs for each tool category
        """
        try:
            result = {}

            # Tool categories and their directories
            tool_categories = {
                "AI": TOOLS_PATH / "AI_Tools",
                "CLOUD": TOOLS_PATH / "Cloud_Platforms",
                "SMM": TOOLS_PATH / "Social_Media_Platforms",
                "VID": TOOLS_PATH / "Video_Editing_Tools",
                "DEV": TOOLS_PATH / "Development_Tools"
            }

            for category, dir_path in tool_categories.items():
                if dir_path.exists():
                    # Find all JSON files in category
                    tool_files = list(dir_path.glob("*.json"))

                    # Extract tool IDs
                    max_num = 0
                    for file in tool_files:
                        with open(file, 'r', encoding='utf-8') as f:
                            try:
                                data = json.load(f)
                                tool_id = data.get('tool_id', '')

                                # Extract number from tool ID (e.g., TOOL-AI-222 → 222)
                                match = re.search(r'TOOL-[A-Z]+-(\d{3})', tool_id)
                                if match:
                                    max_num = max(max_num, int(match.group(1)))
                            except:
                                continue

                    next_num = max_num + 1
                    prefix = TOOL_CATEGORIES.get(category, f"TOOL-{category}")
                    next_id = f"{prefix}-{next_num:03d}"
                    result[category] = next_id

                    logger.info(f"Tools ({category}): {max_num} existing → {next_id}")
                else:
                    result[category] = f"{TOOL_CATEGORIES.get(category, f'TOOL-{category}')}-001"

            return result

        except Exception as e:
            logger.error(f"Error scanning tools: {e}")
            return {}

    def scan_professions(self) -> str:
        """
        Scan Professions directory for count (no numeric IDs)

        Returns:
            Count of existing professions
        """
        try:
            if not PROFESSIONS_PATH.exists():
                return "0 professions"

            profession_files = list(PROFESSIONS_PATH.glob("*.json"))
            count = len(profession_files)

            logger.info(f"Professions: {count} existing")
            return f"{count} professions (name-based, not numeric IDs)"

        except Exception as e:
            logger.error(f"Error scanning professions: {e}")
            return "0 professions"

    def validate_no_gaps(self) -> bool:
        """
        Validate that there are no gaps in entity ID sequences

        Returns:
            True if no gaps found, False otherwise
        """
        logger.info("Validating ID sequences for gaps...")

        gaps_found = False

        # Check workflows
        workflow_files = sorted(WORKFLOWS_PATH.glob("WRF-*.json"))
        workflow_nums = []
        for file in workflow_files:
            match = re.search(r'WRF-(\d{3})', file.name)
            if match:
                workflow_nums.append(int(match.group(1)))

        if workflow_nums:
            expected = list(range(1, max(workflow_nums) + 1))
            missing = set(expected) - set(workflow_nums)
            if missing:
                logger.warning(f"Workflow ID gaps found: {sorted(missing)}")
                gaps_found = True

        # Similar checks could be added for other entity types

        if not gaps_found:
            logger.info("✓ No ID gaps detected")

        return not gaps_found

    def save_to_file(self, output_path: Path, format: str = "json"):
        """
        Save scan results to file

        Args:
            output_path: Path to output file
            format: Output format ('json' or 'markdown')
        """
        if format == "json":
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(self.next_ids, f, indent=2)
            logger.info(f"Saved scan results to: {output_path}")

        elif format == "markdown":
            lines = ["# Next Available Entity IDs", ""]
            lines.append(f"**Scan Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            lines.append("")

            for entity_type, ids in self.next_ids.items():
                lines.append(f"## {entity_type.title()}")
                if isinstance(ids, dict):
                    for key, value in ids.items():
                        lines.append(f"- **{key}**: `{value}`")
                else:
                    lines.append(f"- `{ids}`")
                lines.append("")

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))

            logger.info(f"Saved scan results to: {output_path}")


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(
        description="Scan LIBRARIES directories and discover next available entity IDs"
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
        '--entity-type',
        choices=['workflows', 'actions', 'objects', 'skills', 'tools', 'professions', 'all'],
        default='all',
        help='Specific entity type to scan (default: all)'
    )
    parser.add_argument(
        '--validate',
        action='store_true',
        help='Validate ID sequences for gaps'
    )

    args = parser.parse_args()

    # Initialize scanner
    scanner = VideoIDScanner()

    # Scan based on entity type
    if args.entity_type == 'all':
        results = scanner.scan_all()
    else:
        # Scan specific entity type
        method = getattr(scanner, f"scan_{args.entity_type}")
        results = {args.entity_type: method()}

    # Validate if requested
    if args.validate:
        scanner.validate_no_gaps()

    # Output results
    if args.output == 'console':
        print(json.dumps(results, indent=2))

    elif args.file:
        output_path = Path(args.file)
        scanner.next_ids = results
        scanner.save_to_file(output_path, args.output)

    else:
        # Default file output
        output_path = SCRIPTS_PATH / f"next_ids_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{args.output}"
        scanner.next_ids = results
        scanner.save_to_file(output_path, args.output)


if __name__ == "__main__":
    main()
