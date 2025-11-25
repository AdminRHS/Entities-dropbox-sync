import os
import json
import csv
import re

# Base path
base_path = r"C:\Users\Dell\Dropbox\ENTITIES\TASK_MANAGERS\Step_Templates"

# Output CSV file
output_csv = os.path.join(base_path, "Taxonomy", "Step_Templates_Master_List.csv")

# Ensure Taxonomy folder exists
os.makedirs(os.path.join(base_path, "Taxonomy"), exist_ok=True)

# Department mapping based on file paths and naming
dept_map = {
    "ADMIN": "ADM",
    "AI": "AID",
    "Content-Ops": "CTN",
    "DESIGN": "DGN",
    "DEV": "DEV",
    "HR": "HRM",
    "LG": "LGN",
    "Ops": "OPS",
    "SALES": "SLS",
    "Video": "VID"
}

# Function to extract department from filename or path
def get_department(filepath, filename):
    # Check path first
    for dept in dept_map.keys():
        if f"/{dept}/" in filepath or f"\\{dept}\\" in filepath:
            return dept_map[dept]

    # Check filename patterns
    filename_upper = filename.upper()
    for dept_code in ["ADMIN", "AI", "DESIGN", "DEV", "HR", "LG", "SALES", "VIDEO"]:
        if dept_code in filename_upper:
            return dept_map.get(dept_code.replace("VIDEO", "Video"), "AID")

    return "AID"  # Default to AI Department

# Function to extract description from filename
def get_description(filename):
    # Remove extension
    name = filename.replace(".json", "").replace(".md", "")

    # Remove Step-Template-XXX_ prefix
    name = re.sub(r'^Step-Template-\d{3}_', '', name)

    # Replace hyphens and underscores with spaces
    name = name.replace("_", " ").replace("-", " ")

    # Capitalize words
    return " ".join(word.capitalize() for word in name.split())

# Collect all step templates
step_templates = []

for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.startswith("Step-Template-") and (file.endswith(".json") or file.endswith(".md")):
            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, r"C:\Users\Dell\Dropbox")

            # Extract step number
            match = re.search(r'Step-Template-(\d{3})', file)
            if match:
                step_num = int(match.group(1))

                # Get department and description
                dept = get_department(filepath, file)
                desc = get_description(file)

                step_templates.append({
                    "new_id": f"STT-{step_num:03d}",
                    "entity_type": "Step_Template",
                    "current_id": file.replace(".json", "").replace(".md", ""),
                    "name": desc,
                    "description": f"Step template for {desc.lower()}",
                    "department": dept,
                    "file_path": rel_path.replace("\\", "/"),
                    "status": "Active"
                })

# Sort by step number
step_templates.sort(key=lambda x: int(x["new_id"].split("-")[1]))

# Write to CSV
with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ["New_ID", "Entity_Type", "Current_ID", "Name", "Description", "Department", "File_Path", "Status"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for template in step_templates:
        writer.writerow({
            "New_ID": template["new_id"],
            "Entity_Type": template["entity_type"],
            "Current_ID": template["current_id"],
            "Name": template["name"],
            "Description": template["description"],
            "Department": template["department"],
            "File_Path": template["file_path"],
            "Status": template["status"]
        })

print(f"Generated {len(step_templates)} step templates in {output_csv}")
