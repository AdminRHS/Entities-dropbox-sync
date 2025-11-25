"""
Merge 2025-11-20 tasks with existing consolidated tasks
"""

import csv
from pathlib import Path

BASE_DIR = Path(r"C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_4")

# Input files
nov20_file = BASE_DIR / "Tasks_2025_11_20.csv"
consolidated_file = BASE_DIR / "ALL_TASKS_CONSOLIDATED.csv"

# Output file
output_file = BASE_DIR / "ALL_TASKS_CONSOLIDATED_WITH_NOV20.csv"

print("Merging tasks...")

# Read existing consolidated tasks
existing_tasks = []
with open(consolidated_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    existing_fields = reader.fieldnames
    existing_tasks = list(reader)

print(f"  Loaded {len(existing_tasks)} existing tasks")

# Read Nov 20 tasks
nov20_tasks = []
with open(nov20_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    nov20_fields = reader.fieldnames
    nov20_tasks = list(reader)

print(f"  Loaded {len(nov20_tasks)} Nov 20 tasks")

# Merge fields (union of all fields)
all_fields = list(dict.fromkeys(existing_fields + nov20_fields))

# Normalize Nov 20 tasks to match existing format
normalized_nov20 = []
for task in nov20_tasks:
    normalized = {}
    for field in all_fields:
        if field in task:
            normalized[field] = task[field]
        else:
            normalized[field] = ''
    normalized_nov20.append(normalized)

# Normalize existing tasks
normalized_existing = []
for task in existing_tasks:
    normalized = {}
    for field in all_fields:
        if field in task:
            normalized[field] = task[field]
        else:
            normalized[field] = ''
    normalized_existing.append(normalized)

# Combine
all_tasks = normalized_existing + normalized_nov20

# Write merged output
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=all_fields)
    writer.writeheader()
    writer.writerows(all_tasks)

print(f"\n[OK] Created {output_file}")
print(f"[OK] Total tasks: {len(all_tasks)}")
print(f"  - Existing: {len(existing_tasks)}")
print(f"  - Nov 20: {len(nov20_tasks)}")
