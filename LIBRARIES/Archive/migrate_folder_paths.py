"""
LIBRARIES Folder Path Migration Script

This script updates all references to old LIBRARIES folder paths to new LBS_XXX_Name format.
It processes markdown, Python, JSON, CSV, and other text files.

Migration Mapping:
- LIBRARIES/Responsibilities/Actions/ → LIBRARIES/Responsibilities/Actions/
- LIBRARIES/Responsibilities/Objects/ → LIBRARIES/Responsibilities/Objects/
- LIBRARIES/Tools/ → LIBRARIES/LBS_003_Tools/
- LIBRARIES/Skills/ → LIBRARIES/../TALENTS/Skills/
- LIBRARIES/Professions/ → LIBRARIES/LBS_005_Professions/
- LIBRARIES/DEPARTMENTS/ → LIBRARIES/LBS_006_Departments/
- LIBRARIES/Responsibilities/Parameters/ → LIBRARIES/Responsibilities/Parameters/
- LIBRARIES/Taxonomy/ → LIBRARIES/Taxonomy/
- LIBRARIES/Archive/ → LIBRARIES/Archive/

Usage:
    python migrate_folder_paths.py [--dry-run] [--backup] [--target-dir PATH]
"""

import os
import re
import json
import csv
import shutil
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple, Optional
import argparse

# Path mapping configuration
PATH_MAPPINGS = {
    # Old path patterns -> New path patterns
    'LIBRARIES/Responsibilities/Actions/': 'LIBRARIES/Responsibilities/Actions/',
    'LIBRARIES/Responsibilities/Objects/': 'LIBRARIES/Responsibilities/Objects/',
    'LIBRARIES/Tools/': 'LIBRARIES/LBS_003_Tools/',
    'LIBRARIES/Skills/': 'LIBRARIES/../TALENTS/Skills/',
    'LIBRARIES/Professions/': 'LIBRARIES/LBS_005_Professions/',
    'LIBRARIES/DEPARTMENTS/': 'LIBRARIES/LBS_006_Departments/',
    'LIBRARIES/Responsibilities/Parameters/': 'LIBRARIES/Responsibilities/Parameters/',
    'LIBRARIES/Taxonomy/': 'LIBRARIES/Taxonomy/',
    'LIBRARIES/Archive/': 'LIBRARIES/Archive/',
    
    # Relative paths (without LIBRARIES prefix)
    'Responsibilities/Actions/': 'Responsibilities/Actions/',
    'Responsibilities/Objects/': 'Responsibilities/Objects/',
    'Tools/': 'LBS_003_Tools/',
    'Skills/': '../TALENTS/Skills/',
    'Professions/': 'LBS_005_Professions/',
    'DEPARTMENTS/': 'LBS_006_Departments/',
    'Responsibilities/Parameters/': 'Responsibilities/Parameters/',
    'Taxonomy/': 'Taxonomy/',
    'Archive/': 'Archive/',
    
    # Internal subfolder mappings - keep original names, only update root
    'Tools/AI_Tools/': 'LBS_003_Tools/AI_Tools/',
    'Tools/Development_Tools/': 'LBS_003_Tools/Development_Tools/',
    'Tools/Social_Media_Platforms/': 'LBS_003_Tools/Social_Media_Platforms/',
    'Tools/Video_Editing_Tools/': 'LBS_003_Tools/Video_Editing_Tools/',
    'Tools/Automation_Tools/': 'LBS_003_Tools/Automation_Tools/',
    'Tools/Business_Tools/': 'LBS_003_Tools/Business_Tools/',
    'Tools/MCP_Services/': 'LBS_003_Tools/MCP_Services/',
    
    'LIBRARIES/Tools/AI_Tools/': 'LIBRARIES/LBS_003_Tools/AI_Tools/',
    'LIBRARIES/Tools/Development_Tools/': 'LIBRARIES/LBS_003_Tools/Development_Tools/',
    'LIBRARIES/Tools/Social_Media_Platforms/': 'LIBRARIES/LBS_003_Tools/Social_Media_Platforms/',
    'LIBRARIES/Tools/Video_Editing_Tools/': 'LIBRARIES/LBS_003_Tools/Video_Editing_Tools/',
    'LIBRARIES/Tools/Automation_Tools/': 'LIBRARIES/LBS_003_Tools/Automation_Tools/',
    'LIBRARIES/Tools/Business_Tools/': 'LIBRARIES/LBS_003_Tools/Business_Tools/',
    'LIBRARIES/Tools/MCP_Services/': 'LIBRARIES/LBS_003_Tools/MCP_Services/',
    
    # Skills subfolder mappings
    'Skills/Master/': '../TALENTS/Skills/Master/',
    'Skills/By_Department/': '../TALENTS/Skills/By_Department/',
    'Skills/By_Profession/': '../TALENTS/Skills/By_Profession/',
    'Skills/By_Difficulty/': '../TALENTS/Skills/By_Difficulty/',
    
    'LIBRARIES/Skills/Master/': 'LIBRARIES/../TALENTS/Skills/Master/',
    'LIBRARIES/Skills/By_Department/': 'LIBRARIES/../TALENTS/Skills/By_Department/',
    'LIBRARIES/Skills/By_Profession/': 'LIBRARIES/../TALENTS/Skills/By_Profession/',
    'LIBRARIES/Skills/By_Difficulty/': 'LIBRARIES/../TALENTS/Skills/By_Difficulty/',
    
    # Professions mappings
    'Professions/professions.json': 'LBS_005_Professions/Master/professions.json',
    'LIBRARIES/Professions/professions.json': 'LIBRARIES/LBS_005_Professions/Master/professions.json',
    
    # Departments mappings
    'DEPARTMENTS/departments.json': 'LBS_006_Departments/Master/departments.json',
    'LIBRARIES/DEPARTMENTS/departments.json': 'LIBRARIES/LBS_006_Departments/Master/departments.json',
    
    # Parameters mappings
    'Responsibilities/Parameters/organized_by_profession/': 'Responsibilities/Parameters/By_Profession/',
    'Responsibilities/Parameters/organized_by_department/': 'Responsibilities/Parameters/By_Department/',
    'LIBRARIES/Responsibilities/Parameters/organized_by_profession/': 'LIBRARIES/Responsibilities/Parameters/By_Profession/',
    'LIBRARIES/Responsibilities/Parameters/organized_by_department/': 'LIBRARIES/Responsibilities/Parameters/By_Department/',
    
    # Actions file mappings
    'Responsibilities/Actions/Actions_Master.json': 'Responsibilities/Actions/Master/actions_master.json',
    'LIBRARIES/Responsibilities/Actions/Actions_Master.json': 'LIBRARIES/Responsibilities/Actions/Master/actions_master.json',
    'Responsibilities/Actions/Video_Generation_Actions.json': 'Responsibilities/Actions/By_Domain/video_generation_actions.json',
    'LIBRARIES/Responsibilities/Actions/Video_Generation_Actions.json': 'LIBRARIES/Responsibilities/Actions/By_Domain/video_generation_actions.json',
}

# File extensions to process
TEXT_EXTENSIONS = {'.md', '.py', '.json', '.csv', '.txt', '.yaml', '.yml', '.rst', '.html', '.js', '.ts', '.tsx', '.jsx'}

# Files/directories to skip
SKIP_PATTERNS = {
    '.git',
    '__pycache__',
    '.pytest_cache',
    'node_modules',
    '.venv',
    'venv',
    'env',
    '.env',
    'migrate_folder_paths.py',  # Skip self
    'migration_log.json',  # Skip log files
    'migration_report.md',
}


class PathMigrator:
    """
    Handles migration of folder path references in files.
    
    Attributes:
        base_path: Base directory to process
        dry_run: If True, don't modify files, only report changes
        backup: If True, create backup before modifying
        changes_log: List of all changes made
        files_processed: Set of files processed
        errors: List of errors encountered
    """
    
    def __init__(self, base_path: Path, dry_run: bool = False, backup: bool = False):
        """
        Initialize migrator.
        
        Args:
            base_path: Base directory to process
            dry_run: If True, don't modify files
            backup: If True, create backups
        """
        self.base_path = Path(base_path).resolve()
        self.dry_run = dry_run
        self.backup = backup
        self.changes_log: List[Dict] = []
        self.files_processed: set = set()
        self.errors: List[Dict] = []
        
        # Create backup directory if needed
        if backup and not dry_run:
            self.backup_dir = self.base_path / f'backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
            self.backup_dir.mkdir(exist_ok=True)
    
    def should_skip(self, file_path: Path) -> bool:
        """
        Check if file should be skipped.
        
        Args:
            file_path: Path to check
            
        Returns:
            True if file should be skipped
        """
        # Check skip patterns
        for pattern in SKIP_PATTERNS:
            if pattern in str(file_path):
                return True
        
        # Check if it's a binary file (basic check)
        if file_path.suffix.lower() not in TEXT_EXTENSIONS:
            return True
        
        return False
    
    def update_content(self, content: str, file_path: Path) -> Tuple[str, List[Dict]]:
        """
        Update path references in content.
        
        Args:
            content: File content to update
            file_path: Path of file being processed
            
        Returns:
            Tuple of (updated_content, list_of_changes)
        """
        changes = []
        updated_content = content
        
        # Sort mappings by length (longest first) to handle nested paths correctly
        sorted_mappings = sorted(PATH_MAPPINGS.items(), key=lambda x: len(x[0]), reverse=True)
        
        for old_path, new_path in sorted_mappings:
            # Count occurrences
            count = content.count(old_path)
            if count > 0:
                # Replace all occurrences
                updated_content = updated_content.replace(old_path, new_path)
                
                changes.append({
                    'old_path': old_path,
                    'new_path': new_path,
                    'count': count,
                    'file': str(file_path.relative_to(self.base_path))
                })
        
        return updated_content, changes
    
    def process_file(self, file_path: Path) -> bool:
        """
        Process a single file.
        
        Args:
            file_path: Path to file
            
        Returns:
            True if file was modified
        """
        if self.should_skip(file_path):
            return False
        
        try:
            # Read file
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                original_content = f.read()
            
            # Update content
            updated_content, changes = self.update_content(original_content, file_path)
            
            if not changes:
                return False  # No changes needed
            
            # Create backup if requested
            if self.backup and not self.dry_run:
                backup_path = self.backup_dir / file_path.relative_to(self.base_path)
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file_path, backup_path)
            
            # Write updated content
            if not self.dry_run:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
            
            # Log changes
            self.changes_log.extend(changes)
            self.files_processed.add(str(file_path.relative_to(self.base_path)))
            
            return True
            
        except Exception as e:
            self.errors.append({
                'file': str(file_path.relative_to(self.base_path)),
                'error': str(e)
            })
            return False
    
    def process_directory(self, directory: Optional[Path] = None) -> None:
        """
        Process all files in directory recursively.
        
        Args:
            directory: Directory to process (defaults to base_path)
        """
        if directory is None:
            directory = self.base_path
        
        directory = Path(directory).resolve()
        
        # Process all files
        for file_path in directory.rglob('*'):
            if file_path.is_file():
                self.process_file(file_path)
    
    def generate_report(self) -> Dict:
        """
        Generate migration report.
        
        Returns:
            Dictionary with report data
        """
        # Group changes by file
        changes_by_file: Dict[str, List[Dict]] = {}
        for change in self.changes_log:
            file = change['file']
            if file not in changes_by_file:
                changes_by_file[file] = []
            changes_by_file[file].append(change)
        
        # Count total replacements
        total_replacements = sum(change['count'] for change in self.changes_log)
        
        # Group by path mapping
        changes_by_path: Dict[str, int] = {}
        for change in self.changes_log:
            key = f"{change['old_path']} → {change['new_path']}"
            changes_by_path[key] = changes_by_path.get(key, 0) + change['count']
        
        return {
            'timestamp': datetime.now().isoformat(),
            'dry_run': self.dry_run,
            'files_processed': len(self.files_processed),
            'total_replacements': total_replacements,
            'unique_path_mappings': len(changes_by_path),
            'changes_by_file': changes_by_file,
            'changes_by_path': changes_by_path,
            'errors': self.errors
        }
    
    def save_report(self, report_path: Optional[Path] = None) -> None:
        """
        Save migration report to JSON and Markdown.
        
        Args:
            report_path: Path to save report (defaults to base_path/migration_report)
        """
        if report_path is None:
            report_path = self.base_path / 'migration_report'
        
        report = self.generate_report()
        
        # Save JSON report
        json_path = Path(f"{report_path}.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        # Save Markdown report
        md_path = Path(f"{report_path}.md")
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(f"# LIBRARIES Folder Path Migration Report\n\n")
            f.write(f"**Generated:** {report['timestamp']}\n")
            f.write(f"**Mode:** {'DRY RUN' if report['dry_run'] else 'LIVE'}\n\n")
            f.write(f"## Summary\n\n")
            f.write(f"- **Files Processed:** {report['files_processed']}\n")
            f.write(f"- **Total Replacements:** {report['total_replacements']}\n")
            f.write(f"- **Unique Path Mappings:** {report['unique_path_mappings']}\n")
            f.write(f"- **Errors:** {len(report['errors'])}\n\n")
            
            if report['errors']:
                f.write(f"## Errors\n\n")
                for error in report['errors']:
                    f.write(f"- **{error['file']}**: {error['error']}\n")
                f.write(f"\n")
            
            f.write(f"## Path Mappings Applied\n\n")
            for mapping, count in sorted(report['changes_by_path'].items(), key=lambda x: x[1], reverse=True):
                f.write(f"- `{mapping}`: {count} replacements\n")
            f.write(f"\n")
            
            f.write(f"## Files Modified\n\n")
            for file, changes in sorted(report['changes_by_file'].items()):
                f.write(f"### {file}\n\n")
                for change in changes:
                    f.write(f"- `{change['old_path']}` → `{change['new_path']}` ({change['count']} replacements)\n")
                f.write(f"\n")
        
        print(f"\n[OK] Reports saved:")
        print(f"  - JSON: {json_path}")
        print(f"  - Markdown: {md_path}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Migrate LIBRARIES folder path references to new LBS_XXX_Name format'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Run without modifying files (default: False)'
    )
    parser.add_argument(
        '--backup',
        action='store_true',
        help='Create backup before modifying files (default: False)'
    )
    parser.add_argument(
        '--target-dir',
        type=str,
        default=None,
        help='Target directory to process (default: script directory)'
    )
    
    args = parser.parse_args()
    
    # Determine base path
    if args.target_dir:
        base_path = Path(args.target_dir).resolve()
    else:
        # Default to script's parent directory (LIBRARIES)
        base_path = Path(__file__).parent.resolve()
    
    if not base_path.exists():
        print(f"Error: Directory does not exist: {base_path}")
        return 1
    
    print(f"LIBRARIES Folder Path Migration")
    print(f"{'=' * 50}")
    print(f"Base Path: {base_path}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print(f"Backup: {'Yes' if args.backup else 'No'}")
    print(f"{'=' * 50}\n")
    
    # Create migrator
    migrator = PathMigrator(base_path, dry_run=args.dry_run, backup=args.backup)
    
    # Process files
    print("Processing files...")
    migrator.process_directory()
    
    # Generate and save report
    print("\nGenerating report...")
    migrator.save_report()
    
    # Print summary
    report = migrator.generate_report()
    print(f"\n{'=' * 50}")
    print(f"Migration Complete!")
    print(f"{'=' * 50}")
    print(f"Files Processed: {report['files_processed']}")
    print(f"Total Replacements: {report['total_replacements']}")
    print(f"Errors: {len(report['errors'])}")
    
    if report['errors']:
        print(f"\nErrors encountered:")
        for error in report['errors']:
            print(f"  - {error['file']}: {error['error']}")
    
    return 0


if __name__ == '__main__':
    exit(main())

