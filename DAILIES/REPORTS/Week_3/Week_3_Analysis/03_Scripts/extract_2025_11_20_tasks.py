"""
Extract tasks from 2025-11-20 Department Reports
Parses narrative markdown reports and extracts structured task data.
"""

import csv
import re
from pathlib import Path
from collections import defaultdict

# Configuration
BASE_DIR = Path(r"C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS")
REPORTS_DIR = BASE_DIR / "Reports_week 3" / "2025-11-20" / "Departments_Processed_TM"
OUTPUT_DIR = BASE_DIR / "Week_4"
OUTPUT_FILE = OUTPUT_DIR / "Tasks_2025_11_20.csv"

# Department mapping
DEPT_CODE_MAP = {
    'AID': 'AI',
    'HRM': 'HR',
    'VID': 'Video',
    'DEV': 'Development',
    'DGN': 'Design',
    'FIN': 'Finance',
    'SLS': 'Sales',
    'LGN': 'Lead Generation'
}

class Nov20Extractor:
    def __init__(self):
        self.tasks = []
        self.task_counter = defaultdict(int)

    def extract_from_markdown(self, md_file):
        """Extract tasks from a department markdown report"""
        print(f"Processing: {md_file.name}")

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract department code from filename (e.g., AID_Department_Report_2025-11-20.md)
            dept_code = md_file.stem.split('_')[0]
            dept_name = DEPT_CODE_MAP.get(dept_code, dept_code)

            # Extract tasks from "TASK SEQUENCES AND ENTITY MAPPING" section
            task_sections = re.findall(
                r'### Activity \d+: (.+?)\n(.*?)(?=### Activity \d+:|## \d+\.|$)',
                content,
                re.DOTALL
            )

            for activity_name, activity_content in task_sections:
                task = self._parse_activity(activity_name, activity_content, dept_code, dept_name)
                if task:
                    self.tasks.append(task)

            print(f"  Extracted {len(task_sections)} activities")
            return len(task_sections)

        except Exception as e:
            print(f"  [ERROR] {e}")
            return 0

    def _parse_activity(self, activity_name, content, dept_code, dept_name):
        """Parse an activity section into structured task data"""

        # Extract time
        time_match = re.search(r'\*\*Time:\*\*\s*(\d+(?:\.\d+)?)\s*hours?', content)
        time_hours = float(time_match.group(1)) if time_match else 0.0

        # Extract status
        status = "Completed" if "✅" in content or "Completed" in content else "In Progress"

        # Extract priority
        priority_match = re.search(r'\*\*Priority:\*\*\s*(\w+)', content)
        priority = priority_match.group(1) if priority_match else "Medium"

        # Extract confidence
        confidence_match = re.search(r'\*\*Confidence:\*\*\s*(\d+)%', content)
        confidence = confidence_match.group(1) if confidence_match else "N/A"

        # Extract objective
        objective_match = re.search(r'\*\*Objective:\*\*\s*(.+?)(?=\n\*\*|\n-|$)', content, re.DOTALL)
        objective = objective_match.group(1).strip() if objective_match else ""

        # Extract actions taken
        actions_match = re.search(r'\*\*Actions Taken:\*\*\s*\n((?:\s*-\s*.+?\n)+)', content, re.DOTALL)
        actions = []
        if actions_match:
            actions = [line.strip('- ').strip() for line in actions_match.group(1).split('\n') if line.strip().startswith('-')]

        # Extract results
        results_match = re.search(r'\*\*Results:\*\*\s*\n((?:\s*-\s*.+?\n)+)', content, re.DOTALL)
        results = []
        if results_match:
            results = [line.strip('- ').strip() for line in results_match.group(1).split('\n') if line.strip().startswith('-')]

        # Generate entity ID
        self.task_counter[dept_code] += 1
        entity_id = f"TSK-{dept_code}-2025-11-20-{self.task_counter[dept_code]:03d}"

        # Determine entity type
        if "project" in activity_name.lower() or "Project" in content:
            entity_type = "PRT"
        elif "milestone" in activity_name.lower():
            entity_type = "MLT"
        else:
            entity_type = "TSK"

        return {
            'Date': '2025-11-20',
            'Department': dept_name,
            'Department_Code': dept_code,
            'Employee': 'Team',  # Not specified in these reports
            'Activity_Name': activity_name.strip(),
            'Entity_Type': entity_type,
            'Entity_ID': entity_id,
            'Priority': priority,
            'Status': status,
            'Time_Hours': time_hours,
            'Confidence': confidence,
            'Objective': objective[:200] if objective else '',  # Limit length
            'Actions_Taken': '; '.join(actions[:3]) if actions else '',  # Top 3 actions
            'Key_Results': '; '.join(results[:3]) if results else '',  # Top 3 results
        }

    def write_csv(self):
        """Write extracted tasks to CSV"""
        if not self.tasks:
            print("[!] No tasks extracted")
            return

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
            fieldnames = [
                'Date', 'Department', 'Department_Code', 'Employee',
                'Activity_Name', 'Entity_Type', 'Entity_ID', 'Priority',
                'Status', 'Time_Hours', 'Confidence', 'Objective',
                'Actions_Taken', 'Key_Results'
            ]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.tasks)

        print(f"\n[OK] Created {OUTPUT_FILE}")
        print(f"[OK] Total tasks extracted: {len(self.tasks)}")

    def run(self):
        """Execute extraction pipeline"""
        print("=" * 60)
        print("2025-11-20 TASK EXTRACTION")
        print("=" * 60)

        if not REPORTS_DIR.exists():
            print(f"[ERROR] Reports directory not found: {REPORTS_DIR}")
            return

        # Process all department reports
        for md_file in REPORTS_DIR.glob("*_Department_Report_2025-11-20.md"):
            self.extract_from_markdown(md_file)

        # Write output
        self.write_csv()

        # Summary by department
        dept_summary = defaultdict(int)
        for task in self.tasks:
            dept_summary[task['Department']] += 1

        print("\nDepartment Summary:")
        for dept, count in sorted(dept_summary.items()):
            print(f"  {dept}: {count} tasks")

if __name__ == "__main__":
    extractor = Nov20Extractor()
    extractor.run()
