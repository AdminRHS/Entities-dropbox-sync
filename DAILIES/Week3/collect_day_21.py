#!/usr/bin/env python3
"""
Collect all day 21 files from employee folders
"""
import os
import shutil
from pathlib import Path

# Source and destination
nov25_base = Path(r"C:\Users\Dell\Dropbox\Nov25")
dest_dir = Path(r"C:\Users\Dell\Dropbox\ENTITIES\DAILIES\21")

# Ensure destination exists
dest_dir.mkdir(parents=True, exist_ok=True)

# Department folders
departments = [
    "AI Nov25",
    "Design Nov25",
    "Dev Nov25",
    "Fin Nov25",
    "HR Nov25",
    "LG Nov25",
    "Sales Nov25",
    "Video Nov25"
]

# Track statistics
stats = {
    "total_files": 0,
    "by_dept": {},
    "employees": []
}

# Process each department
for dept in departments:
    dept_path = nov25_base / dept
    if not dept_path.exists():
        continue

    dept_code = dept.split()[0]  # AI, Design, Dev, etc.
    stats["by_dept"][dept_code] = {"employees": 0, "files": 0}

    # Find all employees in this department
    for employee_dir in dept_path.iterdir():
        if not employee_dir.is_dir():
            continue

        employee_name = employee_dir.name

        # Check for Week_3/21 first
        day_21_week3 = employee_dir / "Week_3" / "21"
        day_21_direct = employee_dir / "21"

        day_21_path = None
        if day_21_week3.exists():
            day_21_path = day_21_week3
        elif day_21_direct.exists():
            day_21_path = day_21_direct

        if not day_21_path:
            continue

        # Found day 21 data for this employee
        stats["by_dept"][dept_code]["employees"] += 1
        stats["employees"].append(f"{employee_name} ({dept_code})")

        # Copy all .md files
        for md_file in day_21_path.glob("*.md"):
            # Create standardized filename
            file_type = md_file.stem.lower()  # daily, plans, task, etc.

            # Normalize employee name (replace spaces with underscores)
            safe_name = employee_name.replace(" ", "_").replace("'", "").replace("ʼ", "")

            # Determine destination filename
            if dept_code in ["LG", "Sales"] and dept == "Sales Nov25":
                dest_name = f"{file_type}_{safe_name}_Sales.md"
            else:
                dest_name = f"{file_type}_{safe_name}.md"

            dest_file = dest_dir / dest_name

            # Copy file
            try:
                shutil.copy2(md_file, dest_file)
                stats["total_files"] += 1
                stats["by_dept"][dept_code]["files"] += 1
                print(f"[OK] Copied: {dest_name}")
            except Exception as e:
                print(f"[ERROR] Error copying {md_file}: {e}")

# Print summary
print("\n" + "=" * 60)
print("COLLECTION SUMMARY")
print("=" * 60)
print(f"Total files copied: {stats['total_files']}")
print(f"Total employees: {len(stats['employees'])}")
print("\nBy Department:")
for dept, data in sorted(stats["by_dept"].items()):
    if data["employees"] > 0:
        print(f"  {dept:10} - {data['employees']} employees, {data['files']} files")

print("\nEmployees processed:")
for emp in sorted(stats["employees"]):
    print(f"  - {emp}")

print(f"\nAll files saved to: {dest_dir}")
