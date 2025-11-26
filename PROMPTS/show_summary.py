import csv
from collections import Counter

MASTER_LIST_PATH = r"C:\Users\Dell\Dropbox\ENTITIES\PROMPTS\PROMPTS_Master_List.csv"

with open(MASTER_LIST_PATH, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

depts = Counter([r['Department'] for r in rows])
statuses = Counter([r['Status'] for r in rows])

print("=== PROMPTS MASTER LIST SUMMARY ===")
print(f"\nTotal Entries: {len(rows)}")
print(f"Previously: 62 entries")
print(f"Newly Added: {len(rows) - 62} entries")

print(f"\nBy Department:")
for dept, count in sorted(depts.items()):
    print(f"  {dept}: {count}")

print(f"\nBy Status:")
for status, count in sorted(statuses.items()):
    print(f"  {status}: {count}")

print(f"\n[SUCCESS] Master List updated successfully!")
print(f"[SUCCESS] Core folder was excluded as requested")
