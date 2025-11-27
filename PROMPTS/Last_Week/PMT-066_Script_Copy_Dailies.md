# Prompt: Create script_copy_dailies Script

## Purpose
This document serves as a prompt/specification for creating a Python script named `script_copy_dailies` that will find all folders named "17" and "18" within department employee folders under `Nov25/`, and copy them to `ENTITIES/DAILIES/` with expanded folder names that include employee identification codes (employee_id).

## Structure Analysis
- **Source locations**: `Nov25/{Department} Nov25/{Employee Name}/{17|18}/` or `Nov25/{Department} Nov25/{Employee Name}/Week_X/{17|18}/`
- **Target location**: `ENTITIES/DAILIES/`
- **Employee data source**: `Nov25/Niko Nov25/ExportCRMS/Employees.json` contains `employee_id` (e.g., "EMP002") and `short_name` (e.g., "Niko K")

## Script Requirements

### 1. Create DAILIES folder structure
- Create `ENTITIES/DAILIES/` directory if it doesn't exist

### 2. Load employee mapping data
- Read `Nov25/Niko Nov25/ExportCRMS/Employees.json` (contains employee_id and short_name fields)
- Create mapping dictionary: `{employee_name: {employee_id, short_name}}`
- Handle name matching (match folder names like "Artemchuk Nikolay" to employee records using name_eng or name_ua fields)

### 3. Scan and identify folders
- Recursively scan all `Nov25/{Department} Nov25/` directories
- Find all folders named exactly "17" or "18"
- Record full path, employee name, department, and whether it's inside a Week_X folder

### 4. Copy folders with expanded names
- For each found folder:
  - Extract employee name from path
  - Look up employee_id from mapping
  - Generate new folder name: `{day}_{employee_id}` (e.g., `17_EMP002`)
  - Copy entire folder contents to `ENTITIES/DAILIES/{new_folder_name}/`
  - Preserve all files and subdirectories within the copied folder

### 5. Handle edge cases
- If employee not found in mapping, log notification/warning and skip that folder (do not copy)
- Handle duplicate folder names (if same employee has both Week_X/17 and direct 17 folder) - append department or path identifier if needed
- Preserve Week_X structure if present in source

### 6. Create summary report
- Generate a log file listing all copied folders
- Include: source path, target path, employee identification used (employee_id)
- Include notifications for employees not found in mapping (list their folder paths)

## Output Files
- **New**: `ENTITIES/DAILIES/` directory structure (created by script)
- **New**: `ENTITIES/DAILIES/copy_log.json` (summary of copied folders and notifications for missing employees)

## Technical Approach
- Use Python with `os`, `shutil`, and `json` modules
- Recursive directory scanning
- Safe file copying with error handling
- Name matching logic for employee identification

## Implementation Notes
- The script should handle both direct day folders (`Nov25/Dept/Employee/17/`) and Week_X folders (`Nov25/Dept/Employee/Week_X/17/`)
- Employee name matching should handle variations (name_eng, name_ua, and reversed formats)
- Duplicate folder names should be handled by appending department or week information
- Missing employees should be logged but not cause script failure

## Expected Output Format
The script should generate folder names in the format: `{day}_{employee_id}` (e.g., `17_EMP002`, `18_EMP123`)

## Status
✅ **Implemented**: Script created at `ENTITIES/Scripts/script_copy_dailies.py`

