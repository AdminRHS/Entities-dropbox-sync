import json

# Read the original file
with open('crm_export_2025-11-19 copy.md', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Write formatted JSON
with open('crm_export_2025-11-19_FORMATTED.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Formatted {len(data)} employee records successfully!")


