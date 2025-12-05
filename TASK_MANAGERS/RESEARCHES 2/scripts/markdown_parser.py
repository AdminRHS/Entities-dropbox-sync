"""
Markdown Parser for Video Transcription Files
Handles parsing of Video_XXX.md files with structured taxonomy sections

Purpose: Extract workflows, actions, tools, objects, and other entities from markdown transcriptions
"""

import re
from typing import Dict, List, Optional, Tuple
from pathlib import Path

from utils import logger


class MarkdownTranscriptionParser:
    """Parse structured markdown transcription files"""

    def __init__(self, file_path: Path):
        """
        Initialize parser with transcription file

        Args:
            file_path: Path to Video_XXX.md transcription file
        """
        self.file_path = file_path
        self.content = ""
        self.sections = {}
        self.load_file()

    def load_file(self):
        """Load markdown file content"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
            logger.info(f"Loaded transcription: {self.file_path.name} ({len(self.content)} chars)")
        except Exception as e:
            logger.error(f"Error loading {self.file_path}: {e}")
            raise

    def parse_all_sections(self) -> Dict[str, any]:
        """
        Parse all major sections from transcription

        Returns:
            Dictionary with all parsed sections
        """
        self.sections = {
            "metadata": self.parse_metadata(),
            "workflows": self.parse_workflows(),
            "actions": self.parse_actions(),
            "tools": self.parse_tools(),
            "objects": self.parse_objects(),
            "integrations": self.parse_integrations(),
            "entities_csv": self.parse_entity_csv(),
            "department_distribution": self.parse_department_distribution()
        }

        logger.info(f"Parsed {len(self.sections)} sections")
        return self.sections

    def parse_metadata(self) -> Dict[str, str]:
        """
        Parse metadata section from transcription

        Returns:
            Dictionary with video metadata
        """
        metadata = {
            "video_id": "",
            "title": "",
            "channel": "",
            "creator": "",
            "url": "",
            "duration": "",
            "publication_date": "",
            "extraction_date": ""
        }

        try:
            # Extract title from first # heading
            title_match = re.search(r'^# (.+)', self.content, re.MULTILINE)
            if title_match:
                metadata["title"] = title_match.group(1).strip()

            # Extract video ID from title
            video_id_match = re.search(r'Video_(\d{3})', metadata["title"])
            if video_id_match:
                metadata["video_id"] = f"Video_{video_id_match.group(1)}"

            # Find metadata section
            meta_section = re.search(r'## Metadata\s*\n(.*?)(?=\n##|\Z)', self.content, re.DOTALL)
            if meta_section:
                meta_text = meta_section.group(1)

                # Parse metadata fields
                patterns = {
                    "channel": r'[\*\-]\s*(?:Channel|Creator):\s*(.+)',
                    "creator": r'[\*\-]\s*(?:Creator|Channel):\s*(.+)',
                    "url": r'[\*\-]\s*(?:Video\s+)?URL:\s*(.+)',
                    "duration": r'[\*\-]\s*Duration:\s*(.+)',
                    "publication_date": r'[\*\-]\s*Publication\s+Date:\s*(.+)',
                    "extraction_date": r'[\*\-]\s*Extraction\s+Date:\s*(.+)'
                }

                for key, pattern in patterns.items():
                    match = re.search(pattern, meta_text, re.IGNORECASE)
                    if match:
                        metadata[key] = match.group(1).strip()

        except Exception as e:
            logger.warning(f"Error parsing metadata: {e}")

        return metadata

    def parse_workflows(self) -> List[Dict]:
        """
        Parse workflows from "Workflows Identified" section

        Returns:
            List of workflow dictionaries
        """
        workflows = []

        try:
            # Find workflows section
            section = re.search(
                r'## Workflows?\s+Identified\s*\n(.*?)(?=\n##|\Z)',
                self.content,
                re.DOTALL | re.IGNORECASE
            )

            if not section:
                logger.warning("Workflows section not found")
                return workflows

            section_text = section.group(1)

            # Parse each workflow (format: WRF-XXX: Name)
            workflow_blocks = re.finditer(
                r'(WRF-\d{3}):\s*(.+?)\n(.*?)(?=WRF-\d{3}:|\Z)',
                section_text,
                re.DOTALL
            )

            for match in workflow_blocks:
                workflow_id = match.group(1)
                workflow_name = match.group(2).strip()
                workflow_details = match.group(3).strip()

                # Extract workflow components
                workflow = {
                    "workflow_id": workflow_id,
                    "name": workflow_name,
                    "objective": "",
                    "tasks": [],
                    "duration": "",
                    "complexity": "",
                    "department": []
                }

                # Parse OBJECTIVE
                obj_match = re.search(r'[\*\-]\s*OBJECTIVE:\s*(.+)', workflow_details, re.IGNORECASE)
                if obj_match:
                    workflow["objective"] = obj_match.group(1).strip()

                # Parse TASKS
                tasks_section = re.search(r'[\*\-]\s*TASKS?:\s*\n(.*?)(?=[\*\-]\s*[A-Z]+:|\Z)', workflow_details, re.DOTALL | re.IGNORECASE)
                if tasks_section:
                    task_lines = tasks_section.group(1).strip().split('\n')
                    for line in task_lines:
                        task_match = re.search(r'(TSK-\d{3}):\s*(.+)', line)
                        if task_match:
                            workflow["tasks"].append({
                                "task_id": task_match.group(1),
                                "description": task_match.group(2).strip()
                            })

                # Parse DURATION
                dur_match = re.search(r'[\*\-]\s*DURATION:\s*(.+)', workflow_details, re.IGNORECASE)
                if dur_match:
                    workflow["duration"] = dur_match.group(1).strip()

                # Parse COMPLEXITY
                comp_match = re.search(r'[\*\-]\s*COMPLEXITY:\s*(.+)', workflow_details, re.IGNORECASE)
                if comp_match:
                    workflow["complexity"] = comp_match.group(1).strip()

                # Parse DEPARTMENT
                dept_match = re.search(r'[\*\-]\s*DEPARTMENT:\s*(.+)', workflow_details, re.IGNORECASE)
                if dept_match:
                    dept_str = dept_match.group(1).strip()
                    workflow["department"] = [d.strip() for d in dept_str.split(',')]

                workflows.append(workflow)

            logger.info(f"Parsed {len(workflows)} workflows")

        except Exception as e:
            logger.error(f"Error parsing workflows: {e}")

        return workflows

    def parse_actions(self) -> Dict[str, List[str]]:
        """
        Parse action verbs from "Action Verbs & Operations" section

        Returns:
            Dictionary with actions grouped by category
        """
        actions = {
            "creation": [],
            "modification": [],
            "analysis": [],
            "organization": [],
            "communication": [],
            "browser_agentic": [],
            "data_operations": []
        }

        try:
            # Find action verbs section
            section = re.search(
                r'## Action Verbs?\s+(&|and)\s+Operations.*?\n(.*?)(?=\n##|\Z)',
                self.content,
                re.DOTALL | re.IGNORECASE
            )

            if not section:
                logger.warning("Action Verbs section not found")
                return actions

            section_text = section.group(2)

            # Parse each category
            category_patterns = {
                "creation": r'A\.\s*CREATION\s+VERBS?\s*\n(.*?)(?=[B-G]\.|$)',
                "modification": r'B\.\s*MODIFICATION\s+VERBS?\s*\n(.*?)(?=[C-G]\.|$)',
                "analysis": r'C\.\s*ANALYSIS\s+VERBS?\s*\n(.*?)(?=[D-G]\.|$)',
                "organization": r'D\.\s*ORGANIZATION\s+VERBS?\s*\n(.*?)(?=[E-G]\.|$)',
                "communication": r'E\.\s*COMMUNICATION\s+VERBS?\s*\n(.*?)(?=[F-G]\.|$)',
                "browser_agentic": r'F\.\s*BROWSER/?AGENTIC\s+(?:VERBS?|OPERATIONS)\s*\n(.*?)(?=G\.|$)',
                "data_operations": r'G\.\s*DATA\s+OPERATIONS\s*\n(.*?)$'
            }

            for category, pattern in category_patterns.items():
                match = re.search(pattern, section_text, re.DOTALL | re.IGNORECASE)
                if match:
                    verbs_text = match.group(1)
                    # Extract verbs (typically listed with - or *)
                    verbs = re.findall(r'[\*\-]\s*(\w+(?:\s+\w+)?)', verbs_text)
                    actions[category] = [v.strip().lower() for v in verbs if v.strip()]

            total_actions = sum(len(v) for v in actions.values())
            logger.info(f"Parsed {total_actions} action verbs across {len(actions)} categories")

        except Exception as e:
            logger.error(f"Error parsing actions: {e}")

        return actions

    def parse_tools(self) -> List[Dict]:
        """
        Parse tools from "Tools & Technologies Matrix" section

        Returns:
            List of tool dictionaries
        """
        tools = []

        try:
            # Find tools matrix section
            section = re.search(
                r'## Tools?\s+(&|and)\s+Technologies?\s+Matrix.*?\n(.*?)(?=\n##|\Z)',
                self.content,
                re.DOTALL | re.IGNORECASE
            )

            if not section:
                logger.warning("Tools & Technologies Matrix section not found")
                return tools

            section_text = section.group(2)

            # Find markdown table
            table_match = re.search(r'\|.*Tool.*\|.*\n\|[-\s|]+\n(.*?)(?=\n\n|$)', section_text, re.DOTALL)
            if table_match:
                table_rows = table_match.group(1).strip().split('\n')

                for row in table_rows:
                    # Parse table cells
                    cells = [cell.strip() for cell in row.split('|') if cell.strip()]

                    if len(cells) >= 4:
                        tool = {
                            "tool_id": cells[0] if len(cells) > 0 else "",
                            "name": cells[1] if len(cells) > 1 else "",
                            "category": cells[2] if len(cells) > 2 else "",
                            "purpose": cells[3] if len(cells) > 3 else "",
                            "department": cells[4].split(',') if len(cells) > 4 else []
                        }
                        tools.append(tool)

            logger.info(f"Parsed {len(tools)} tools")

        except Exception as e:
            logger.error(f"Error parsing tools: {e}")

        return tools

    def parse_objects(self) -> List[str]:
        """
        Parse objects from "Objects & Deliverables" section

        Returns:
            List of object names
        """
        objects = []

        try:
            # Find objects section
            section = re.search(
                r'## Objects?\s+(&|and)\s+Deliverables?\s*\n(.*?)(?=\n##|\Z)',
                self.content,
                re.DOTALL | re.IGNORECASE
            )

            if not section:
                logger.warning("Objects & Deliverables section not found")
                return objects

            section_text = section.group(2)

            # Extract bulleted items
            object_items = re.findall(r'[\*\-]\s*(.+)', section_text)
            objects = [obj.strip() for obj in object_items if obj.strip()]

            logger.info(f"Parsed {len(objects)} objects")

        except Exception as e:
            logger.error(f"Error parsing objects: {e}")

        return objects

    def parse_integrations(self) -> List[Dict]:
        """
        Parse integration patterns from "Integration Patterns" section

        Returns:
            List of integration dictionaries
        """
        integrations = []

        try:
            # Find integrations section
            section = re.search(
                r'## Integration\s+Patterns?\s*\n(.*?)(?=\n##|\Z)',
                self.content,
                re.DOTALL | re.IGNORECASE
            )

            if not section:
                logger.warning("Integration Patterns section not found")
                return integrations

            section_text = section.group(2)

            # Parse each integration (format: INT-XXX: Name)
            int_blocks = re.finditer(
                r'(INT-\d{3}):\s*(.+?)\n(.*?)(?=INT-\d{3}:|\Z)',
                section_text,
                re.DOTALL
            )

            for match in int_blocks:
                integration = {
                    "integration_id": match.group(1),
                    "name": match.group(2).strip(),
                    "entity_chain": "",
                    "flow": []
                }

                details = match.group(3).strip()

                # Parse ENTITY_CHAIN
                chain_match = re.search(r'[\*\-]\s*ENTITY_CHAIN:\s*(.+)', details, re.IGNORECASE)
                if chain_match:
                    integration["entity_chain"] = chain_match.group(1).strip()

                # Parse FLOW
                flow_match = re.search(r'[\*\-]\s*FLOW:\s*(.+)', details, re.IGNORECASE)
                if flow_match:
                    flow_text = flow_match.group(1).strip()
                    integration["flow"] = [step.strip() for step in flow_text.split('→') if step.strip()]

                integrations.append(integration)

            logger.info(f"Parsed {len(integrations)} integration patterns")

        except Exception as e:
            logger.error(f"Error parsing integrations: {e}")

        return integrations

    def parse_entity_csv(self) -> List[Dict]:
        """
        Parse entity CSV section (Entity ID Assignment & Master List)

        Returns:
            List of entity dictionaries from CSV
        """
        entities = []

        try:
            # Find CSV section
            section = re.search(
                r'## Entity ID Assignment\s+(&|and)\s+Master List\s*\n(.*?)(?=\n##|\Z)',
                self.content,
                re.DOTALL | re.IGNORECASE
            )

            if not section:
                logger.warning("Entity ID Assignment & Master List section not found")
                return entities

            section_text = section.group(2)

            # Find CSV table
            table_match = re.search(r'\|.*New_ID.*\|.*\n\|[-\s|]+\n(.*?)(?=\n\n|$)', section_text, re.DOTALL)
            if table_match:
                table_rows = table_match.group(1).strip().split('\n')

                for row in table_rows:
                    # Parse table cells
                    cells = [cell.strip() for cell in row.split('|') if cell.strip()]

                    if len(cells) >= 7:
                        entity = {
                            "new_id": cells[0],
                            "entity_type": cells[1],
                            "name": cells[2],
                            "description": cells[3],
                            "department": cells[4].split(',') if cells[4] else [],
                            "source": cells[5],
                            "status": cells[6]
                        }
                        entities.append(entity)

            logger.info(f"Parsed {len(entities)} entities from CSV")

        except Exception as e:
            logger.error(f"Error parsing entity CSV: {e}")

        return entities

    def parse_department_distribution(self) -> Dict[str, int]:
        """
        Parse department distribution from analysis section

        Returns:
            Dictionary with entity counts by department
        """
        distribution = {}

        try:
            # Find department distribution section
            section = re.search(
                r'## Department Distribution\s+Analysis?\s*\n(.*?)(?=\n##|\Z)',
                self.content,
                re.DOTALL | re.IGNORECASE
            )

            if not section:
                logger.warning("Department Distribution section not found")
                return distribution

            section_text = section.group(2)

            # Parse markdown table
            table_match = re.search(r'\|.*Department.*\|.*\n\|[-\s|]+\n(.*?)(?=\n\n|$)', section_text, re.DOTALL)
            if table_match:
                table_rows = table_match.group(1).strip().split('\n')

                for row in table_rows:
                    cells = [cell.strip() for cell in row.split('|') if cell.strip()]
                    if len(cells) >= 2:
                        dept = cells[0]
                        try:
                            count = int(cells[1])
                            distribution[dept] = count
                        except ValueError:
                            continue

            logger.info(f"Parsed department distribution: {len(distribution)} departments")

        except Exception as e:
            logger.error(f"Error parsing department distribution: {e}")

        return distribution

    def get_section_text(self, section_header: str) -> str:
        """
        Extract text of a specific section by header

        Args:
            section_header: Section header (e.g., "## Workflows Identified")

        Returns:
            Section text content
        """
        pattern = f'{section_header}\\s*\\n(.*?)(?=\\n##|\\Z)'
        match = re.search(pattern, self.content, re.DOTALL | re.IGNORECASE)

        if match:
            return match.group(1).strip()

        return ""

    def count_lines(self) -> int:
        """Return total line count of transcription"""
        return len(self.content.split('\n'))

    def validate_structure(self) -> Dict[str, bool]:
        """
        Validate transcription has required sections

        Returns:
            Dictionary with validation results
        """
        required_sections = [
            "Metadata",
            "Workflows Identified",
            "Action Verbs",
            "Tools & Technologies Matrix",
            "Objects & Deliverables",
            "Entity ID Assignment & Master List"
        ]

        validation = {}
        for section in required_sections:
            validation[section] = bool(re.search(f'## {section}', self.content, re.IGNORECASE))

        return validation


# Standalone helper functions

def extract_video_id_from_markdown(file_path: Path) -> str:
    """
    Extract video ID from markdown filename or content

    Args:
        file_path: Path to markdown file

    Returns:
        Video ID (e.g., 'Video_023')
    """
    # Try filename first
    match = re.search(r'Video_(\d{3})', file_path.name)
    if match:
        return f"Video_{match.group(1)}"

    # Try content
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read(500)  # Read first 500 chars
            match = re.search(r'Video_(\d{3})', content)
            if match:
                return f"Video_{match.group(1)}"
    except:
        pass

    return ""


def list_transcription_files(transcriptions_dir: Path) -> List[Path]:
    """
    List all Video_XXX.md files in transcriptions directory

    Args:
        transcriptions_dir: Path to transcriptions directory

    Returns:
        List of transcription file paths
    """
    return sorted(transcriptions_dir.glob("Video_*.md"))
