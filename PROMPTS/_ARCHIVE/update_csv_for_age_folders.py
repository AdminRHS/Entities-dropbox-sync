"""
Update Master CSV with new folder paths for age-organized prompts
"""
import csv
import os

MASTER_CSV = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\PROMPTS_Master_List.csv"
BACKUP_CSV = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\_ARCHIVE\PROMPTS_Master_List_BACKUP_AGE_ORG.csv"

# Files moved to Last_Week/
last_week_files = [
    'PMT-053_CV_Parser_v1.md',
    'PMT-069_Version_Control_Main.md',
    'PMT-029_System_Health_Review.md',
    'PMT-060_Products_Integration.md',
    'PMT-023_Schema_Validation.md',
    'PMT-024_Content_Analysis.md',
    'PMT-030_Architecture_Learning_Guide.md',
    'PMT-059_Document_Finished_Project.md',
    'PMT-025_Relationship_Validation.md',
    'PMT-026_Synthesis_Recommendations.md',
    'PMT-054_CRM_Data_Entry.md',
    'PMT-056_Interview_Conductor.md',
    'PMT-057_Job_Sites_Research.md',
    'PMT-062_Tools_Collection_Matching.md',
    'PMT-058_Call_Organizer_v4.md',
    'PMT-021_Ecosystem_Analysis_Overview.md',
    'PMT-031_Architecture_Merge_Planning.md',
    'PMT-027_Data_Consistency.md',
    'PMT-022_Data_Inventory.md',
    'PMT-061_Task_Manager_Entity_Filling.md',
    'PMT-063_Account_Creation_Validation.md',
    'PMT-064_Account_Security_Audit.md',
    'PMT-065_Subscription_Renewal_Alert.md',
    'PMT-018_Employee_Profile_Schema.md',
    'PMT-014_Build_Taxonomy_ID_System.md',
    'PMT-019_Restructure_Employee_Profile.md',
    'PMT-066_Script_Copy_Dailies.md',
    'PMT-070_Entity_Identification_v1.md',
    'PROMPTS_ISO_Code_Registry.md',
    'PROMPTS_Hierarchy_Tree.md',
    'PROMPTS_Folder_ID_Registry.md',
]

# Files moved to Old/
old_files = [
    'PMT-068_Version_Control_Automation.md',
    'PMT-067_Rules_Automation.md',
]

print("=" * 60)
print("UPDATING MASTER CSV")
print("=" * 60)

# Read current CSV
entries = []
with open(MASTER_CSV, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    entries = list(reader)

print(f"Loaded {len(entries)} entries")

# Create backup
import shutil
shutil.copy2(MASTER_CSV, BACKUP_CSV)
print(f"Backup created: {os.path.basename(BACKUP_CSV)}")

# Update paths
updated = 0
for entry in entries:
    file_path = entry['File_Path']
    filename = file_path.split('/')[-1]

    if filename in last_week_files:
        entry['File_Path'] = f"ENTITIES/PROMPTS/Last_Week/{filename}"
        updated += 1
    elif filename in old_files:
        entry['File_Path'] = f"ENTITIES/PROMPTS/Old/{filename}"
        updated += 1

# Write updated CSV
with open(MASTER_CSV, 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['ID', 'Name', 'Category', 'File_Path', 'Status']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(entries)

print(f"\n[SUCCESS] Updated {updated} file paths in Master CSV")
print(f"  - Last_Week/: {len(last_week_files)} files")
print(f"  - Old/: {len(old_files)} files")
print("\n[SUCCESS] Master CSV updated!")
