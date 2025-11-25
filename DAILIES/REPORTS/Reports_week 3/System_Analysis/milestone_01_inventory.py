import os
import json
from pathlib import Path
from collections import Counter, defaultdict

# Configuration
entities_path = Path(r'C:\Users\Dell\Dropbox\ENTITIES')
output_path = Path(r'C:\Users\Dell\Dropbox\ENTITIES\ANALYTICS\REPORTS\System_Analysis\Milestone_01_Data_Inventory')

print("="*60)
print("MILESTONE 1: DATA INVENTORY")
print("="*60)

# Task 1: Count files by extension
print("\n[TASK 1] Counting files by extension...")
file_extensions = Counter()
file_list = []

for file_path in entities_path.rglob('*'):
    if file_path.is_file():
        ext = file_path.suffix.lower() if file_path.suffix else '[no extension]'
        file_extensions[ext] += 1
        file_list.append(file_path)

# Save file distribution
with open(output_path / 'file_distribution.json', 'w') as f:
    json.dump(dict(file_extensions.most_common()), f, indent=2)

print(f"Total files: {len(file_list)}")
print(f"Unique extensions: {len(file_extensions)}")
print(f"\nTop 10 extensions:")
for ext, count in file_extensions.most_common(10):
    pct = (count / len(file_list)) * 100
    print(f"  {ext:20} {count:6} ({pct:5.1f}%)")

# Task 2: Map folder structure
print("\n[TASK 2] Mapping folder structure...")
folder_stats = defaultdict(lambda: {'files': 0, 'subdirs': 0})

for root, dirs, files in os.walk(entities_path):
    rel_path = Path(root).relative_to(entities_path)
    folder_stats[str(rel_path)]['files'] = len(files)
    folder_stats[str(rel_path)]['subdirs'] = len(dirs)

# Save folder structure
with open(output_path / 'folder_structure.json', 'w') as f:
    json.dump(dict(folder_stats), f, indent=2)

print(f"Total folders: {len(folder_stats)}")

# Count files by entity (top-level folders)
entity_counts = defaultdict(int)
for file_path in file_list:
    try:
        entity = file_path.relative_to(entities_path).parts[0]
        entity_counts[entity] += 1
    except:
        pass

print(f"\nFiles by entity:")
for entity in sorted(entity_counts.keys()):
    count = entity_counts[entity]
    pct = (count / len(file_list)) * 100
    print(f"  {entity:30} {count:6} ({pct:5.1f}%)")

# Task 3: Analyze file sizes
print("\n[TASK 3] Analyzing file sizes...")
total_size = 0
size_by_ext = defaultdict(int)
large_files = []

for file_path in file_list:
    size_kb = file_path.stat().st_size / 1024
    total_size += size_kb
    ext = file_path.suffix.lower() if file_path.suffix else '[no extension]'
    size_by_ext[ext] += size_kb

    if size_kb > 100:  # Files larger than 100KB
        large_files.append({
            'path': str(file_path.relative_to(entities_path)),
            'size_kb': round(size_kb, 2)
        })

# Save file sizes
file_size_data = {
    'total_size_mb': round(total_size / 1024, 2),
    'size_by_extension_kb': {k: round(v, 2) for k, v in sorted(size_by_ext.items(), key=lambda x: x[1], reverse=True)},
    'large_files': sorted(large_files, key=lambda x: x['size_kb'], reverse=True)[:50]  # Top 50
}

with open(output_path / 'file_sizes.json', 'w') as f:
    json.dump(file_size_data, f, indent=2)

print(f"Total size: {total_size/1024:.2f} MB")
print(f"Average file size: {total_size/len(file_list):.2f} KB")
print(f"Files > 100KB: {len(large_files)}")

# Save summary
summary = {
    'total_files': len(file_list),
    'total_folders': len(folder_stats),
    'total_size_mb': round(total_size / 1024, 2),
    'unique_extensions': len(file_extensions),
    'entities': dict(entity_counts),
    'top_extensions': dict(file_extensions.most_common(10))
}

with open(output_path / 'milestone_01_summary.json', 'w') as f:
    json.dump(summary, f, indent=2)

print("\n" + "="*60)
print("MILESTONE 1 COMPLETE")
print("="*60)
print(f"\nOutputs saved to: {output_path}")
print("Files created:")
print("  - file_distribution.json")
print("  - folder_structure.json")
print("  - file_sizes.json")
print("  - milestone_01_summary.json")
