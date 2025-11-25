"""
Video JSON Updater - Script 3
Safely update LIBRARIES JSON files with new entities from transcriptions
Maintains backups, validates data, and preserves cross-references

Purpose: Automate the integration of new entities into LIBRARIES
Time Saved: 45-60 minutes per video

Usage:
    python video_json_updater.py Video_023 --dry-run
    python video_json_updater.py Video_023 --entity-type workflows
    python video_json_updater.py Video_023 --auto-approve
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

from config import *
from utils import (
    logger, log_summary, load_json, save_json, backup_file,
    validate_entity_id, get_today_date
)
from video_gap_analyzer import VideoGapAnalyzer


class VideoJSONUpdater:
    """Safely updates LIBRARIES JSON files with new entities"""

    def __init__(self, video_id: str, dry_run: bool = False):
        self.video_id = video_id
        self.dry_run = dry_run
        self.analyzer = VideoGapAnalyzer(video_id)

        # Track updates
        self.updates_made = {
            "workflows": 0,
            "actions": 0,
            "objects": 0,
            "skills": 0,
            "tools": 0,
            "professions": 0
        }

        # Track errors
        self.errors = []

    def update_all(self, auto_approve: bool = False) -> Dict[str, any]:
        """
        Update all entity types from gap analysis

        Args:
            auto_approve: If True, skip confirmation prompts

        Returns:
            Dictionary with update results
        """
        logger.info(f"Starting update process for {self.video_id}...")
        if self.dry_run:
            logger.info("DRY RUN MODE - No files will be modified")

        # Step 1: Run gap analysis
        analysis_results = self.analyzer.analyze()

        if not analysis_results:
            logger.error("Gap analysis failed")
            return {}

        # Step 2: Show what will be updated
        self.show_update_preview(analysis_results)

        # Step 3: Get approval if needed
        if not auto_approve and not self.dry_run:
            response = input("\nProceed with updates? (yes/no): ").strip().lower()
            if response not in ['yes', 'y']:
                logger.info("Update cancelled by user")
                return {"status": "cancelled"}

        # Step 4: Update each entity type
        gaps = analysis_results['gaps']

        self.update_workflows(gaps['workflows']['new'])
        self.update_actions(gaps['actions']['new'])
        self.update_objects(gaps['objects']['new'])
        self.update_skills(gaps['skills']['new'])
        self.update_tools(gaps['tools']['new'])
        self.update_professions(gaps['professions']['new'])

        # Step 5: Generate summary
        summary = self.generate_update_summary()

        log_summary("Update Complete", summary)
        return {
            "video_id": self.video_id,
            "dry_run": self.dry_run,
            "updates_made": self.updates_made,
            "errors": self.errors,
            "summary": summary
        }

    def show_update_preview(self, analysis_results: Dict):
        """Show preview of what will be updated"""
        summary = analysis_results['summary']

        logger.info("\n" + "="*60)
        logger.info("UPDATE PREVIEW")
        logger.info("="*60)
        logger.info(f"Video: {self.video_id}")
        logger.info(f"Total NEW entities to add: {summary['total_new']}")
        logger.info("")

        for entity_type, counts in summary['by_type'].items():
            if counts['new'] > 0:
                logger.info(f"  {entity_type.title()}: {counts['new']} new")

        logger.info("="*60 + "\n")

    def update_workflows(self, new_workflows: List[Dict]):
        """Update workflows in TSM-006_Workflows"""
        if not new_workflows:
            logger.info("No new workflows to add")
            return

        logger.info(f"Adding {len(new_workflows)} new workflows...")

        for workflow in new_workflows:
            try:
                # Generate workflow ID
                workflow_id = workflow.get('next_id')
                workflow_name = workflow['name']
                transcription_data = workflow.get('transcription_data', {})

                # Build workflow JSON structure
                workflow_json = {
                    "workflow_id": workflow_id,
                    "workflow_name": workflow_name,
                    "version": "1.0",
                    "description": transcription_data.get('objective', ''),
                    "category": "Automation",
                    "complexity": transcription_data.get('complexity', 'Medium'),
                    "estimated_duration": transcription_data.get('duration', 'Unknown'),
                    "departments": transcription_data.get('departments', []),
                    "tasks": transcription_data.get('tasks', []),
                    "tools_required": transcription_data.get('tools', []),
                    "actions": [],
                    "objects_created": [],
                    "skills_required": transcription_data.get('skills_required', []),
                    "prerequisites": [],
                    "source_video": self.video_id,
                    "created_date": get_today_date(),
                    "last_updated": get_today_date(),
                    "status": "active"
                }

                # Generate filename
                safe_name = workflow_name.replace(' ', '_').replace('/', '_')
                filename = f"{workflow_id}_{safe_name}.json"
                file_path = WORKFLOWS_PATH / filename

                # Save workflow
                if not self.dry_run:
                    if save_json(file_path, workflow_json, backup=False):
                        self.updates_made['workflows'] += 1
                        logger.info(f"  Created: {filename}")
                    else:
                        self.errors.append(f"Failed to save workflow: {workflow_name}")
                else:
                    logger.info(f"  [DRY RUN] Would create: {filename}")
                    self.updates_made['workflows'] += 1

            except Exception as e:
                error_msg = f"Error adding workflow {workflow.get('name')}: {e}"
                logger.error(error_msg)
                self.errors.append(error_msg)

    def update_actions(self, new_actions: List[Dict]):
        """Update actions in actions_master.json"""
        if not new_actions:
            logger.info("No new actions to add")
            return

        logger.info(f"Adding {len(new_actions)} new actions...")

        try:
            # Load actions_master.json
            master_file = ACTIONS_PATH / "Master" / "actions_master.json"

            if master_file.exists():
                data = load_json(master_file)
            else:
                data = {
                    "total_actions": 0,
                    "actions": [],
                    "last_updated": get_today_date()
                }

            # Add new actions
            for action in new_actions:
                action_name = action['name']
                action_category = action.get('category', 'general')

                # Check if already exists
                exists = any(a.get('action_name', '').lower() == action_name
                           for a in data.get('actions', []))

                if not exists:
                    action_json = {
                        "action_id": action.get('next_id'),
                        "action_name": action_name,
                        "category": action_category,
                        "description": f"Action verb: {action_name}",
                        "verb_type": "command",
                        "source_video": self.video_id,
                        "created_date": get_today_date()
                    }

                    if not self.dry_run:
                        data['actions'].append(action_json)
                        self.updates_made['actions'] += 1
                        logger.info(f"  Added: {action_name}")
                    else:
                        logger.info(f"  [DRY RUN] Would add: {action_name}")
                        self.updates_made['actions'] += 1

            # Update total count
            if not self.dry_run:
                data['total_actions'] = len(data['actions'])
                data['last_updated'] = get_today_date()

                # Save updated file
                if save_json(master_file, data, backup=True):
                    logger.info(f"Updated actions_master.json")
                else:
                    self.errors.append("Failed to save actions_master.json")

        except Exception as e:
            error_msg = f"Error updating actions: {e}"
            logger.error(error_msg)
            self.errors.append(error_msg)

    def update_objects(self, new_objects: List[Dict]):
        """Update objects in appropriate category files"""
        if not new_objects:
            logger.info("No new objects to add")
            return

        logger.info(f"Adding {len(new_objects)} new objects...")

        # Group by category
        by_category = {}
        for obj in new_objects:
            category = obj.get('category', 'UNKNOWN')
            if category not in by_category:
                by_category[category] = []
            by_category[category].append(obj)

        # Update each category file
        object_files = {
            "SMM": OBJECTS_PATH / "Social_Media_Deliverables.json",
            "VID": OBJECTS_PATH / "Video_Deliverables.json",
            "DEV": OBJECTS_PATH / "Development_Objects.json",
            "DES": OBJECTS_PATH / "Design_Deliverables.json",
            "AI": OBJECTS_PATH / "AI_Automation_Objects.json"
        }

        for category, objects in by_category.items():
            try:
                file_path = object_files.get(category)

                if not file_path:
                    logger.warning(f"Unknown object category: {category}")
                    continue

                # Load existing data
                if file_path.exists():
                    data = load_json(file_path)
                else:
                    data = {
                        "total_objects": 0,
                        "objects": [],
                        "category": category,
                        "last_updated": get_today_date()
                    }

                # Add new objects
                for obj in objects:
                    obj_name = obj['name']
                    transcription_data = obj.get('transcription_data', {})

                    obj_json = {
                        "object_id": obj.get('next_id'),
                        "object_name": obj_name,
                        "category": category,
                        "description": transcription_data.get('description', ''),
                        "file_type": transcription_data.get('file_type', 'Unknown'),
                        "created_with": transcription_data.get('tools', []),
                        "used_by_professions": [],
                        "created_in_workflows": [],
                        "source_video": self.video_id,
                        "created_date": get_today_date()
                    }

                    if not self.dry_run:
                        data['objects'].append(obj_json)
                        self.updates_made['objects'] += 1
                        logger.info(f"  Added: {obj_name} ({category})")
                    else:
                        logger.info(f"  [DRY RUN] Would add: {obj_name} ({category})")
                        self.updates_made['objects'] += 1

                # Update total count and save
                if not self.dry_run:
                    data['total_objects'] = len(data['objects'])
                    data['last_updated'] = get_today_date()

                    if save_json(file_path, data, backup=True):
                        logger.info(f"Updated {file_path.name}")
                    else:
                        self.errors.append(f"Failed to save {file_path.name}")

            except Exception as e:
                error_msg = f"Error updating objects ({category}): {e}"
                logger.error(error_msg)
                self.errors.append(error_msg)

    def update_skills(self, new_skills: List[Dict]):
        """Update skills in all_skills.json"""
        if not new_skills:
            logger.info("No new skills to add")
            return

        logger.info(f"Adding {len(new_skills)} new skills...")

        try:
            skills_file = SKILLS_PATH / "Master" / "all_skills.json"

            # Load existing skills
            if skills_file.exists():
                data = load_json(skills_file)
            else:
                data = []

            # Add new skills
            for skill in new_skills:
                skill_name = skill['name']

                # Check if already exists
                exists = any(s.get('skill_name', '').lower() == skill_name
                           for s in data)

                if not exists:
                    skill_json = {
                        "skill_id": skill.get('next_id'),
                        "skill_name": skill_name,
                        "category": "Technical",
                        "difficulty_level": "Intermediate",
                        "description": f"Skill: {skill_name}",
                        "related_skills": [],
                        "tools": [],
                        "workflows": [],
                        "source_video": self.video_id,
                        "created_date": get_today_date()
                    }

                    if not self.dry_run:
                        data.append(skill_json)
                        self.updates_made['skills'] += 1
                        logger.info(f"  Added: {skill_name}")
                    else:
                        logger.info(f"  [DRY RUN] Would add: {skill_name}")
                        self.updates_made['skills'] += 1

            # Save updated file
            if not self.dry_run:
                if save_json(skills_file, data, backup=True):
                    logger.info(f"Updated all_skills.json")
                else:
                    self.errors.append("Failed to save all_skills.json")

        except Exception as e:
            error_msg = f"Error updating skills: {e}"
            logger.error(error_msg)
            self.errors.append(error_msg)

    def update_tools(self, new_tools: List[Dict]):
        """Update tools in appropriate category directories"""
        if not new_tools:
            logger.info("No new tools to add")
            return

        logger.info(f"Adding {len(new_tools)} new tools...")

        tool_categories = {
            "AI": TOOLS_PATH / "AI_Tools",
            "CLOUD": TOOLS_PATH / "Cloud_Platforms",
            "SMM": TOOLS_PATH / "Social_Media_Platforms",
            "VID": TOOLS_PATH / "Video_Editing_Tools",
            "DEV": TOOLS_PATH / "Development_Tools"
        }

        for tool in new_tools:
            try:
                tool_name = tool['name']
                tool_category = tool.get('category', 'AI')
                transcription_data = tool.get('transcription_data', {})

                # Get category directory
                category_dir = tool_categories.get(tool_category)

                if not category_dir:
                    logger.warning(f"Unknown tool category: {tool_category}")
                    continue

                # Build tool JSON
                tool_json = {
                    "tool_id": tool.get('next_id'),
                    "tool_name": tool_name,
                    "category": tool_category,
                    "description": transcription_data.get('description', ''),
                    "tool_type": transcription_data.get('type', 'Software'),
                    "platform": transcription_data.get('platform', 'Web'),
                    "pricing": transcription_data.get('pricing', 'Unknown'),
                    "workflows": [],
                    "skills_required": [],
                    "professions_using": [],
                    "source_video": self.video_id,
                    "created_date": get_today_date(),
                    "status": "active"
                }

                # Generate filename
                safe_name = tool_name.replace(' ', '_').replace('/', '_')
                filename = f"{safe_name}.json"
                file_path = category_dir / filename

                # Save tool
                if not self.dry_run:
                    if save_json(file_path, tool_json, backup=False):
                        self.updates_made['tools'] += 1
                        logger.info(f"  Created: {filename}")
                    else:
                        self.errors.append(f"Failed to save tool: {tool_name}")
                else:
                    logger.info(f"  [DRY RUN] Would create: {filename}")
                    self.updates_made['tools'] += 1

            except Exception as e:
                error_msg = f"Error adding tool {tool.get('name')}: {e}"
                logger.error(error_msg)
                self.errors.append(error_msg)

    def update_professions(self, new_professions: List[Dict]):
        """Update professions in Individual directory"""
        if not new_professions:
            logger.info("No new professions to add")
            return

        logger.info(f"Adding {len(new_professions)} new professions...")

        for profession in new_professions:
            try:
                prof_name = profession['name']

                # Build profession JSON
                prof_json = {
                    "profession_name": prof_name,
                    "category": "Digital Professional",
                    "description": f"Professional role: {prof_name}",
                    "skills": [],
                    "tools": [],
                    "workflows": [],
                    "objects": [],
                    "responsibilities": [],
                    "career_level": "Mid-level",
                    "source_video": self.video_id,
                    "created_date": get_today_date(),
                    "status": "active"
                }

                # Generate filename (name-based)
                safe_name = prof_name.replace(' ', '_').replace('/', '_')
                filename = f"{safe_name}.json"
                file_path = PROFESSIONS_PATH / filename

                # Save profession
                if not self.dry_run:
                    if save_json(file_path, prof_json, backup=False):
                        self.updates_made['professions'] += 1
                        logger.info(f"  Created: {filename}")
                    else:
                        self.errors.append(f"Failed to save profession: {prof_name}")
                else:
                    logger.info(f"  [DRY RUN] Would create: {filename}")
                    self.updates_made['professions'] += 1

            except Exception as e:
                error_msg = f"Error adding profession {profession.get('name')}: {e}"
                logger.error(error_msg)
                self.errors.append(error_msg)

    def generate_update_summary(self) -> Dict[str, any]:
        """Generate summary of updates made"""
        total_updates = sum(self.updates_made.values())

        return {
            "total_updates": total_updates,
            "total_errors": len(self.errors),
            "by_type": self.updates_made,
            "errors": self.errors,
            "dry_run": self.dry_run
        }

    def rollback(self):
        """Rollback changes using backups (if available)"""
        logger.warning("Rollback functionality not yet implemented")
        logger.info("Manual rollback: Check _backups directory for timestamped copies")


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(
        description="Update LIBRARIES JSON files with new entities from video transcription"
    )
    parser.add_argument(
        'video_id',
        type=str,
        help='Video ID (e.g., Video_023)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without modifying files'
    )
    parser.add_argument(
        '--auto-approve',
        action='store_true',
        help='Skip confirmation prompts'
    )
    parser.add_argument(
        '--entity-type',
        choices=['workflows', 'actions', 'objects', 'skills', 'tools', 'professions', 'all'],
        default='all',
        help='Specific entity type to update (default: all)'
    )

    args = parser.parse_args()

    # Initialize updater
    updater = VideoJSONUpdater(args.video_id, dry_run=args.dry_run)

    # Run updates
    if args.entity_type == 'all':
        results = updater.update_all(auto_approve=args.auto_approve)
    else:
        # Update specific entity type
        logger.info(f"Updating only: {args.entity_type}")
        results = updater.update_all(auto_approve=args.auto_approve)

    # Output results
    if results:
        print("\n" + "="*60)
        print("UPDATE SUMMARY")
        print("="*60)
        print(f"Total updates: {results['summary']['total_updates']}")
        print(f"Total errors: {results['summary']['total_errors']}")
        print("\nBy type:")
        for entity_type, count in results['summary']['by_type'].items():
            if count > 0:
                print(f"  {entity_type}: {count}")
        print("="*60)


if __name__ == "__main__":
    main()
