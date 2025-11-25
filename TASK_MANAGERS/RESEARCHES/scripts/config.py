"""
Configuration file for Video Transcription Processing Scripts
Defines paths, constants, and validation rules for universal video processing

UPDATED: 2025-11-24 for new architecture under TASK_MANAGERS/RESEARCHES
"""

from pathlib import Path

# Base paths - UPDATED ARCHITECTURE
BASE_PATH = Path(r"C:\Users\Dell\Dropbox\ENTITIES")
LIBRARIES_PATH = BASE_PATH / "LIBRARIES"
RESEARCHES_PATH = BASE_PATH / "TASK_MANAGERS" / "RESEARCHES"
TRANSCRIPTIONS_PATH = RESEARCHES_PATH / "02_TRANSCRIPTIONS"
ANALYSIS_PATH = RESEARCHES_PATH / "03_ANALYSIS"
INTEGRATION_PATH = RESEARCHES_PATH / "04_INTEGRATION"

# Task Managers and Libraries paths
WORKFLOWS_PATH = BASE_PATH / "TASK_MANAGERS" / "TSM-006_Workflows"
SKILLS_PATH = BASE_PATH / "TALENTS" / "Skills"
PROFESSIONS_PATH = LIBRARIES_PATH / "LBS_005_Professions" / "Individual"
TOOLS_PATH = LIBRARIES_PATH / "LBS_003_Tools"
ACTIONS_PATH = LIBRARIES_PATH / "Responsibilities" / "Actions"
OBJECTS_PATH = LIBRARIES_PATH / "Responsibilities" / "Objects"

# Script-specific paths
BACKUPS_PATH = RESEARCHES_PATH / "_backups"
SCRIPTS_PATH = RESEARCHES_PATH / "scripts"
TEMPLATES_PATH = RESEARCHES_PATH / "templates"
PROMPTS_PATH = RESEARCHES_PATH / "PROMPTS"
REPORTS_PATH = RESEARCHES_PATH / "REPORTS"
DATA_PATH = RESEARCHES_PATH / "DATA"

# Entity ID Prefixes
WORKFLOW_PREFIX = "WRF"
ACTION_PREFIX = "ACTION"
SKILL_PREFIX = "SKL"
TOOL_PREFIX = "TOOL"
PROFESSION_PREFIX = "PROF"

# Object category prefixes
OBJECT_PREFIXES = {
    "SMM": "OBJ-SMM",      # Social Media
    "VID": "OBJ-VID",      # Video
    "DEV": "OBJ-DEV",      # Development
    "DES": "OBJ-DES",      # Design
    "MKT": "OBJ-MKT",      # Marketing
    "HRM": "OBJ-HRM",      # Human Resources
    "SLS": "OBJ-SLS",      # Sales
    "LG": "OBJ-LG",        # Lead Generation
    "REC": "OBJ-REC",      # Recruitment
    "AI": "OBJ-AI"         # AI Automation
}

# Tool category codes
TOOL_CATEGORIES = {
    "AI": "TOOL-AI",
    "CLOUD": "TOOL-CLOUD",
    "SMM": "TOOL-SMM",
    "VID": "TOOL-VID",
    "DEV": "TOOL-DEV",
    "DES": "TOOL-DES",
    "DB": "TOOL-DB",
    "AUTH": "TOOL-AUTH"
}

# Valid department codes (ISO 3-letter format)
VALID_DEPARTMENTS = [
    "AID",  # AI & Automations
    "DEV",  # Development
    "VID",  # Video
    "SMM",  # Social Media Marketing
    "DGN",  # Design
    "MKT",  # Marketing
    "HRM",  # Human Resources
    "SLS",  # Sales
    "LG",   # Lead Generation
    "OPS",  # Operations
    "FIN",  # Finance
    "LGL"   # Legal
]

# Complexity levels
COMPLEXITY_LEVELS = ["Low", "Medium", "High"]

# Difficulty levels
DIFFICULTY_LEVELS = ["Beginner", "Intermediate", "Advanced", "Expert"]

# Entity types for validation
ENTITY_TYPES = [
    "WORKFLOW",
    "ACTION",
    "OBJECT",
    "SKILL",
    "TOOL",
    "PROFESSION",
    "INTEGRATION",
    "DEPARTMENT"
]

# File naming patterns
JSON_PATTERNS = {
    "workflow": "{prefix}-{id:03d}_{name}.json",
    "tool": "{name}.json",
    "profession": "{name}.json",
    "object": "{category}_Deliverables.json"
}

# CSV Section Headers in Transcription Files
CSV_SECTION_HEADER = "## Entity ID Assignment & Master List"
CSV_HEADERS = ["New_ID", "Entity_Type", "Name", "Description", "Department", "Source", "Status"]

# Quality thresholds
MIN_WORKFLOWS = 1          # Minimum workflows per video
MIN_TOOLS = 1              # Minimum tools per video
MIN_ACTIONS = 3            # Minimum actions per video
MIN_TRANSCRIPTION_LINES = 100  # Minimum lines for valid transcription

# Validation patterns
WORKFLOW_ID_PATTERN = r"WRF-\d{3}"
ACTION_ID_PATTERN = r"ACTION-\d{3}"
SKILL_ID_PATTERN = r"SKL-\d{3}"
OBJECT_ID_PATTERN = r"OBJ-[A-Z]{3}-\d{3}"
TOOL_ID_PATTERN = r"TOOL-[A-Z]{2,5}-\d{3}"

# Report templates
REPORT_TEMPLATES = {
    "gap_analysis": "gap_analysis_template.md",
    "integration_report": "integration_report_template.md",
    "mapping_report": "mapping_report_template.md"
}

# Logging configuration
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FILE = SCRIPTS_PATH / "process.log"
LOG_LEVEL = "INFO"

# Backup configuration
BACKUP_TIMESTAMP_FORMAT = "%Y%m%d_%H%M%S"
MAX_BACKUPS = 50  # Maximum number of backup copies to keep

# Cross-reference fields to validate
CROSS_REFERENCE_FIELDS = {
    "workflows": ["tools_required", "actions", "objects_created", "skills_required"],
    "tools": ["workflows", "skills_required", "professions_using"],
    "skills": ["related_skills", "tools", "workflows"],
    "professions": ["skills", "tools", "workflows", "objects"],
    "objects": ["created_with", "used_by_professions", "created_in_workflows"]
}

# Default metadata
DEFAULT_METADATA = {
    "version": "1.0",
    "status": "active",
    "created": None,  # Will be set to current date
    "last_updated": None  # Will be set to current date
}
