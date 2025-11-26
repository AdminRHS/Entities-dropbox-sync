"""
Script: script_copy_dailies

Purpose:
    Find all folders named "17" and "18" within department employee folders under Nov25/,
    and copy them to ENTITIES/DAILIES/ with expanded folder names that include employee
    identification codes (employee_id).

Author: Generated from plan specification
Date: 2025-11-25
"""

import os
import json
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')


def load_employee_mapping(employees_json_path: str) -> Dict[str, Dict[str, str]]:
    """
    Load employee data from JSON and create a mapping dictionary.
    
    Args:
        employees_json_path: Path to Employees.json file
        
    Returns:
        Dictionary mapping employee names to {employee_id, short_name}
        Format: {name: {employee_id: str, short_name: str}}
    """
    mapping = {}
    
    try:
        with open(employees_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        employees = data.get('data', {}).get('employees', [])
        
        for emp in employees:
            employee_id = emp.get('employee_id', '')
            short_name = emp.get('short_name', '')
            name_eng = emp.get('name_eng', '')
            name_ua = emp.get('name_ua', '')
            
            # Create mappings for both English and Ukrainian names
            if name_eng:
                mapping[name_eng] = {
                    'employee_id': employee_id,
                    'short_name': short_name
                }
            if name_ua:
                mapping[name_ua] = {
                    'employee_id': employee_id,
                    'short_name': short_name
                }
            
            # Also try reversed format (Last First) for name_eng
            if name_eng and ' ' in name_eng:
                parts = name_eng.split(' ', 1)
                if len(parts) == 2:
                    reversed_name = f"{parts[1]} {parts[0]}"
                    mapping[reversed_name] = {
                        'employee_id': employee_id,
                        'short_name': short_name
                    }
        
        print(f"Loaded {len(employees)} employees into mapping")
        return mapping
        
    except FileNotFoundError:
        print(f"ERROR: Employees.json not found at {employees_json_path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in {employees_json_path}: {e}")
        return {}
    except Exception as e:
        print(f"ERROR: Failed to load employee data: {e}")
        return {}


def find_daily_folders(nov25_path: str, target_days: List[str]) -> List[Dict]:
    """
    Recursively scan Nov25 directory for folders named "17" or "18".
    
    Args:
        nov25_path: Path to Nov25 directory
        target_days: List of day numbers to find (e.g., ["17", "18"])
        
    Returns:
        List of dictionaries with folder information:
        {
            'path': full_path,
            'day': day_number,
            'employee_name': extracted_name,
            'department': department_name,
            'has_week': boolean
        }
    """
    found_folders = []
    nov25 = Path(nov25_path)
    
    if not nov25.exists():
        print(f"ERROR: Nov25 directory not found at {nov25_path}")
        return found_folders
    
    # Scan all department directories
    for dept_dir in nov25.iterdir():
        if not dept_dir.is_dir() or dept_dir.name == 'git' or dept_dir.name == 'nul':
            continue
        
        # Skip if it's not a department folder (check for "Nov25" in name pattern)
        if 'Nov25' not in dept_dir.name:
            continue
        
        dept_name = dept_dir.name.replace(' Nov25', '').replace('Nov25', '')
        
        # Scan employee folders within department
        for emp_dir in dept_dir.iterdir():
            if not emp_dir.is_dir():
                continue
            
            # Skip non-employee folders (like Reports, Overview, etc.)
            skip_folders = ['Reports', 'Overview', 'DEP_README.md', 'desktop.ini', 
                          'Projects', 'Tasks', 'Microservices', 'Calls', 'CVs',
                          'HR Instructions', 'prompts', 'Recruiting China',
                          'RemotEmployees AI Recruiter', 'Instagram_Ads', 'Interviews',
                          'Public', 'git', 'nul', 'Archive', 'Creatives', 'Dailies',
                          'Employees', 'ExportCRMS', 'Tasks', 'LIBRARIES', 'TASK_MANAGERS']
            
            if emp_dir.name in skip_folders or any(skip in emp_dir.name for skip in ['README', 'GUIDE', 'PROMPT', '.md']):
                continue
            
            employee_name = emp_dir.name
            
            # Check for direct day folders (e.g., Nov25/AI Nov25/Employee/17/)
            for day in target_days:
                day_folder = emp_dir / day
                if day_folder.exists() and day_folder.is_dir():
                    found_folders.append({
                        'path': str(day_folder),
                        'day': day,
                        'employee_name': employee_name,
                        'department': dept_name,
                        'has_week': False,
                        'week_folder': None
                    })
            
            # Check for Week_X/day folders (e.g., Nov25/HR Nov25/Employee/Week_3/17/)
            for week_dir in emp_dir.iterdir():
                if week_dir.is_dir() and week_dir.name.startswith('Week_'):
                    for day in target_days:
                        day_folder = week_dir / day
                        if day_folder.exists() and day_folder.is_dir():
                            found_folders.append({
                                'path': str(day_folder),
                                'day': day,
                                'employee_name': employee_name,
                                'department': dept_name,
                                'has_week': True,
                                'week_folder': week_dir.name
                            })
    
    return found_folders


def copy_files_with_employee_id(
    source_path: str,
    target_base: str,
    day: str,
    employee_id: str,
    employee_name: str,
    department: str,
    has_week: bool,
    week_folder: Optional[str]
) -> Tuple[int, int]:
    """
    Copy files from source folder to DAILIES/{day}/ with renamed files.
    Files are renamed: {original_name}_{employee_id}_{employee_name}.{ext}
    
    Args:
        source_path: Source folder path
        target_base: Base target directory (ENTITIES/DAILIES/)
        day: Day number (17 or 18)
        employee_id: Employee ID (e.g., "37226")
        employee_name: Employee name for file naming
        department: Department name
        has_week: Whether source is in Week_X folder
        week_folder: Week folder name if applicable
        
    Returns:
        Tuple of (files_copied: int, errors: int)
    """
    source_dir = Path(source_path)
    day_folder = Path(target_base) / day
    day_folder.mkdir(parents=True, exist_ok=True)
    
    files_copied = 0
    errors = 0
    
    # Clean employee name for filename (remove special chars, replace spaces)
    clean_name = employee_name.replace(' ', '_').replace('/', '_').replace('\\', '_')
    clean_name = ''.join(c for c in clean_name if c.isalnum() or c in ('_', '-'))
    
    if not source_dir.exists() or not source_dir.is_dir():
        return 0, 0
    
    # Get all files (not directories) from source folder
    files = [f for f in source_dir.iterdir() if f.is_file()]
    
    if not files:
        # Skip empty folders
        return 0, 0
    
    for source_file in files:
        try:
            # Get file extension
            file_stem = source_file.stem
            file_suffix = source_file.suffix
            
            # Create new filename: {original_name}_{employee_id}_{employee_name}.{ext}
            new_filename = f"{file_stem}_{employee_id}_{clean_name}{file_suffix}"
            target_file = day_folder / new_filename
            
            # Handle duplicates: append counter if file exists
            counter = 1
            original_target = target_file
            while target_file.exists():
                new_filename = f"{file_stem}_{employee_id}_{clean_name}_{counter}{file_suffix}"
                target_file = day_folder / new_filename
                counter += 1
            
            # Copy file
            shutil.copy2(source_file, target_file)
            files_copied += 1
            
        except Exception as e:
            print(f"  ERROR copying file {source_file.name}: {e}")
            errors += 1
    
    return files_copied, errors


def main():
    """Main execution function."""
    # Define paths
    workspace_root = Path(__file__).parent.parent.parent.parent  # Go up from ENTITIES/PROMPTS/Automation/
    nov25_path = workspace_root / "Nov25"
    employees_json_path = nov25_path / "Niko Nov25" / "ExportCRMS" / "Employees.json"
    dailies_path = workspace_root / "ENTITIES" / "DAILIES"
    
    # Target days to find
    target_days = ["17", "18"]
    
    print("=" * 60)
    print("Script: script_copy_dailies")
    print("=" * 60)
    print(f"Workspace root: {workspace_root}")
    print(f"Nov25 path: {nov25_path}")
    print(f"Employees JSON: {employees_json_path}")
    print(f"DAILIES target: {dailies_path}")
    print()
    
    # Step 1: Create DAILIES folder
    print("Step 1: Creating DAILIES directory...")
    dailies_path.mkdir(parents=True, exist_ok=True)
    print(f"[OK] DAILIES directory ready: {dailies_path}")
    print()
    
    # Step 2: Load employee mapping
    print("Step 2: Loading employee data...")
    employee_mapping = load_employee_mapping(str(employees_json_path))
    if not employee_mapping:
        print("ERROR: No employee mapping loaded. Exiting.")
        return
    print()
    
    # Step 3: Find all 17 and 18 folders
    print("Step 3: Scanning for folders 17 and 18...")
    found_folders = find_daily_folders(str(nov25_path), target_days)
    print(f"Found {len(found_folders)} folders to process")
    print()
    
    # Step 4: Copy files with employee IDs
    print("Step 4: Copying files...")
    copied_files = []
    missing_employees = []
    total_files_copied = 0
    total_errors = 0
    
    for folder_info in found_folders:
        employee_name = folder_info['employee_name']
        day = folder_info['day']
        source_path = folder_info['path']
        department = folder_info['department']
        has_week = folder_info['has_week']
        week_folder = folder_info.get('week_folder')
        
        # Look up employee_id
        emp_data = employee_mapping.get(employee_name)
        
        if not emp_data or not emp_data.get('employee_id'):
            missing_employees.append({
                'employee_name': employee_name,
                'source_path': source_path,
                'day': day,
                'department': department
            })
            print(f"[SKIP] Employee '{employee_name}' not found in mapping")
            print(f"  Path: {source_path}")
            continue
        
        employee_id = emp_data['employee_id']
        
        # Copy files
        files_copied, errors = copy_files_with_employee_id(
            source_path=source_path,
            target_base=str(dailies_path),
            day=day,
            employee_id=employee_id,
            employee_name=employee_name,
            department=department,
            has_week=has_week,
            week_folder=week_folder
        )
        
        if files_copied > 0:
            copied_files.append({
                'source_path': source_path,
                'employee_name': employee_name,
                'employee_id': employee_id,
                'day': day,
                'department': department,
                'files_copied': files_copied
            })
            print(f"[OK] COPIED {files_copied} file(s): {employee_name} ({employee_id}) - {day}")
            print(f"  From: {source_path}")
            total_files_copied += files_copied
        
        if errors > 0:
            total_errors += errors
            print(f"[ERROR] {errors} error(s) copying files from {employee_name} ({employee_id}) - {day}")
    
    print()
    
    # Step 5: Create summary log
    print("Step 5: Creating summary log...")
    log_data = {
        'summary': {
            'total_folders_found': len(found_folders),
            'total_files_copied': total_files_copied,
            'total_folders_processed': len(copied_files),
            'total_missing': len(missing_employees),
            'total_errors': total_errors
        },
        'copied_files': copied_files,
        'missing_employees': missing_employees
    }
    
    log_path = dailies_path / "copy_log.json"
    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(log_data, f, indent=2, ensure_ascii=False)
    
    print(f"[OK] Log file created: {log_path}")
    print()
    
    # Final summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total folders found: {len(found_folders)}")
    print(f"Folders processed: {len(copied_files)}")
    print(f"Total files copied: {total_files_copied}")
    print(f"Missing employees (skipped): {len(missing_employees)}")
    print(f"File copy errors: {total_errors}")
    print()
    
    if missing_employees:
        print("Missing employees (not copied):")
        for emp in missing_employees:
            print(f"  - {emp['employee_name']} ({emp['department']}) - {emp['day']}")
            print(f"    Path: {emp['source_path']}")
        print()
    
    print("=" * 60)
    print("Script completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

