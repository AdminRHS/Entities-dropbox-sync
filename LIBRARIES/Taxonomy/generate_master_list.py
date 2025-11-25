"""
Generate comprehensive LIBRARIES Master List
Scans all LIBRARIES directories and generates a complete CSV master list
"""

import json
import csv
import os
from pathlib import Path
from datetime import datetime

def scan_tools(base_path):
    """Scan all tool files and extract tool information"""
    tools = []
    tools_dir = base_path / "Tools"
    
    if not tools_dir.exists():
        return tools
    
    # Scan AI Tools
    ai_tools_dir = tools_dir / "AI_Tools"
    if ai_tools_dir.exists():
        for tool_file in ai_tools_dir.glob("*.json"):
            if tool_file.name == "AI_Tools_Master_Listing.json":
                continue
            try:
                with open(tool_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    tool_id = data.get('tool_id', f'TOOL-AI-{len(tools)+1:03d}')
                    tool_name = data.get('tool_name') or data.get('name', tool_file.stem)
                    tools.append({
                        'Entity_ID': tool_id,
                        'Entity_Name': tool_name,
                        'Entity_Type': 'Tools',
                        'Department': 'AI',
                        'Category': 'AI Platform',
                        'File_Path': f'LIBRARIES/LBS_003_LBS_003_Tools/By_Category/AI/{tool_file.name}',
                        'Count': 1,
                        'Status': 'Active',
                        'ISO_Code': tool_id,
                        'Notes': f'AI Tool: {tool_name}'
                    })
            except Exception as e:
                print(f"Error reading {tool_file}: {e}")
    
    # Scan other tool categories
    # Map categories to department ISO codes (not category codes)
    category_to_dept_code = {
        'Development_Tools': 'DEV',
        'Video_Editing_Tools': 'VID',
        'Social_Media_Platforms': 'SMM',
        'Automation_Tools': 'AIA',
        'Business_Tools': 'SLS',
        'Cloud_Platforms': 'DEV',  # Operations -> DEV for cloud
        'Databases': 'DEV',
        'Data_Tools': 'DEV',
        'Integration_Tools': 'DEV',
        'Authentication_Tools': 'DEV',
        'Security_Tools': 'DEV',
        'Payment_Tools': 'SLS',
        'File_Management': 'DEV',
        'Web_Tools': 'DEV',
        'MCP_Services': 'AIA',
        'Methodologies': None  # Multi-Department, no dept code
    }
    
    dept_map = {
        'Development_Tools': 'Development',
        'Video_Editing_Tools': 'Video Production',
        'Social_Media_Platforms': 'Marketing',
        'Automation_Tools': 'Operations',
        'Business_Tools': 'Operations',
        'Cloud_Platforms': 'Operations',
        'Databases': 'Development',
        'Data_Tools': 'Development',
        'Integration_Tools': 'Development',
        'Authentication_Tools': 'Development',
        'Security_Tools': 'Operations',
        'Payment_Tools': 'Operations',
        'File_Management': 'Operations',
        'Web_Tools': 'Development',
        'MCP_Services': 'AI',
        'Methodologies': 'Multi-Department'
    }
    
    tool_counter = {}  # Track sequential numbers per department
    
    for category_dir in tools_dir.iterdir():
        if category_dir.is_dir() and category_dir.name != "AI_Tools":
            dept_code = category_to_dept_code.get(category_dir.name)
            department = dept_map.get(category_dir.name, 'Multi-Department')
            
            for tool_file in category_dir.glob("*.json"):
                try:
                    with open(tool_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        # Use existing tool_id if present, but remove category codes
                        existing_id = data.get('tool_id', '')
                        if existing_id:
                            # Remove category codes from ID (AUTH, AUTO, BUS, CLOUD, DB, DATA, etc.)
                            # Keep only department codes (AI, DEV, VID, SMM, SLS, etc.)
                            import re
                            # Pattern: TOOL-CATEGORY-XXX -> TOOL-DEPT-XXX or TOOL-XXX
                            # Category codes to remove: AUTH, AUTO, BUS, CLOUD, DB, DATA, DESIGN, etc.
                            category_codes = ['AUTH', 'AUTO', 'BUS', 'CLOUD', 'DB', 'DATA', 'DESIGN', 'INT', 'SEC', 'PAY', 'FIL', 'WEB', 'MCP', 'MET']
                            
                            # Check if ID contains a category code
                            id_parts = existing_id.split('-')
                            if len(id_parts) >= 3:
                                potential_category = id_parts[1]
                                if potential_category in category_codes:
                                    # Remove category code, use department code instead
                                    if dept_code:
                                        # Extract number from original ID
                                        number = id_parts[-1] if id_parts[-1].isdigit() else f'{tool_counter.get(dept_code, 0)+1:03d}'
                                        tool_id = f'TOOL-{dept_code}-{number}'
                                    else:
                                        # No dept code, use sequential
                                        if 'MULTI' not in tool_counter:
                                            tool_counter['MULTI'] = 0
                                        tool_counter['MULTI'] += 1
                                        tool_id = f'TOOL-{tool_counter["MULTI"]:03d}'
                                else:
                                    # ID already uses department code or is correct format
                                    tool_id = existing_id
                            else:
                                # ID format is already simple (TOOL-XXX or TOOL-DEPT-XXX)
                                tool_id = existing_id
                        else:
                            # Generate ID without category code - use department code or sequential
                            if dept_code:
                                if dept_code not in tool_counter:
                                    tool_counter[dept_code] = 0
                                tool_counter[dept_code] += 1
                                tool_id = f'TOOL-{dept_code}-{tool_counter[dept_code]:03d}'
                            else:
                                # Multi-Department - use sequential
                                if 'MULTI' not in tool_counter:
                                    tool_counter['MULTI'] = 0
                                tool_counter['MULTI'] += 1
                                tool_id = f'TOOL-{tool_counter["MULTI"]:03d}'
                        
                        tool_name = data.get('tool_name') or data.get('name', tool_file.stem)
                        tools.append({
                            'Entity_ID': tool_id,
                            'Entity_Name': tool_name,
                            'Entity_Type': 'Tools',
                            'Department': department,
                            'Category': category_dir.name.replace('_', ' '),
                            'File_Path': f'LIBRARIES/LBS_003_LBS_003_Tools/{category_dir.name}/{tool_file.name}',
                            'Count': 1,
                            'Status': 'Active',
                            'ISO_Code': tool_id,
                            'Notes': f'Tool: {tool_name}'
                        })
                except Exception as e:
                    print(f"Error reading {tool_file}: {e}")
    
    # Scan root level tool files
    root_tool_counter = len(tools) + 1
    for tool_file in tools_dir.glob("*.json"):
        try:
            with open(tool_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                existing_id = data.get('tool_id', '')
                if existing_id:
                    tool_id = existing_id
                else:
                    tool_id = f'TOOL-{root_tool_counter:03d}'
                    root_tool_counter += 1
                tool_name = data.get('tool_name') or data.get('name', tool_file.stem)
                tools.append({
                    'Entity_ID': tool_id,
                    'Entity_Name': tool_name,
                    'Entity_Type': 'Tools',
                    'Department': 'Multi-Department',
                    'Category': 'Platform',
                    'File_Path': f'LIBRARIES/LBS_003_LBS_003_Tools/{tool_file.name}',
                    'Count': 1,
                    'Status': 'Active',
                    'ISO_Code': tool_id,
                    'Notes': f'Tool: {tool_name}'
                })
        except Exception as e:
            print(f"Error reading {tool_file}: {e}")
    
    return tools

def scan_skills(base_path):
    """Scan skills files"""
    skills = []
    skills_dir = base_path / "Skills" / "Master"
    
    if skills_dir.exists():
        skills_file = skills_dir / "all_skills.json"
        if skills_file.exists():
            try:
                with open(skills_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for skill in data:
                        skills.append({
                            'Entity_ID': skill.get('skill_id', 'SKL-000'),
                            'Entity_Name': skill.get('skill_phrase', ''),
                            'Entity_Type': 'Skills',
                            'Department': skill.get('department', 'Multi-Department'),
                            'Category': 'Skill',
                            'File_Path': f'LIBRARIES/LBS_004_LBS_004_../TALENTS/Skills/Master/all_skills.json',
                            'Count': 1,
                            'Status': 'Active',
                            'ISO_Code': skill.get('skill_id', 'SKL-000'),
                            'Notes': f"Skill: {skill.get('skill_phrase', '')}"
                        })
            except Exception as e:
                print(f"Error reading skills file: {e}")
    
    return skills

def scan_professions(base_path):
    """Scan profession files"""
    professions = []
    professions_dir = base_path / "Professions"
    
    if professions_dir.exists():
        for prof_file in professions_dir.glob("*.json"):
            if prof_file.name == "professions.json":
                continue
            try:
                with open(prof_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    prof_name = data.get('profession_name', prof_file.stem)
                    dept = data.get('department', 'Multi-Department')
                    professions.append({
                        'Entity_ID': f'PRF-{len(professions)+1:03d}',
                        'Entity_Name': prof_name.title(),
                        'Entity_Type': 'Professions',
                        'Department': dept.title() if isinstance(dept, str) else 'Multi-Department',
                        'Category': 'Role',
                        'File_Path': f'LIBRARIES/LBS_005_LBS_005_Professions/{prof_file.name}',
                        'Count': 1,
                        'Status': 'Active',
                        'ISO_Code': f'PRF-{len(professions)+1:03d}',
                        'Notes': f'Profession: {prof_name}'
                    })
            except Exception as e:
                print(f"Error reading {prof_file}: {e}")
    
    return professions

def scan_responsibilities(base_path):
    """Scan responsibility files"""
    responsibilities = []
    resp_file = base_path / "Responsibilities" / "responsibilities.json"
    
    if resp_file.exists():
        try:
            with open(resp_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for resp in data:
                    responsibilities.append({
                        'Entity_ID': resp.get('responsibility_id', 'RESP-000'),
                        'Entity_Name': resp.get('responsibility_name', ''),
                        'Entity_Type': 'Responsibilities',
                        'Department': resp.get('department', 'Multi-Department'),
                        'Category': 'Responsibility',
                        'File_Path': f'LIBRARIES/Responsibilities/responsibilities.json',
                        'Count': 1,
                        'Status': 'Active',
                        'ISO_Code': resp.get('responsibility_id', 'RESP-000'),
                        'Notes': f"Responsibility: {resp.get('responsibility_name', '')}"
                    })
        except Exception as e:
            print(f"Error reading responsibilities file: {e}")
    
    return responsibilities

def scan_objects(base_path):
    """Scan object files"""
    objects = []
    objects_dir = base_path / "Responsibilities" / "Objects"
    
    if not objects_dir.exists():
        return objects
    
    for obj_file in objects_dir.glob("*.json"):
        try:
            with open(obj_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, dict) and 'objects' in data:
                    for obj in data['objects']:
                        objects.append({
                            'Entity_ID': obj.get('object_id', 'OBJ-000'),
                            'Entity_Name': obj.get('name', ''),
                            'Entity_Type': 'Objects',
                            'Department': obj.get('category', 'Multi-Department'),
                            'Category': 'Object',
                            'File_Path': f'LIBRARIES/Responsibilities/Objects/{obj_file.name}',
                            'Count': 1,
                            'Status': 'Active',
                            'ISO_Code': obj.get('object_id', 'OBJ-000'),
                            'Notes': f"Object: {obj.get('name', '')}"
                        })
        except Exception as e:
            print(f"Error reading {obj_file}: {e}")
    
    return objects

def scan_departments(base_path):
    """Scan department files"""
    departments = []
    dept_file = base_path / "DEPARTMENTS" / "departments.json"
    
    if dept_file.exists():
        try:
            with open(dept_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, dict) and 'data' in data:
                    for dept in data['data']:
                        departments.append({
                            'Entity_ID': dept.get('department_id', 'DPT-000'),
                            'Entity_Name': dept.get('name', ''),
                            'Entity_Type': 'Departments',
                            'Department': dept.get('full_name', ''),
                            'Category': 'Department',
                            'File_Path': f'LIBRARIES/LBS_006_Departments/Master/departments.json',
                            'Count': 1,
                            'Status': 'Active' if dept.get('is_active', True) else 'Inactive',
                            'ISO_Code': dept.get('code', ''),
                            'Notes': f"Department: {dept.get('full_name', '')}"
                        })
        except Exception as e:
            print(f"Error reading departments file: {e}")
    
    return departments

def main():
    """Generate master list"""
    base_path = Path(__file__).parent.parent
    output_file = base_path / "Taxonomy" / f"Libraries_Master_List_{datetime.now().strftime('%Y-%m-%d')}.csv"
    
    print(f"Scanning LIBRARIES directory: {base_path}")
    
    # Collect all entities
    all_entities = []
    
    # Add master/collection entries first
    master_entries = [
        {'Entity_ID': 'RSP-001', 'Entity_Name': 'Core Responsibilities', 'Entity_Type': 'Responsibilities', 'Department': 'Multi-Department', 'Category': 'Core', 'File_Path': 'LIBRARIES/Responsibilities/Core/responsibilities.json', 'Count': 193, 'Status': 'Active', 'ISO_Code': 'RSP', 'Notes': 'Master responsibilities file'},
        {'Entity_ID': 'ACT-001', 'Entity_Name': 'Actions Master', 'Entity_Type': 'Actions', 'Department': 'Multi-Department', 'Category': 'Master', 'File_Path': 'LIBRARIES/Responsibilities/Actions/Master/actions_master.json', 'Count': 429, 'Status': 'Active', 'ISO_Code': 'ACT', 'Notes': 'Complete actions catalog'},
        {'Entity_ID': 'SKL-001', 'Entity_Name': 'Skills Master', 'Entity_Type': 'Skills', 'Department': 'Multi-Department', 'Category': 'Master', 'File_Path': 'LIBRARIES/LBS_004_LBS_004_../TALENTS/Skills/Master/all_skills.json', 'Count': 28, 'Status': 'Active', 'ISO_Code': 'SKL', 'Notes': 'Complete skills catalog'},
        {'Entity_ID': 'TOL-001', 'Entity_Name': 'AI Tools Master Listing', 'Entity_Type': 'Tools', 'Department': 'AI', 'Category': 'Category', 'File_Path': 'LIBRARIES/LBS_003_LBS_003_Tools/By_Category/AI/AI_Tools_Master_Listing.json', 'Count': 80, 'Status': 'Active', 'ISO_Code': 'TOL-AIA', 'Notes': 'Complete AI tools catalog'},
    ]
    all_entities.extend(master_entries)
    
    # Scan individual entities
    print("Scanning tools...")
    all_entities.extend(scan_tools(base_path))
    
    print("Scanning skills...")
    all_entities.extend(scan_skills(base_path))
    
    print("Scanning professions...")
    all_entities.extend(scan_professions(base_path))
    
    print("Scanning responsibilities...")
    all_entities.extend(scan_responsibilities(base_path))
    
    print("Scanning objects...")
    all_entities.extend(scan_objects(base_path))
    
    print("Scanning departments...")
    all_entities.extend(scan_departments(base_path))
    
    # Write CSV
    fieldnames = ['Entity_ID', 'Entity_Name', 'Entity_Type', 'Department', 'Category', 'File_Path', 'Count', 'Status', 'ISO_Code', 'Notes']
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_entities)
    
    print(f"\nMaster list generated: {output_file}")
    print(f"Total entities: {len(all_entities)}")
    print(f"\nBreakdown by type:")
    for entity_type in set(e['Entity_Type'] for e in all_entities):
        count = sum(1 for e in all_entities if e['Entity_Type'] == entity_type)
        print(f"  {entity_type}: {count}")

if __name__ == "__main__":
    main()

