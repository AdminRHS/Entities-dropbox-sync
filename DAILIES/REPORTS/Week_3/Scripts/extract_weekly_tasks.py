"""
Weekly Task Extraction Script
Extracts tasks, projects, and milestones from Week 3 daily reports
and creates clean CSV listings for Week 4 task distribution.
"""

import csv
import json
import os
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Configuration
BASE_DIR = Path(r"C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS")
WEEK_3_DIR = BASE_DIR / "Reports_week 3"
WEEK_4_DIR = BASE_DIR / "Week_4"
EXEC_NOTES_DIR = WEEK_3_DIR / "Executive_Notes_Summary"

# Source dates
SOURCE_DATES = ["2025-11-19", "2025-11-20", "2025-11-21"]

# Department mapping
DEPT_MAPPING = {
    "FIN": "Finance",
    "HRM": "HR",
    "VID": "Video",
    "AID": "AI_Automation",
    "DEV": "Development",
    "DGN": "Design",
    "SLS": "Sales",
    "LGN": "LeadGen"
}

# Minimal fields for clean listing
MINIMAL_FIELDS = [
    "Date",
    "Department",
    "Department_Code",
    "Employee",
    "Activity_Name",
    "Entity_Type",
    "Entity_ID",
    "Priority",
    "Status",
    "Time_Hours",
    "Objective",
    "Key_Results",
    "Next_Actions"
]


class TaskExtractor:
    """Extract and consolidate tasks from multiple sources"""

    def __init__(self):
        self.all_tasks = []
        self.projects = []
        self.milestones = []
        self.seen_entities = set()

    def extract_from_csv(self, csv_path):
        """Extract tasks from CSV master activity listing"""
        print(f"Extracting from CSV: {csv_path}")

        if not csv_path.exists():
            print(f"  [!] CSV not found: {csv_path}")
            return 0

        count = 0
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    entity_id = row.get('Entity_ID', '').strip()

                    # Skip if already seen
                    if entity_id in self.seen_entities:
                        continue

                    if entity_id:
                        self.seen_entities.add(entity_id)

                    # Extract minimal fields
                    task = {
                        "Date": row.get('Date', '').strip(),
                        "Department": row.get('Department', '').strip(),
                        "Department_Code": row.get('Department_Code', '').strip(),
                        "Employee": row.get('Employee', '').strip(),
                        "Activity_Name": row.get('Activity_Name', '').strip(),
                        "Entity_Type": row.get('Entity_Type', '').strip(),
                        "Entity_ID": entity_id,
                        "Priority": row.get('Priority', '').strip(),
                        "Status": row.get('Status', '').strip(),
                        "Time_Hours": row.get('Time_Hours', '0').strip(),
                        "Objective": row.get('Objective', '').strip(),
                        "Key_Results": row.get('Key_Results', '').strip(),
                        "Next_Actions": ""  # Will be filled from markdown if available
                    }

                    # Categorize by entity type
                    entity_type = task['Entity_Type'].upper()
                    if entity_type == 'PRT':
                        self.projects.append(task)
                    elif entity_type == 'MLT':
                        self.milestones.append(task)
                    else:
                        self.all_tasks.append(task)

                    count += 1

            print(f"  [OK] Extracted {count} entries")
            return count
        except Exception as e:
            print(f"  [ERROR] Error reading CSV: {e}")
            return 0

    def extract_from_markdown(self, md_path):
        """Extract next actions and additional context from markdown reports"""
        print(f"Parsing markdown: {md_path}")

        if not md_path.exists():
            print(f"  [!] Markdown not found: {md_path}")
            return

        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract next day plans section
            next_plans_match = re.search(
                r'##\s+(?:7\.|七\.)\s+Next Day Plans.*?(?=##|\Z)',
                content,
                re.DOTALL | re.IGNORECASE
            )

            if next_plans_match:
                next_plans = next_plans_match.group(0)
                # Parse tasks with entity IDs
                task_pattern = r'\*\*([A-Z]+-[A-Z]+-\d{4}-\d{2}-\d{2}-\d{3})\*\*[:\s]+(.*?)(?=\n\*\*[A-Z]+-|\Z)'

                for match in re.finditer(task_pattern, next_plans, re.DOTALL):
                    entity_id = match.group(1).strip()
                    next_action = match.group(2).strip()

                    # Find matching task and add next action
                    for task in self.all_tasks:
                        if task['Entity_ID'] == entity_id:
                            task['Next_Actions'] = next_action[:200]  # Limit length
                            break

            print(f"  [OK] Parsed markdown successfully")
        except Exception as e:
            print(f"  [ERROR] Error parsing markdown: {e}")

    def extract_from_executive_notes(self):
        """Extract strategic tasks from executive notes"""
        print(f"Parsing executive notes from: {EXEC_NOTES_DIR}")

        if not EXEC_NOTES_DIR.exists():
            print(f"  [!] Executive notes directory not found")
            return

        count = 0
        for md_file in EXEC_NOTES_DIR.glob("*_PROCESSED.md"):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Extract date from filename (e.g., "211225" -> "2025-11-21")
                file_date = md_file.stem.split('_')[0]
                try:
                    # Parse date like "211225" as DDMMYY
                    day = file_date[:2]
                    month = file_date[2:4]
                    year = "20" + file_date[4:6]
                    formatted_date = f"{year}-{month}-{day}"
                except:
                    formatted_date = "2025-11-21"

                # Extract tasks from markdown tables (format: | **TSK-###** | Description | ...)
                task_table_pattern = r'\|\s*\*\*([A-Z]+-\d{3})\*\*\s*\|\s*([^|]+)\|'
                task_matches = re.findall(task_table_pattern, content)

                for entity_id, description in task_matches:
                    entity_id = entity_id.strip()
                    description = description.strip()

                    if entity_id and entity_id not in self.seen_entities:
                        # Determine entity type from ID
                        entity_type = "TSK"
                        if entity_id.startswith("PRT-"):
                            entity_type = "PRT"
                        elif entity_id.startswith("MLT-"):
                            entity_type = "MLT"

                        # Create task from executive note
                        task = {
                            "Date": formatted_date,
                            "Department": "Executive",
                            "Department_Code": "EXC",
                            "Employee": "Strategic Planning",
                            "Activity_Name": description[:100].strip(),
                            "Entity_Type": entity_type,
                            "Entity_ID": entity_id,
                            "Priority": "High",
                            "Status": "Planned",
                            "Time_Hours": "0",
                            "Objective": description.strip(),
                            "Key_Results": "",
                            "Next_Actions": ""
                        }

                        # Categorize by entity type
                        if entity_type == 'PRT':
                            self.projects.append(task)
                        elif entity_type == 'MLT':
                            self.milestones.append(task)
                        else:
                            self.all_tasks.append(task)

                        self.seen_entities.add(entity_id)
                        count += 1

            except Exception as e:
                print(f"  [ERROR] Error parsing {md_file.name}: {e}")

        print(f"  [OK] Extracted {count} strategic tasks from executive notes")

    def generate_master_csv(self):
        """Generate master task list CSV"""
        output_path = WEEK_4_DIR / "Master_Task_List_Week4.csv"
        print(f"\nGenerating master CSV: {output_path}")

        all_entries = self.all_tasks + self.projects + self.milestones

        try:
            with open(output_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=MINIMAL_FIELDS)
                writer.writeheader()
                writer.writerows(all_entries)

            print(f"  [OK] Generated master CSV with {len(all_entries)} entries")
            return True
        except Exception as e:
            print(f"  [ERROR] Error generating master CSV: {e}")
            return False

    def generate_department_csvs(self):
        """Generate department-specific CSV files"""
        print(f"\nGenerating department-specific CSVs...")

        # Group by department
        dept_tasks = defaultdict(list)
        for task in self.all_tasks + self.projects + self.milestones:
            dept_code = task.get('Department_Code', 'UNK')
            dept_tasks[dept_code].append(task)

        generated = 0
        for dept_code, tasks in dept_tasks.items():
            dept_name = DEPT_MAPPING.get(dept_code, dept_code)
            output_path = WEEK_4_DIR / f"{dept_name}_Tasks_Week4.csv"

            try:
                with open(output_path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=MINIMAL_FIELDS)
                    writer.writeheader()
                    writer.writerows(tasks)

                print(f"  [OK] {dept_name}: {len(tasks)} tasks")
                generated += 1
            except Exception as e:
                print(f"  [ERROR] Error generating {dept_name} CSV: {e}")

        return generated

    def generate_projects_milestones_csv(self):
        """Generate projects and milestones CSV"""
        output_path = WEEK_4_DIR / "Projects_Milestones_Week4.csv"
        print(f"\nGenerating projects/milestones CSV: {output_path}")

        entries = self.projects + self.milestones

        try:
            with open(output_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=MINIMAL_FIELDS)
                writer.writeheader()
                writer.writerows(entries)

            print(f"  [OK] Generated {len(self.projects)} projects and {len(self.milestones)} milestones")
            return True
        except Exception as e:
            print(f"  [ERROR] Error generating projects/milestones CSV: {e}")
            return False

    def generate_summary_csv(self):
        """Generate summary statistics by department"""
        output_path = WEEK_4_DIR / "Summary_By_Department.csv"
        print(f"\nGenerating department summary: {output_path}")

        # Calculate statistics by department
        dept_stats = defaultdict(lambda: {
            'Department': '',
            'Department_Code': '',
            'Total_Tasks': 0,
            'Total_Projects': 0,
            'Total_Milestones': 0,
            'Total_Hours': 0.0,
            'Unique_Employees': set(),
            'Completed_Tasks': 0,
            'In_Progress_Tasks': 0,
            'High_Priority': 0,
            'Critical_Priority': 0
        })

        all_entries = self.all_tasks + self.projects + self.milestones

        for entry in all_entries:
            dept_code = entry.get('Department_Code', 'UNK')
            stats = dept_stats[dept_code]

            stats['Department'] = entry.get('Department', dept_code)
            stats['Department_Code'] = dept_code

            # Count by entity type
            entity_type = entry.get('Entity_Type', '').upper()
            if entity_type == 'PRT':
                stats['Total_Projects'] += 1
            elif entity_type == 'MLT':
                stats['Total_Milestones'] += 1
            else:
                stats['Total_Tasks'] += 1

            # Sum hours
            try:
                hours = float(entry.get('Time_Hours', 0))
                stats['Total_Hours'] += hours
            except:
                pass

            # Track employees
            employee = entry.get('Employee', '').strip()
            if employee:
                stats['Unique_Employees'].add(employee)

            # Status counts
            status = entry.get('Status', '').lower()
            if 'completed' in status:
                stats['Completed_Tasks'] += 1
            elif 'progress' in status:
                stats['In_Progress_Tasks'] += 1

            # Priority counts
            priority = entry.get('Priority', '').lower()
            if priority == 'high':
                stats['High_Priority'] += 1
            elif priority == 'critical':
                stats['Critical_Priority'] += 1

        # Write summary
        try:
            with open(output_path, 'w', newline='', encoding='utf-8') as f:
                fieldnames = [
                    'Department', 'Department_Code', 'Total_Tasks', 'Total_Projects',
                    'Total_Milestones', 'Total_Hours', 'Unique_Employees',
                    'Completed_Tasks', 'In_Progress_Tasks', 'High_Priority', 'Critical_Priority'
                ]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()

                for dept_code in sorted(dept_stats.keys()):
                    stats = dept_stats[dept_code]
                    stats['Unique_Employees'] = len(stats['Unique_Employees'])
                    stats['Total_Hours'] = round(stats['Total_Hours'], 2)
                    writer.writerow(stats)

            print(f"  [OK] Generated summary for {len(dept_stats)} departments")
            return True
        except Exception as e:
            print(f"  [ERROR] Error generating summary CSV: {e}")
            return False


def main():
    """Main extraction workflow"""
    print("=" * 60)
    print("Weekly Task Extraction - Week 3 to Week 4")
    print("=" * 60)
    print()

    # Create output directory
    WEEK_4_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {WEEK_4_DIR}")
    print()

    # Initialize extractor
    extractor = TaskExtractor()

    # Step 1: Extract from CSV files
    print("STEP 1: Extracting from CSV files")
    print("-" * 60)
    for date in SOURCE_DATES:
        csv_path = WEEK_3_DIR / date / f"MASTER_ACTIVITY_LISTING_{date}.csv"
        extractor.extract_from_csv(csv_path)
    print()

    # Step 2: Parse markdown reports for context
    print("STEP 2: Parsing markdown reports")
    print("-" * 60)
    for date in SOURCE_DATES:
        dept_dir = WEEK_3_DIR / date / "Departments"
        if dept_dir.exists():
            for md_file in dept_dir.glob("*_Department_Report_*.md"):
                extractor.extract_from_markdown(md_file)
    print()

    # Step 3: Extract from executive notes
    print("STEP 3: Extracting from executive notes")
    print("-" * 60)
    extractor.extract_from_executive_notes()
    print()

    # Step 4: Generate outputs
    print("STEP 4: Generating output CSVs")
    print("=" * 60)

    extractor.generate_master_csv()
    extractor.generate_department_csvs()
    extractor.generate_projects_milestones_csv()
    extractor.generate_summary_csv()

    # Final summary
    print()
    print("=" * 60)
    print("EXTRACTION COMPLETE")
    print("=" * 60)
    print(f"Total tasks extracted: {len(extractor.all_tasks)}")
    print(f"Total projects: {len(extractor.projects)}")
    print(f"Total milestones: {len(extractor.milestones)}")
    print(f"Unique entities: {len(extractor.seen_entities)}")
    print()
    print(f"Output files saved to: {WEEK_4_DIR}")
    print()
    print("Generated files:")
    for file in sorted(WEEK_4_DIR.glob("*.csv")):
        size = file.stat().st_size
        print(f"  - {file.name} ({size:,} bytes)")
    print()


if __name__ == "__main__":
    main()
