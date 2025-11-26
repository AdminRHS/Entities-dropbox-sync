"""
Simplify Master CSV
Remove redundant columns, update paths to flat structure
"""
import csv

MASTER_LIST = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\PROMPTS_Master_List.csv"
BACKUP = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\PROMPTS_Master_List_BACKUP_FULL.csv"
OUTPUT = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\PROMPTS_Master_List_NEW.csv"

# Read current CSV
entries = []
with open(MASTER_LIST, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    entries = list(reader)

print(f"Loaded {len(entries)} entries")

# Create backup
import shutil
shutil.copy2(MASTER_LIST, BACKUP)
print(f"Backup created: PROMPTS_Master_List_BACKUP_FULL.csv")

# Simplify entries
simplified = []
for entry in entries:
    # Determine category from old Current_ID or Department
    category = ""
    current_id = entry.get('Current_ID', '')
    dept = entry.get('Department', '')

    if 'PMT-' in current_id:
        pmt_num = current_id.replace('PMT-', '').split('_')[0]
        try:
            num = int(pmt_num)
            # Categorize by PMT number ranges
            if 1 <= num <= 13:
                category = "Video & Analysis"
            elif 14 <= num <= 20:
                category = "Taxonomy"
            elif 21 <= num <= 31:
                category = "System Analysis"
            elif 32 <= num <= 43:
                category = "Daily Reports"
            elif 53 <= num <= 57:
                category = "HR Operations"
            elif 58 <= num <= 65:
                category = "Workflows"
            elif 66 <= num <= 69:
                category = "Automation"
            elif 70 <= num <= 70:
                category = "Utilities"
            elif 74 <= num <= 80:
                category = "Data Architecture"
            elif 81 <= num <= 92:
                category = "System & Integration"
            else:
                category = dept or "General"
        except:
            category = dept or "General"
    elif 'CR' in current_id:
        category = "Core System"
    elif 'DR' in current_id:
        category = "Daily Reports"
    elif 'HR' in current_id:
        category = "HR Operations"
    elif 'VT' in current_id or 'VID' in dept:
        category = "Video & Analysis"
    elif 'TX' in current_id:
        category = "Taxonomy"
    elif 'SY' in current_id:
        category = "System"
    elif 'AT' in current_id:
        category = "Automation"
    elif 'OW' in current_id:
        category = "Workflows"
    else:
        category = dept or "General"

    # Extract just filename from path
    file_path = entry['File_Path']
    filename = file_path.split('/')[-1]

    # New simplified path (flat structure)
    if 'Core/' in file_path and ('MAIN_PROMPT' in file_path or 'PMT-001' in file_path or 'PMT-002' in file_path or 'PMT-003' in file_path):
        # Keep in Core folder
        new_path = file_path
    else:
        # Flat structure in PROMPTS root
        new_path = f"ENTITIES/PROMPTS/{filename}"

    simplified.append({
        'ID': entry['New_ID'],
        'Name': entry['Name'],
        'Category': category,
        'File_Path': new_path,
        'Status': entry['Status']
    })

# Write simplified CSV
with open(OUTPUT, 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['ID', 'Name', 'Category', 'File_Path', 'Status']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(simplified)

print(f"\n[SUCCESS] Created simplified CSV: PROMPTS_Master_List_NEW.csv")
print(f"Columns: ID, Name, Category, File_Path, Status")
print(f"Total entries: {len(simplified)}")

# Show sample
print("\nSample entries:")
for entry in simplified[:5]:
    print(f"  {entry['ID']}: {entry['Name']} ({entry['Category']})")

print("\nReview the new file, then rename it to replace the old one:")
print("  1. Check: PROMPTS_Master_List_NEW.csv")
print("  2. If good, rename to: PROMPTS_Master_List.csv")
