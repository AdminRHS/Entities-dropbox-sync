"""
Utility functions shared across video processing scripts

UPDATED: 2025-11-24 for new architecture under TASK_MANAGERS/RESEARCHES
"""

import json
import shutil
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any
import re

from config import *

# Setup logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def load_json(file_path: Path) -> Dict:
    """
    Safely load JSON file with error handling
    Handles UTF-8 BOM if present

    Args:
        file_path: Path to JSON file

    Returns:
        Dictionary containing JSON data
    """
    try:
        # Try with utf-8-sig first (handles BOM)
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in {file_path}: {e}")
        raise
    except Exception as e:
        logger.error(f"Error loading {file_path}: {e}")
        raise


def save_json(file_path: Path, data: Dict, backup: bool = True) -> bool:
    """
    Safely save JSON file with optional backup

    Args:
        file_path: Path to JSON file
        data: Dictionary to save
        backup: Whether to create backup before saving

    Returns:
        True if successful, False otherwise
    """
    try:
        # Create backup if requested and file exists
        if backup and file_path.exists():
            backup_file(file_path)

        # Ensure directory exists
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Save JSON with pretty formatting
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        logger.info(f"Saved: {file_path}")
        return True

    except Exception as e:
        logger.error(f"Error saving {file_path}: {e}")
        return False


def backup_file(file_path: Path) -> Optional[Path]:
    """
    Create timestamped backup of file

    Args:
        file_path: Path to file to backup

    Returns:
        Path to backup file, or None if failed
    """
    try:
        if not file_path.exists():
            logger.warning(f"File does not exist for backup: {file_path}")
            return None

        # Create backup filename with timestamp
        timestamp = datetime.now().strftime(BACKUP_TIMESTAMP_FORMAT)
        backup_name = f"{file_path.stem}_{timestamp}{file_path.suffix}"
        backup_path = BACKUPS_PATH / backup_name

        # Ensure backup directory exists
        BACKUPS_PATH.mkdir(parents=True, exist_ok=True)

        # Copy file to backup
        shutil.copy2(file_path, backup_path)
        logger.info(f"Backed up: {file_path} → {backup_path}")

        # Clean old backups
        cleanup_old_backups()

        return backup_path

    except Exception as e:
        logger.error(f"Error backing up {file_path}: {e}")
        return None


def cleanup_old_backups():
    """Remove old backup files exceeding MAX_BACKUPS limit"""
    try:
        backups = sorted(BACKUPS_PATH.glob("*"), key=lambda p: p.stat().st_mtime, reverse=True)

        if len(backups) > MAX_BACKUPS:
            for backup in backups[MAX_BACKUPS:]:
                backup.unlink()
                logger.info(f"Removed old backup: {backup}")

    except Exception as e:
        logger.error(f"Error cleaning up backups: {e}")


def validate_json_schema(data: Dict, required_fields: List[str]) -> bool:
    """
    Validate JSON data has required fields

    Args:
        data: Dictionary to validate
        required_fields: List of required field names

    Returns:
        True if valid, False otherwise
    """
    for field in required_fields:
        if field not in data:
            logger.error(f"Missing required field: {field}")
            return False
    return True


def get_next_id(existing_ids: List[str], prefix: str, width: int = 3) -> str:
    """
    Get next sequential ID given list of existing IDs

    Args:
        existing_ids: List of existing IDs (e.g., ['WRF-001', 'WRF-002'])
        prefix: ID prefix (e.g., 'WRF')
        width: Number of digits for ID (default: 3)

    Returns:
        Next sequential ID (e.g., 'WRF-003')
    """
    if not existing_ids:
        return f"{prefix}-{1:0{width}d}"

    # Extract numeric parts
    numbers = []
    for id_str in existing_ids:
        match = re.search(r'(\d+)', id_str)
        if match:
            numbers.append(int(match.group(1)))

    if not numbers:
        return f"{prefix}-{1:0{width}d}"

    max_num = max(numbers)
    return f"{prefix}-{max_num + 1:0{width}d}"


def parse_csv_section(content: str, section_header: str = CSV_SECTION_HEADER) -> List[Dict]:
    """
    Parse CSV section from markdown transcription file

    Args:
        content: Full markdown content
        section_header: Header marking start of CSV section

    Returns:
        List of dictionaries representing CSV rows
    """
    try:
        # Find CSV section
        if section_header not in content:
            logger.warning(f"CSV section not found: {section_header}")
            return []

        # Extract section
        section_start = content.index(section_header)
        section_content = content[section_start:]

        # Find CSV data (starts after header, ends at next ## or end of file)
        lines = section_content.split('\n')
        csv_lines = []
        in_csv = False

        for line in lines:
            if line.strip().startswith('|') and 'New_ID' in line:
                in_csv = True
                continue  # Skip header row
            elif line.strip().startswith('|---'):
                continue  # Skip separator row
            elif in_csv and line.strip().startswith('|'):
                csv_lines.append(line)
            elif in_csv and line.strip().startswith('##'):
                break  # End of CSV section

        # Parse CSV lines
        entities = []
        for line in csv_lines:
            # Split by | and clean
            parts = [p.strip() for p in line.split('|') if p.strip()]

            if len(parts) >= 7:
                entity = {
                    "new_id": parts[0],
                    "entity_type": parts[1],
                    "name": parts[2],
                    "description": parts[3],
                    "department": parts[4],
                    "source": parts[5],
                    "status": parts[6]
                }
                entities.append(entity)

        logger.info(f"Parsed {len(entities)} entities from CSV section")
        return entities

    except Exception as e:
        logger.error(f"Error parsing CSV section: {e}")
        return []


def get_today_date() -> str:
    """Get today's date in YYYY-MM-DD format"""
    return datetime.now().strftime("%Y-%m-%d")


def validate_department_code(code: str) -> bool:
    """Validate department code against allowed list"""
    return code in VALID_DEPARTMENTS


def validate_entity_id(entity_id: str, entity_type: str) -> bool:
    """
    Validate entity ID format

    Args:
        entity_id: ID to validate (e.g., 'WRF-021')
        entity_type: Type of entity ('WORKFLOW', 'ACTION', etc.)

    Returns:
        True if valid format, False otherwise
    """
    patterns = {
        "WORKFLOW": WORKFLOW_ID_PATTERN,
        "ACTION": ACTION_ID_PATTERN,
        "SKILL": SKILL_ID_PATTERN,
        "OBJECT": OBJECT_ID_PATTERN,
        "TOOL": TOOL_ID_PATTERN
    }

    pattern = patterns.get(entity_type.upper())
    if not pattern:
        logger.warning(f"Unknown entity type: {entity_type}")
        return False

    return bool(re.match(pattern, entity_id))


def extract_video_number(video_id: str) -> int:
    """
    Extract numeric part from video ID

    Args:
        video_id: Video identifier (e.g., 'Video_023' or '023')

    Returns:
        Numeric video number
    """
    match = re.search(r'(\d+)', video_id)
    if match:
        return int(match.group(1))
    raise ValueError(f"Invalid video ID format: {video_id}")


def format_video_id(video_num: int) -> str:
    """
    Format video number as Video_XXX

    Args:
        video_num: Numeric video number

    Returns:
        Formatted video ID (e.g., 'Video_023')
    """
    return f"Video_{video_num:03d}"


def count_entities_by_type(entities: List[Dict]) -> Dict[str, int]:
    """
    Count entities by type

    Args:
        entities: List of entity dictionaries

    Returns:
        Dictionary with counts by entity type
    """
    counts = {}
    for entity in entities:
        entity_type = entity.get('entity_type', 'Unknown')
        counts[entity_type] = counts.get(entity_type, 0) + 1
    return counts


def count_entities_by_department(entities: List[Dict]) -> Dict[str, int]:
    """
    Count entities by department

    Args:
        entities: List of entity dictionaries

    Returns:
        Dictionary with counts by department
    """
    counts = {}
    for entity in entities:
        # Department can be a string or list
        depts = entity.get('department', [])
        if isinstance(depts, str):
            depts = [depts]

        for dept in depts:
            dept = dept.strip()
            counts[dept] = counts.get(dept, 0) + 1

    return counts


def create_markdown_table(headers: List[str], rows: List[List[str]]) -> str:
    """
    Create markdown table from headers and rows

    Args:
        headers: List of column headers
        rows: List of rows (each row is list of values)

    Returns:
        Formatted markdown table string
    """
    # Calculate column widths
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(val)))

    # Build table
    lines = []

    # Header row
    header_line = "| " + " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers)) + " |"
    lines.append(header_line)

    # Separator row
    sep_line = "|" + "|".join("-" * (w + 2) for w in col_widths) + "|"
    lines.append(sep_line)

    # Data rows
    for row in rows:
        row_line = "| " + " | ".join(str(val).ljust(col_widths[i]) for i, val in enumerate(row)) + " |"
        lines.append(row_line)

    return "\n".join(lines)


def log_summary(title: str, details: Dict[str, Any]):
    """
    Log formatted summary

    Args:
        title: Summary title
        details: Dictionary of key-value pairs to log
    """
    logger.info(f"\n{'='*60}")
    logger.info(f"{title}")
    logger.info(f"{'='*60}")
    for key, value in details.items():
        logger.info(f"{key}: {value}")
    logger.info(f"{'='*60}\n")
