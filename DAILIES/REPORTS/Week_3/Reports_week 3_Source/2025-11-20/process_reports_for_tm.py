"""
Process Department Reports for TASK_MANAGERS Import

This script creates processed variations of department reports that match
the TASK_MANAGERS architecture naming conventions for data import.

Department Mapping:
- AI → AID (AI Department)
- Design → DGN (Design & Creative)
- Dev → DEV (Development & Engineering)
- Finance → FIN (Finance)
- HR → HRM (Human Resource Management)
- LG → LGN (Lead Generation & Marketing)
- Sales → SLS (Sales & Client Relations)
- Video → VID (Video Production)
"""

import os
import re
from pathlib import Path
from datetime import datetime

# Department name to code mapping
DEPT_MAPPING = {
    "AI": "AID",
    "Design": "DGN",
    "Dev": "DEV",
    "Development": "DEV",
    "Finance": "FIN",
    "HR": "HRM",
    "LG": "LGN",
    "Lead Generation": "LGN",
    "Sales": "SLS",
    "Video": "VID"
}

# Full department name mappings for content replacement
FULL_NAME_MAPPING = {
    "AI Department": "AI Department (AID)",
    "Design Department": "Design Department (DGN)",
    "Development Department": "Development Department (DEV)",
    "Finance Department": "Finance Department (FIN)",
    "HR Department": "HR Department (HRM)",
    "Lead Generation Department": "Lead Generation Department (LGN)",
    "Sales Department": "Sales Department (SLS)",
    "Video Department": "Video Department (VID)",
    "AI & Automation": "AI & Automation (AID)",
    "HR & Recruitment": "HR & Recruitment (HRM)",
    "Design (DGN)": "Design Department (DGN)",
    "AI (AID)": "AI Department (AID)",
    "HR (HRM)": "HR Department (HRM)",
    "Development (DEV)": "Development Department (DEV)",
    "Finance (FIN)": "Finance Department (FIN)",
    "Lead Generation (LGN)": "Lead Generation Department (LGN)",
    "Sales (SLS)": "Sales Department (SLS)",
    "Video (VID)": "Video Department (VID)",
}

def extract_dept_code_from_filename(filename):
    """Extract department code from filename."""
    for dept_name, dept_code in DEPT_MAPPING.items():
        if dept_name in filename:
            return dept_code
    return None

def extract_date_from_filename(filename):
    """Extract date from filename in YYYY-MM-DD format."""
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
    if date_match:
        return date_match.group(1)
    return None

def get_day_of_week(date_str):
    """
    Get day of week from date string.
    
    Args:
        date_str: Date string in YYYY-MM-DD format
        
    Returns:
        dict with day_name (full), day_name_short (3-letter), day_number (0-6, Monday=0)
    """
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        day_number = date_obj.weekday()  # Monday = 0, Sunday = 6
        day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_names_short = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        
        return {
            'day_name': day_names[day_number],
            'day_name_short': day_names_short[day_number],
            'day_number': day_number,
            'is_weekend': day_number >= 5,  # Saturday or Sunday
            'is_weekday': day_number < 5
        }
    except (ValueError, AttributeError):
        return None

def process_report_content(content, dept_code, day_of_week_info):
    """
    Process report content to use department codes consistently and inject day of week.
    
    Since the original files already contain department codes, we primarily
    ensure consistency and fix any issues introduced by previous processing.
    Also adds day of week metadata for pattern analysis.
    """
    processed_content = content
    
    # Inject day of week information into metadata section
    if day_of_week_info:
        # Add day of week to EXECUTIVE SUMMARY section
        exec_summary_pattern = r'(## 1\. EXECUTIVE SUMMARY\s*\n)'
        day_info_insert = f"## 1. EXECUTIVE SUMMARY\n\n- **Day of Week:** {day_of_week_info['day_name']} ({day_of_week_info['day_name_short']})\n- **Weekday/Weekend:** {'Weekend' if day_of_week_info['is_weekend'] else 'Weekday'}\n"
        
        # Check if day of week already exists
        if 'Day of Week:' not in processed_content:
            processed_content = re.sub(
                exec_summary_pattern,
                day_info_insert,
                processed_content,
                count=1
            )
        
        # Also add to Report Date line if it exists
        report_date_pattern = r'(- \*\*Report Date:\*\* \d{4}-\d{2}-\d{2})'
        if day_of_week_info and re.search(report_date_pattern, processed_content):
            def add_day_to_date(match):
                return f"{match.group(1)} ({day_of_week_info['day_name_short']})"
            processed_content = re.sub(report_date_pattern, add_day_to_date, processed_content, count=1)
    
    # Fix malformed patterns where code was incorrectly inserted into words
    # Pattern: "A (AID)I" -> "AI (AID)", "D (DGN)esign" -> "Design (DGN)"
    # Match: word boundary, letter, space, code in parens, letter, word boundary
    malformed_patterns = [
        (rf'(\b\w)\s*\({dept_code}\)(\w\b)', rf'\1\2 ({dept_code})'),  # "A (AID)I" -> "AI (AID)"
    ]
    
    for pattern, replacement in malformed_patterns:
        processed_content = re.sub(pattern, replacement, processed_content)
    
    # Remove duplicate codes in parentheses
    duplicate_pattern = rf'\({dept_code}\)\s*\({dept_code}\)'
    processed_content = re.sub(duplicate_pattern, f'({dept_code})', processed_content)
    
    # Ensure header has correct format (but don't break if already correct)
    # Only fix if we see malformed patterns
    header_pattern = r'# Daily Activity Report - (.+?)(\s*\([A-Z]{3}\))?$'
    def fix_header(match):
        dept_part = match.group(1).strip()
        existing_code = match.group(2).strip() if match.group(2) else ""
        
        # If code is already correctly placed, keep it
        if existing_code == f'({dept_code})':
            return f'# Daily Activity Report - {dept_part} ({dept_code})'
        # If malformed (code in middle of word), fix it
        elif re.search(rf'\w\s*\({dept_code}\)\w', dept_part):
            # Extract department name properly
            dept_name = re.sub(rf'\s*\({dept_code}\)', '', dept_part)
            dept_name = re.sub(rf'(\w)\s*\({dept_code}\)(\w)', r'\1\2', dept_name)
            return f'# Daily Activity Report - {dept_name} ({dept_code})'
        # Otherwise, ensure code is at the end
        else:
            dept_name = dept_part.replace(f'({dept_code})', '').strip()
            return f'# Daily Activity Report - {dept_name} ({dept_code})'
    
    processed_content = re.sub(header_pattern, fix_header, processed_content, flags=re.MULTILINE)
    
    # Fix department line similarly
    dept_line_pattern = r'- \*\*Department:\*\* (.+?)(\s*\([A-Z]{3}\))?$'
    def fix_dept_line(match):
        dept_part = match.group(1).strip()
        existing_code = match.group(2).strip() if match.group(2) else ""
        
        if existing_code == f'({dept_code})':
            return f'- **Department:** {dept_part} ({dept_code})'
        elif re.search(rf'\w\s*\({dept_code}\)\w', dept_part):
            dept_name = re.sub(rf'\s*\({dept_code}\)', '', dept_part)
            dept_name = re.sub(rf'(\w)\s*\({dept_code}\)(\w)', r'\1\2', dept_name)
            return f'- **Department:** {dept_name} ({dept_code})'
        else:
            dept_name = dept_part.replace(f'({dept_code})', '').strip()
            return f'- **Department:** {dept_name} ({dept_code})'
    
    processed_content = re.sub(dept_line_pattern, fix_dept_line, processed_content, flags=re.MULTILINE)
    
    return processed_content

def process_reports():
    """Process all department reports and create TM-compatible versions."""
    # Paths
    source_dir = Path(__file__).parent / "Departments"
    processed_dir = Path(__file__).parent / "Departments_Processed_TM"
    
    # Create processed directory
    processed_dir.mkdir(exist_ok=True)
    
    # Process each report file
    processed_files = []
    
    for report_file in source_dir.glob("*_Department_Report_*.md"):
        # Extract department code
        dept_code = extract_dept_code_from_filename(report_file.name)
        
        if not dept_code:
            print(f"Warning: Could not determine department code for {report_file.name}")
            continue
        
        # Extract date and calculate day of week
        date_str = extract_date_from_filename(report_file.name) or "2025-11-20"
        day_of_week_info = get_day_of_week(date_str)
        
        # Read original content
        with open(report_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Process content with day of week injection
        processed_content = process_report_content(content, dept_code, day_of_week_info)
        
        # Create new filename with department code
        # Pattern: [DEPT_CODE]_Department_Report_YYYY-MM-DD.md
        new_filename = f"{dept_code}_Department_Report_{date_str}.md"
        new_filepath = processed_dir / new_filename
        
        # Write processed file
        with open(new_filepath, 'w', encoding='utf-8') as f:
            f.write(processed_content)
        
        # Store metadata including day of week
        file_metadata = {
            'original': report_file.name,
            'processed': new_filename,
            'dept_code': dept_code,
            'date': date_str,
            'day_of_week': day_of_week_info
        }
        processed_files.append(file_metadata)
        
        day_info_str = f" ({day_of_week_info['day_name_short']})" if day_of_week_info else ""
        print(f"Processed: {report_file.name} -> {new_filename}{day_info_str}")
    
    # Create mapping file with day of week data
    mapping_file = processed_dir / "Department_Report_Mapping.json"
    import json
    
    # Calculate day of week statistics
    day_stats = {}
    for file_info in processed_files:
        if file_info.get('day_of_week'):
            day_name = file_info['day_of_week']['day_name']
            if day_name not in day_stats:
                day_stats[day_name] = {'count': 0, 'departments': set()}
            day_stats[day_name]['count'] += 1
            day_stats[day_name]['departments'].add(file_info['dept_code'])
    
    # Convert sets to lists for JSON serialization
    for day_name in day_stats:
        day_stats[day_name]['departments'] = list(day_stats[day_name]['departments'])
    
    with open(mapping_file, 'w', encoding='utf-8') as f:
        json.dump({
            'metadata': {
                'purpose': 'Mapping between original report filenames and TM-compatible processed versions',
                'generated': '2025-11-20',
                'naming_convention': '[DEPT_CODE]_Department_Report_YYYY-MM-DD.md',
                'includes_day_of_week': True
            },
            'department_codes': DEPT_MAPPING,
            'day_of_week_statistics': day_stats,
            'processed_files': processed_files
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\nProcessed {len(processed_files)} reports")
    print(f"Created mapping file: {mapping_file.name}")
    print(f"Processed files location: {processed_dir}")
    
    return processed_files

if __name__ == "__main__":
    process_reports()

