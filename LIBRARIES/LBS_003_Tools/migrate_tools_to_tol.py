#!/usr/bin/env python3
"""
Tool ID Migration Script: TOOL-[CAT]-### → TOL-###
Migrates all tool files to Taxonomy TOL-### format with flat directory structure.

Author: Claude Code
Date: 2025-11-25
Version: 1.0
"""

import json
import os
import sys
import csv
import shutil
import hashlib
import zipfile
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import re

# Configuration
TOOLS_DIR = r"C:\Users\delir\Dropbox\Dropbox\ENTITIES\LIBRARIES\LBS_003_Tools"
TAXONOMY_CSV = r"C:\Users\delir\Dropbox\Dropbox\ENTITIES\TAXONOMY\TAX-001_Libraries\Tools_Master_List.csv"
LOG_DIR = r"C:\Users\delir\Dropbox\Dropbox\ENTITIES\DAILIES\LOG\Week_4"
REPORT_DIR = r"C:\Users\delir\Dropbox\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4"
CHECKPOINT_INTERVAL = 10

# Create output directories if they don't exist
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

# Global log file
LOG_FILE = os.path.join(LOG_DIR, f"migration_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")


def log(message: str, level: str = "INFO"):
    """Log message to console and file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [{level}] {message}"
    print(log_line)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_line + '\n')


def calculate_sha256(filepath: str) -> str:
    """Calculate SHA256 hash of file"""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def normalize_tool_name(name: str) -> str:
    """
    Normalize tool name for filename
    Rules:
    - Replace spaces with underscores
    - Remove special chars except underscore
    - Keep existing underscores
    - Preserve case
    """
    # Replace spaces with underscores
    name = name.replace(" ", "_")
    # Remove special characters except underscores and alphanumeric
    name = re.sub(r'[^\w]', '_', name)
    # Remove multiple consecutive underscores
    name = re.sub(r'_+', '_', name)
    # Remove leading/trailing underscores
    name = name.strip('_')
    return name


class ToolMigration:
    def __init__(self):
        self.tools_dir = Path(TOOLS_DIR)
        self.taxonomy_csv = Path(TAXONOMY_CSV)
        self.log_dir = Path(LOG_DIR)
        self.report_dir = Path(REPORT_DIR)

        self.taxonomy_map: Dict[str, Dict] = {}
        self.current_tools: List[Dict] = []
        self.mapping_table: List[Dict] = []
        self.checkpoint_file = self.log_dir / "migration_checkpoint.json"
        self.files_to_delete: List[str] = []

        log("Tool Migration Script Initialized")
        log(f"Tools Directory: {self.tools_dir}")
        log(f"Taxonomy CSV: {self.taxonomy_csv}")

    # ================================================================================
    # PHASE 1: PRE-MIGRATION PREPARATION
    # ================================================================================

    def phase1_backup(self) -> bool:
        """Phase 1.1: Create complete backup"""
        log("=" * 80)
        log("PHASE 1.1: Creating Complete Backup")
        log("=" * 80)

        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_dir = self.tools_dir.parent / f"LBS_003_Tools_BACKUP_{timestamp}"

            log(f"Creating backup directory: {backup_dir}")
            shutil.copytree(self.tools_dir, backup_dir)

            # Generate manifest with SHA256 hashes
            manifest = {
                "backup_date": datetime.now().isoformat(),
                "source_directory": str(self.tools_dir),
                "file_count": 0,
                "total_size_bytes": 0,
                "files": []
            }

            for root, dirs, files in os.walk(backup_dir):
                for file in files:
                    if file.endswith('.json'):
                        filepath = os.path.join(root, file)
                        rel_path = os.path.relpath(filepath, backup_dir)
                        file_size = os.path.getsize(filepath)
                        file_hash = calculate_sha256(filepath)

                        manifest["files"].append({
                            "path": rel_path,
                            "size": file_size,
                            "sha256": file_hash
                        })
                        manifest["file_count"] += 1
                        manifest["total_size_bytes"] += file_size

            # Save manifest
            manifest_path = backup_dir / "backup_manifest.json"
            with open(manifest_path, 'w', encoding='utf-8') as f:
                json.dump(manifest, f, indent=2)

            log(f"✓ Backup created: {manifest['file_count']} files, {manifest['total_size_bytes']:,} bytes")

            # Create ZIP archive
            zip_path = str(backup_dir) + ".zip"
            log(f"Creating ZIP archive: {zip_path}")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(backup_dir):
                    for file in files:
                        filepath = os.path.join(root, file)
                        arcname = os.path.relpath(filepath, backup_dir.parent)
                        zipf.write(filepath, arcname)

            log(f"✓ ZIP archive created: {zip_path}")
            log("✓ Phase 1.1 Complete: Backup created successfully")
            return True

        except Exception as e:
            log(f"✗ Phase 1.1 Failed: {str(e)}", "ERROR")
            return False

    def phase1_load_taxonomy(self) -> bool:
        """Phase 1.2: Load taxonomy mapping from CSV"""
        log("=" * 80)
        log("PHASE 1.2: Loading Taxonomy Mapping")
        log("=" * 80)

        try:
            if not self.taxonomy_csv.exists():
                log(f"✗ Taxonomy CSV not found: {self.taxonomy_csv}", "ERROR")
                return False

            with open(self.taxonomy_csv, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    tool_id = row.get('Tool_ID', '').strip()
                    tool_name = row.get('Tool_Name', '').strip()

                    if tool_id and tool_name:
                        self.taxonomy_map[tool_name.lower()] = {
                            'tool_id': tool_id,
                            'tool_name': tool_name,
                            'category': row.get('Category', ''),
                            'mention_count': row.get('Mention_Count', '0'),
                            'priority': row.get('Priority', ''),
                            'filename': row.get('Filename', '')
                        }

            log(f"✓ Loaded {len(self.taxonomy_map)} tools from taxonomy")
            return True

        except Exception as e:
            log(f"✗ Failed to load taxonomy: {str(e)}", "ERROR")
            return False

    def phase1_inventory(self) -> bool:
        """Phase 1.2: Create inventory of current tool files"""
        log("=" * 80)
        log("PHASE 1.2: Creating Tool Inventory")
        log("=" * 80)

        try:
            for root, dirs, files in os.walk(self.tools_dir):
                # Skip _ARCHIVE directory
                if '_ARCHIVE' in Path(root).parts:
                    continue

                for file in files:
                    if file.endswith('.json') and file != 'backup_manifest.json':
                        filepath = os.path.join(root, file)
                        rel_path = os.path.relpath(filepath, self.tools_dir)

                        try:
                            with open(filepath, 'r', encoding='utf-8') as f:
                                data = json.load(f)

                            tool_entry = {
                                'current_path': rel_path,
                                'full_path': filepath,
                                'current_tool_id': data.get('tool_id', ''),
                                'tool_name': data.get('name', ''),
                                'current_filename': file,
                                'subdirectory': os.path.dirname(rel_path),
                                'file_size': os.path.getsize(filepath),
                                'last_modified': datetime.fromtimestamp(os.path.getmtime(filepath)).isoformat()
                            }

                            self.current_tools.append(tool_entry)

                        except Exception as e:
                            log(f"⚠ Failed to read {file}: {str(e)}", "WARNING")

            log(f"✓ Inventory complete: {len(self.current_tools)} tool files found")

            # Save inventory
            inventory_path = self.report_dir / "pre_migration_inventory.csv"
            with open(inventory_path, 'w', newline='', encoding='utf-8') as f:
                if self.current_tools:
                    writer = csv.DictWriter(f, fieldnames=self.current_tools[0].keys())
                    writer.writeheader()
                    writer.writerows(self.current_tools)

            log(f"✓ Inventory saved: {inventory_path}")
            return True

        except Exception as e:
            log(f"✗ Inventory failed: {str(e)}", "ERROR")
            return False

    def phase1_create_mapping(self) -> bool:
        """Phase 1.2: Create master mapping table"""
        log("=" * 80)
        log("PHASE 1.2: Creating Master Mapping Table")
        log("=" * 80)

        unmapped_tools = []
        duplicates = {}

        for tool in self.current_tools:
            tool_name = tool['tool_name']
            tool_name_key = tool_name.lower().strip()

            # Try to find in taxonomy
            taxonomy_entry = self.taxonomy_map.get(tool_name_key)

            if taxonomy_entry:
                new_tol_id = taxonomy_entry['tool_id']
                normalized_name = normalize_tool_name(tool_name)
                new_filename = f"{new_tol_id}_{normalized_name}.json"
                action = "MIGRATE"

                # Check for duplicates
                if new_tol_id not in duplicates:
                    duplicates[new_tol_id] = []
                duplicates[new_tol_id].append(tool)

            else:
                new_tol_id = "UNMAPPED"
                new_filename = "MANUAL_REVIEW_NEEDED"
                action = "SKIP"
                unmapped_tools.append(tool)

            mapping_entry = {
                'current_path': tool['current_path'],
                'current_tool_id': tool['current_tool_id'],
                'current_filename': tool['current_filename'],
                'tool_name': tool_name,
                'new_tol_id': new_tol_id,
                'new_filename': new_filename,
                'new_path': f"{new_filename}" if new_filename != "MANUAL_REVIEW_NEEDED" else "SKIP",
                'action': action,
                'taxonomy_priority': taxonomy_entry.get('priority', '') if taxonomy_entry else '',
                'mention_count': taxonomy_entry.get('mention_count', '') if taxonomy_entry else ''
            }

            self.mapping_table.append(mapping_entry)

        # Handle duplicates
        duplicate_report = []
        for tol_id, tools in duplicates.items():
            if len(tools) > 1:
                log(f"⚠ Duplicate found for {tol_id}: {len(tools)} files", "WARNING")
                # Keep newest/largest file
                tools.sort(key=lambda x: (x['last_modified'], x['file_size']), reverse=True)
                keep_file = tools[0]
                delete_files = tools[1:]

                duplicate_report.append({
                    'tool_id': tol_id,
                    'tool_name': keep_file['tool_name'],
                    'keep_file': keep_file['current_path'],
                    'delete_files': [t['current_path'] for t in delete_files],
                    'reason': 'Keeping newest/largest file'
                })

                # Mark duplicates for deletion
                for dup in delete_files:
                    for mapping in self.mapping_table:
                        if mapping['current_path'] == dup['current_path']:
                            mapping['action'] = 'DELETE'
                            self.files_to_delete.append(dup['full_path'])

        # Save mapping table
        mapping_path = self.report_dir / "migration_mapping_table.csv"
        with open(mapping_path, 'w', newline='', encoding='utf-8') as f:
            if self.mapping_table:
                writer = csv.DictWriter(f, fieldnames=self.mapping_table[0].keys())
                writer.writeheader()
                writer.writerows(self.mapping_table)

        log(f"✓ Mapping table created: {len(self.mapping_table)} entries")
        log(f"  - MIGRATE: {sum(1 for m in self.mapping_table if m['action'] == 'MIGRATE')}")
        log(f"  - DELETE: {sum(1 for m in self.mapping_table if m['action'] == 'DELETE')}")
        log(f"  - SKIP: {sum(1 for m in self.mapping_table if m['action'] == 'SKIP')}")
        log(f"✓ Mapping table saved: {mapping_path}")

        # Save unmapped tools
        if unmapped_tools:
            unmapped_path = self.report_dir / "unmapped_tools_report.csv"
            with open(unmapped_path, 'w', newline='', encoding='utf-8') as f:
                if unmapped_tools:
                    writer = csv.DictWriter(f, fieldnames=unmapped_tools[0].keys())
                    writer.writeheader()
                    writer.writerows(unmapped_tools)
            log(f"⚠ {len(unmapped_tools)} unmapped tools found - saved to: {unmapped_path}", "WARNING")

        # Save duplicate resolution
        if duplicate_report:
            dup_path = self.report_dir / "duplicate_resolution_decisions.json"
            with open(dup_path, 'w', encoding='utf-8') as f:
                json.dump({'duplicates': duplicate_report}, f, indent=2)
            log(f"⚠ {len(duplicate_report)} duplicates found - saved to: {dup_path}", "WARNING")

        return True

    # ================================================================================
    # PHASE 2: MIGRATION EXECUTION
    # ================================================================================

    def phase2_preflight_check(self) -> bool:
        """Phase 2.1: Pre-flight validation"""
        log("=" * 80)
        log("PHASE 2.1: Pre-Flight Validation")
        log("=" * 80)

        checks = {
            "backup_exists": False,
            "no_unmapped": False,
            "no_collisions": False,
            "all_files_readable": False,
            "disk_space_ok": False,
            "no_duplicate_ids": False
        }

        try:
            # Check 1: Backup exists
            backup_dirs = list(self.tools_dir.parent.glob("LBS_003_Tools_BACKUP_*"))
            checks["backup_exists"] = len(backup_dirs) > 0
            log(f"{'✓' if checks['backup_exists'] else '✗'} Backup exists: {len(backup_dirs)} backup(s) found")

            # Check 2: No unmapped entries
            unmapped_count = sum(1 for m in self.mapping_table if m['new_tol_id'] == 'UNMAPPED')
            checks["no_unmapped"] = unmapped_count == 0
            log(f"{'✓' if checks['no_unmapped'] else '✗'} No unmapped entries: {unmapped_count} unmapped")

            # Check 3: No filename collisions
            new_filenames = [m['new_filename'] for m in self.mapping_table if m['action'] == 'MIGRATE']
            collisions = len(new_filenames) - len(set(new_filenames))
            checks["no_collisions"] = collisions == 0
            log(f"{'✓' if checks['no_collisions'] else '✗'} No filename collisions: {collisions} collisions")

            # Check 4: All source files readable
            readable_count = 0
            for tool in self.current_tools:
                try:
                    with open(tool['full_path'], 'r', encoding='utf-8') as f:
                        json.load(f)
                    readable_count += 1
                except:
                    log(f"✗ Cannot read: {tool['current_path']}", "WARNING")
            checks["all_files_readable"] = readable_count == len(self.current_tools)
            log(f"{'✓' if checks['all_files_readable'] else '✗'} All files readable: {readable_count}/{len(self.current_tools)}")

            # Check 5: Disk space
            stat = shutil.disk_usage(self.tools_dir)
            available_mb = stat.free / (1024 * 1024)
            checks["disk_space_ok"] = available_mb > 50
            log(f"{'✓' if checks['disk_space_ok'] else '✗'} Disk space available: {available_mb:.1f} MB")

            # Check 6: No duplicate TOL-### IDs
            migrate_entries = [m for m in self.mapping_table if m['action'] == 'MIGRATE']
            tol_ids = [m['new_tol_id'] for m in migrate_entries]
            duplicate_ids = len(tol_ids) - len(set(tol_ids))
            checks["no_duplicate_ids"] = duplicate_ids == 0
            log(f"{'✓' if checks['no_duplicate_ids'] else '✗'} No duplicate IDs: {duplicate_ids} duplicates")

            all_passed = all(checks.values())

            # Save preflight report
            preflight_report = {
                "timestamp": datetime.now().isoformat(),
                "checks": checks,
                "overall_status": "PASS" if all_passed else "FAIL"
            }

            report_path = self.report_dir / "preflight_validation_report.json"
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(preflight_report, f, indent=2)

            if all_passed:
                log("✓ Phase 2.1 Complete: All pre-flight checks PASSED")
            else:
                log("✗ Phase 2.1 Failed: Some pre-flight checks FAILED - STOPPING", "ERROR")

            return all_passed

        except Exception as e:
            log(f"✗ Pre-flight check error: {str(e)}", "ERROR")
            return False

    def phase2_dry_run(self) -> bool:
        """Phase 2.2: Dry run simulation"""
        log("=" * 80)
        log("PHASE 2.2: Dry Run Simulation")
        log("=" * 80)

        dry_run_log_path = self.log_dir / "dry_run_log.txt"

        summary = {
            "total_files": len(self.mapping_table),
            "to_migrate": 0,
            "to_delete": 0,
            "to_skip": 0,
            "errors": 0,
            "warnings": 0
        }

        try:
            with open(dry_run_log_path, 'w', encoding='utf-8') as dry_log:
                for mapping in self.mapping_table:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    if mapping['action'] == 'MIGRATE':
                        summary["to_migrate"] += 1
                        dry_log.write(f"[{timestamp}] MIGRATE: {mapping['current_path']} → {mapping['new_filename']}\n")
                        dry_log.write(f"              Update tool_id: {mapping['current_tool_id']} → {mapping['new_tol_id']}\n")
                        dry_log.write(f"              Write to: {mapping['new_path']}\n")

                    elif mapping['action'] == 'DELETE':
                        summary["to_delete"] += 1
                        dry_log.write(f"[{timestamp}] DELETE: {mapping['current_path']} (duplicate)\n")

                    elif mapping['action'] == 'SKIP':
                        summary["to_skip"] += 1
                        summary["warnings"] += 1
                        dry_log.write(f"[{timestamp}] SKIP: {mapping['current_path']} (unmapped)\n")

            # Save dry run summary
            summary_path = self.report_dir / "dry_run_summary.json"
            with open(summary_path, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2)

            log(f"✓ Dry run complete:")
            log(f"  - Total files: {summary['total_files']}")
            log(f"  - To migrate: {summary['to_migrate']}")
            log(f"  - To delete: {summary['to_delete']}")
            log(f"  - To skip: {summary['to_skip']}")
            log(f"  - Errors: {summary['errors']}")
            log(f"  - Warnings: {summary['warnings']}")
            log(f"✓ Dry run log saved: {dry_run_log_path}")
            log(f"✓ Dry run summary saved: {summary_path}")

            log("\n" + "=" * 80)
            log("⚠ MANUAL CHECKPOINT: Review dry run results before proceeding!", "WARNING")
            log("=" * 80)

            return True

        except Exception as e:
            log(f"✗ Dry run failed: {str(e)}", "ERROR")
            return False

    def save_checkpoint(self, processed_count: int):
        """Save migration checkpoint for resumability"""
        checkpoint = {
            "timestamp": datetime.now().isoformat(),
            "processed_count": processed_count,
            "total_count": len([m for m in self.mapping_table if m['action'] == 'MIGRATE'])
        }
        with open(self.checkpoint_file, 'w', encoding='utf-8') as f:
            json.dump(checkpoint, f, indent=2)

    def load_checkpoint(self) -> int:
        """Load checkpoint if exists"""
        if self.checkpoint_file.exists():
            with open(self.checkpoint_file, 'r', encoding='utf-8') as f:
                checkpoint = json.load(f)
                return checkpoint.get('processed_count', 0)
        return 0

    def phase2_execute_migration(self, dry_run: bool = False) -> bool:
        """Phase 2.3: Execute actual migration"""
        log("=" * 80)
        log(f"PHASE 2.3: {'DRY RUN - ' if dry_run else ''}Execute Migration")
        log("=" * 80)

        if dry_run:
            log("⚠ DRY RUN MODE - No actual changes will be made", "WARNING")

        processed = self.load_checkpoint()
        if processed > 0:
            log(f"⚠ Resuming from checkpoint: {processed} files already processed", "WARNING")

        migrate_entries = [m for m in self.mapping_table if m['action'] == 'MIGRATE']
        total = len(migrate_entries)

        files_marked_for_deletion_path = self.log_dir / "files_marked_for_deletion.txt"

        try:
            with open(files_marked_for_deletion_path, 'w', encoding='utf-8') as del_file:
                for i, mapping in enumerate(migrate_entries):
                    if i < processed:
                        continue  # Skip already processed

                    try:
                        # Find original tool entry
                        original_tool = next((t for t in self.current_tools if t['current_path'] == mapping['current_path']), None)
                        if not original_tool:
                            log(f"✗ Could not find original tool: {mapping['current_path']}", "ERROR")
                            continue

                        # Read original file
                        with open(original_tool['full_path'], 'r', encoding='utf-8') as f:
                            data = json.load(f)

                        # Update tool_id
                        old_tool_id = data.get('tool_id', '')
                        data['tool_id'] = mapping['new_tol_id']

                        # Add migration metadata
                        data['_migration'] = {
                            'date': datetime.now().isoformat(),
                            'old_tool_id': old_tool_id,
                            'old_path': mapping['current_path'],
                            'migrated_by': 'tool_migration_script_v1'
                        }

                        # New file path
                        new_file_path = self.tools_dir / mapping['new_filename']

                        if not dry_run:
                            # Write new file
                            with open(new_file_path, 'w', encoding='utf-8') as f:
                                json.dump(data, f, indent=2, ensure_ascii=False)

                            # Verify new file
                            with open(new_file_path, 'r', encoding='utf-8') as f:
                                verify_data = json.load(f)
                                assert verify_data['tool_id'] == mapping['new_tol_id'], "ID mismatch after write"

                        # Mark old file for deletion
                        del_file.write(f"{original_tool['full_path']}\n")

                        log(f"✓ [{i+1}/{total}] Migrated: {mapping['current_filename']} → {mapping['new_filename']}")

                        # Save checkpoint every 10 files
                        if (i + 1) % CHECKPOINT_INTERVAL == 0:
                            if not dry_run:
                                self.save_checkpoint(i + 1)
                            log(f"📍 Checkpoint: {i+1}/{total} files processed")

                    except Exception as e:
                        log(f"✗ Failed to migrate {mapping['current_path']}: {str(e)}", "ERROR")

            if not dry_run:
                # Final checkpoint
                self.save_checkpoint(total)

            log(f"✓ Phase 2.3 Complete: {total} files {'would be ' if dry_run else ''}migrated")
            log(f"✓ Files marked for deletion: {files_marked_for_deletion_path}")

            return True

        except Exception as e:
            log(f"✗ Migration execution failed: {str(e)}", "ERROR")
            return False

    def phase2_validate(self) -> bool:
        """Phase 2.4: Post-migration validation"""
        log("=" * 80)
        log("PHASE 2.4: Post-Migration Validation")
        log("=" * 80)

        validation_results = {
            "timestamp": datetime.now().isoformat(),
            "checks": {},
            "file_count": {
                "expected": 0,
                "actual": 0
            },
            "errors": []
        }

        try:
            # Check 1: Count validation
            expected_count = sum(1 for m in self.mapping_table if m['action'] == 'MIGRATE')
            actual_files = list(self.tools_dir.glob("TOL-*.json"))
            actual_count = len(actual_files)

            validation_results["file_count"]["expected"] = expected_count
            validation_results["file_count"]["actual"] = actual_count
            validation_results["checks"]["count_validation"] = "PASS" if expected_count == actual_count else "FAIL"

            log(f"{'✓' if validation_results['checks']['count_validation'] == 'PASS' else '✗'} Count check: Expected {expected_count}, Found {actual_count}")

            # Check 2: ID validation - filename matches internal tool_id
            id_mismatches = []
            for file in actual_files:
                try:
                    with open(file, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    filename_id = file.stem.split('_')[0]  # TOL-002 from TOL-002_Claude.json
                    internal_id = data.get('tool_id', '')

                    if filename_id != internal_id:
                        id_mismatches.append({
                            "file": file.name,
                            "filename_id": filename_id,
                            "internal_id": internal_id
                        })
                except Exception as e:
                    validation_results["errors"].append(f"Failed to validate {file.name}: {str(e)}")

            validation_results["checks"]["id_validation"] = "PASS" if len(id_mismatches) == 0 else "FAIL"
            log(f"{'✓' if validation_results['checks']['id_validation'] == 'PASS' else '✗'} ID validation: {len(id_mismatches)} mismatches")

            if id_mismatches:
                for mismatch in id_mismatches[:5]:  # Show first 5
                    log(f"  ✗ {mismatch['file']}: filename={mismatch['filename_id']}, internal={mismatch['internal_id']}", "ERROR")

            # Check 3: JSON validation
            json_errors = []
            for file in actual_files:
                try:
                    with open(file, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    # Check required fields
                    required_fields = ['tool_id', 'name', 'category']
                    missing = [field for field in required_fields if field not in data]
                    if missing:
                        json_errors.append(f"{file.name}: Missing fields {missing}")

                except json.JSONDecodeError as e:
                    json_errors.append(f"{file.name}: Invalid JSON - {str(e)}")
                except Exception as e:
                    json_errors.append(f"{file.name}: {str(e)}")

            validation_results["checks"]["json_validation"] = "PASS" if len(json_errors) == 0 else "FAIL"
            log(f"{'✓' if validation_results['checks']['json_validation'] == 'PASS' else '✗'} JSON validation: {len(json_errors)} errors")

            # Check 4: Duplicate check
            tol_ids = []
            for file in actual_files:
                try:
                    with open(file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    tol_ids.append(data.get('tool_id', ''))
                except:
                    pass

            duplicates = [tid for tid in tol_ids if tol_ids.count(tid) > 1]
            unique_duplicates = list(set(duplicates))
            validation_results["checks"]["duplicate_check"] = "PASS" if len(unique_duplicates) == 0 else "FAIL"
            log(f"{'✓' if validation_results['checks']['duplicate_check'] == 'PASS' else '✗'} Duplicate check: {len(unique_duplicates)} duplicate IDs")

            # Check 5: Reference check - subdirectories should be empty (except _ARCHIVE)
            remaining_files = []
            for subdir in ['AI_Tools', 'Cloud_Platforms', 'Data_Tools', 'Developer_Tools', 'Databases']:
                subdir_path = self.tools_dir / subdir
                if subdir_path.exists():
                    json_files = list(subdir_path.glob('*.json'))
                    remaining_files.extend(json_files)

            validation_results["checks"]["reference_check"] = "PASS" if len(remaining_files) == 0 else "FAIL"
            log(f"{'✓' if validation_results['checks']['reference_check'] == 'PASS' else '✗'} Reference check: {len(remaining_files)} files remain in subdirectories")

            # Overall status
            all_passed = all(v == "PASS" for v in validation_results["checks"].values())
            validation_results["overall_status"] = "PASS" if all_passed else "FAIL"

            # Save validation report
            report_path = self.report_dir / "post_migration_validation_report.json"
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(validation_results, f, indent=2)

            if all_passed:
                log("✓ Phase 2.4 Complete: All validation checks PASSED")
            else:
                log("✗ Phase 2.4: Some validation checks FAILED - DO NOT PROCEED TO CLEANUP", "ERROR")

            log(f"✓ Validation report saved: {report_path}")

            return all_passed

        except Exception as e:
            log(f"✗ Validation failed: {str(e)}", "ERROR")
            return False

    # ================================================================================
    # PHASE 3: CLEANUP & FINALIZATION
    # ================================================================================

    def phase3_archive_old_files(self) -> bool:
        """Phase 3.1: Archive old files"""
        log("=" * 80)
        log("PHASE 3.1: Archiving Old Files")
        log("=" * 80)

        try:
            timestamp = datetime.now().strftime("%Y-%m-%d")
            archive_dir = self.tools_dir / "_ARCHIVE" / f"pre_migration_{timestamp}"
            archive_dir.mkdir(parents=True, exist_ok=True)

            log(f"Archive directory: {archive_dir}")

            # Read files marked for deletion
            files_to_delete_path = self.log_dir / "files_marked_for_deletion.txt"
            if not files_to_delete_path.exists():
                log("⚠ No files marked for deletion", "WARNING")
                return True

            with open(files_to_delete_path, 'r', encoding='utf-8') as f:
                files_to_archive = [line.strip() for line in f if line.strip()]

            archived_count = 0
            for filepath in files_to_archive:
                if os.path.exists(filepath):
                    rel_path = os.path.relpath(filepath, self.tools_dir)
                    archive_path = archive_dir / rel_path
                    archive_path.parent.mkdir(parents=True, exist_ok=True)

                    shutil.move(filepath, archive_path)
                    archived_count += 1
                    log(f"✓ Archived: {rel_path}")

            log(f"✓ Phase 3.1 Complete: {archived_count} files archived")

            # Remove empty subdirectories
            subdirs_to_check = ['AI_Tools', 'Cloud_Platforms', 'Data_Tools', 'Developer_Tools',
                               'Databases', 'Authentication_Tools', 'Integration_Tools']

            for subdir in subdirs_to_check:
                subdir_path = self.tools_dir / subdir
                if subdir_path.exists() and not any(subdir_path.iterdir()):
                    subdir_path.rmdir()
                    log(f"✓ Removed empty directory: {subdir}")

            return True

        except Exception as e:
            log(f"✗ Archive failed: {str(e)}", "ERROR")
            return False

    def run_full_migration(self, dry_run: bool = False):
        """Run complete migration process"""
        log("\n")
        log("=" * 80)
        log("TOOL ID MIGRATION: TOOL-[CAT]-### → TOL-###")
        log("=" * 80)
        log(f"Mode: {'DRY RUN' if dry_run else 'ACTUAL EXECUTION'}")
        log(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        log("=" * 80)

        # Phase 1: Preparation
        if not self.phase1_backup():
            return False

        if not self.phase1_load_taxonomy():
            return False

        if not self.phase1_inventory():
            return False

        if not self.phase1_create_mapping():
            return False

        # Phase 2: Execution
        if not self.phase2_preflight_check():
            return False

        if not self.phase2_dry_run():
            return False

        if not dry_run:
            log("\n" + "=" * 80)
            log("⚠ MANUAL CHECKPOINT: Review reports and approve execution", "WARNING")
            log("=" * 80)
            response = input("\nProceed with actual migration? (yes/no): ").strip().lower()
            if response != 'yes':
                log("Migration cancelled by user")
                return False

        if not self.phase2_execute_migration(dry_run=dry_run):
            return False

        if not dry_run:
            if not self.phase2_validate():
                log("✗ Validation failed - NOT proceeding to cleanup", "ERROR")
                return False

            # Phase 3: Cleanup
            if not self.phase3_archive_old_files():
                return False

        log("\n" + "=" * 80)
        log("✓ MIGRATION COMPLETE")
        log("=" * 80)
        log(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        log(f"Logs: {LOG_DIR}")
        log(f"Reports: {REPORT_DIR}")

        return True


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description='Migrate tool files to TOL-### format')
    parser.add_argument('--dry-run', action='store_true', help='Run in dry-run mode (no actual changes)')
    parser.add_argument('--skip-backup', action='store_true', help='Skip backup creation (not recommended)')

    args = parser.parse_args()

    if args.dry_run:
        print("\n⚠ Running in DRY RUN mode - no actual changes will be made\n")

    migration = ToolMigration()
    success = migration.run_full_migration(dry_run=args.dry_run)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()