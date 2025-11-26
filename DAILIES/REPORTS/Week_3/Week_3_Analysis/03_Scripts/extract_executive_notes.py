"""
Executive Notes Extraction Script
Extracts strategic tasks from Executive Notes with connection and grouping analysis.
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
EXEC_NOTES_DIR = WEEK_3_DIR / "Executive_Notes_Summary"
OUTPUT_DIR = BASE_DIR / "Week_4" / "Executive_Strategic"

# Entity fields
EXECUTIVE_FIELDS = [
    "Date",
    "Source_File",
    "Entity_Type",
    "Entity_ID",
    "Activity_Name",
    "Full_Description",
    "Related_Project",
    "Related_Milestone",
    "Department",
    "Priority",
    "Category",
    "Tags"
]


class ExecutiveNotesExtractor:
    """Extract and analyze executive strategic tasks with connections"""

    def __init__(self):
        self.all_tasks = []
        self.all_projects = []
        self.all_milestones = []
        self.connections = []
        self.categories = defaultdict(list)
        self.department_mapping = defaultdict(list)

    def extract_from_file(self, md_file):
        """Extract all entities from a single executive note file"""
        print(f"Processing: {md_file.name}")

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract date from filename
            file_date = self._parse_filename_date(md_file.stem)

            # Extract projects with their milestones and tasks
            projects = self._extract_projects(content, md_file.name, file_date)

            # Extract standalone milestones
            milestones = self._extract_milestones(content, md_file.name, file_date)

            # Extract standalone tasks
            tasks = self._extract_tasks(content, md_file.name, file_date)

            print(f"  Found: {len(projects)} projects, {len(milestones)} milestones, {len(tasks)} tasks")

            return len(projects) + len(milestones) + len(tasks)

        except Exception as e:
            print(f"  [ERROR] {e}")
            return 0

    def _parse_filename_date(self, filename):
        """Parse date from filename like '211225_Niko_PROCESSED'"""
        try:
            date_part = filename.split('_')[0]
            day = date_part[:2]
            month = date_part[2:4]
            year = "20" + date_part[4:6]
            return f"{year}-{month}-{day}"
        except:
            return "2025-11-21"

    def _extract_projects(self, content, source_file, date):
        """Extract projects with their associated milestones and tasks"""
        projects = []

        # Pattern for project sections: ## 2. MAJOR PROJECTS IDENTIFIED
        project_sections = re.findall(
            r'###\s+(PRT-\d{3}):\s+(.+?)\n(.*?)(?=###\s+PRT-|\n##\s+\d+\.|\Z)',
            content,
            re.DOTALL
        )

        for project_id, project_name, project_content in project_sections:
            # Extract department from owner or context
            department = self._extract_department(project_content)

            # Extract priority
            priority = self._extract_priority(project_content)

            # Extract category/type
            category = self._extract_category(project_name, project_content)

            # Extract related milestones
            related_milestones = re.findall(r'MLT-\d{3}', project_content)

            # Extract related tasks
            related_tasks = re.findall(r'TSK-\d{3}', project_content)

            # Get full description (first paragraph after title)
            description_match = re.search(r'\*\*Context.*?:\*\*\s*\n(.*?)(?=\n\n|\n#)', project_content, re.DOTALL)
            description = description_match.group(1).strip() if description_match else project_name

            # Extract tags
            tags = self._extract_tags(project_content)

            project = {
                "Date": date,
                "Source_File": source_file,
                "Entity_Type": "PRT",
                "Entity_ID": project_id,
                "Activity_Name": project_name.strip(),
                "Full_Description": description[:500],
                "Related_Project": "",
                "Related_Milestone": ", ".join(related_milestones[:5]),
                "Department": department,
                "Priority": priority,
                "Category": category,
                "Tags": ", ".join(tags)
            }

            projects.append(project)
            self.all_projects.append(project)
            self.categories[category].append(project_id)
            self.department_mapping[department].append(project_id)

            # Store connections
            for mlt in related_milestones:
                self.connections.append({
                    "From": project_id,
                    "To": mlt,
                    "Type": "Project_to_Milestone"
                })

            for tsk in related_tasks:
                self.connections.append({
                    "From": project_id,
                    "To": tsk,
                    "Type": "Project_to_Task"
                })

        return projects

    def _extract_milestones(self, content, source_file, date):
        """Extract milestones from tables"""
        milestones = []

        # Pattern for milestone tables
        milestone_pattern = r'\|\s*\*\*(MLT-\d{3})\*\*\s*\|\s*([^|]+)\|'
        milestone_matches = re.findall(milestone_pattern, content)

        for entity_id, description in milestone_matches:
            # Check if part of a project (will skip if already captured)
            parent_project = self._find_parent_project(content, entity_id)

            # Extract department
            department = self._extract_department_from_context(content, entity_id)

            # Extract tags
            tags = self._extract_tags_from_description(description)

            milestone = {
                "Date": date,
                "Source_File": source_file,
                "Entity_Type": "MLT",
                "Entity_ID": entity_id.strip(),
                "Activity_Name": description.strip()[:100],
                "Full_Description": description.strip(),
                "Related_Project": parent_project,
                "Related_Milestone": "",
                "Department": department,
                "Priority": "High",
                "Category": "Milestone",
                "Tags": ", ".join(tags)
            }

            milestones.append(milestone)
            self.all_milestones.append(milestone)
            self.department_mapping[department].append(entity_id)

            if parent_project:
                self.connections.append({
                    "From": parent_project,
                    "To": entity_id,
                    "Type": "Project_to_Milestone"
                })

        return milestones

    def _extract_tasks(self, content, source_file, date):
        """Extract tasks from tables"""
        tasks = []

        # Pattern for task tables
        task_pattern = r'\|\s*\*\*(TSK-\d{3}|[A-Z]+-\d{3})\*\*\s*\|\s*([^|]+)\|'
        task_matches = re.findall(task_pattern, content)

        for entity_id, description in task_matches:
            # Skip if not TSK or other recognized prefixes
            if not any(entity_id.startswith(prefix) for prefix in ['TSK-', 'ARC-', 'FIX-']):
                continue

            # Find parent project/milestone
            parent_project = self._find_parent_project(content, entity_id)
            parent_milestone = self._find_parent_milestone(content, entity_id)

            # Extract department
            department = self._extract_department_from_context(content, entity_id)

            # Extract category
            category = self._categorize_task(description)

            # Extract tags
            tags = self._extract_tags_from_description(description)

            task = {
                "Date": date,
                "Source_File": source_file,
                "Entity_Type": entity_id.split('-')[0],
                "Entity_ID": entity_id.strip(),
                "Activity_Name": description.strip()[:100],
                "Full_Description": description.strip(),
                "Related_Project": parent_project,
                "Related_Milestone": parent_milestone,
                "Department": department,
                "Priority": "High",
                "Category": category,
                "Tags": ", ".join(tags)
            }

            tasks.append(task)
            self.all_tasks.append(task)
            self.categories[category].append(entity_id)
            self.department_mapping[department].append(entity_id)

            if parent_project:
                self.connections.append({
                    "From": parent_project,
                    "To": entity_id,
                    "Type": "Project_to_Task"
                })

            if parent_milestone:
                self.connections.append({
                    "From": parent_milestone,
                    "To": entity_id,
                    "Type": "Milestone_to_Task"
                })

        return tasks

    def _find_parent_project(self, content, entity_id):
        """Find which project this entity belongs to"""
        # Look for the entity within project sections
        project_sections = re.findall(
            r'(PRT-\d{3}):\s+.+?\n(.*?)(?=###\s+PRT-|\n##\s+\d+\.|\Z)',
            content,
            re.DOTALL
        )

        for project_id, project_content in project_sections:
            if entity_id in project_content:
                return project_id

        return ""

    def _find_parent_milestone(self, content, entity_id):
        """Find which milestone this task belongs to"""
        # Look backwards from task to find nearest milestone
        lines = content.split('\n')
        entity_index = -1

        for i, line in enumerate(lines):
            if entity_id in line:
                entity_index = i
                break

        if entity_index == -1:
            return ""

        # Search backwards for milestone
        for i in range(entity_index - 1, max(0, entity_index - 50), -1):
            mlt_match = re.search(r'MLT-\d{3}', lines[i])
            if mlt_match:
                return mlt_match.group(0)

        return ""

    def _extract_department(self, content):
        """Extract department from project content"""
        dept_keywords = {
            "AI": ["AI", "Automation", "AID"],
            "Development": ["Dev", "DEV", "Backend", "Frontend"],
            "Design": ["Design", "DGN", "Designer"],
            "Finance": ["Finance", "FIN"],
            "HR": ["HR", "HRM", "Human Resources"],
            "Lead Generation": ["LG", "LGN", "Lead Gen"],
            "Sales": ["Sales", "SLS"],
            "Video": ["Video", "VID"],
            "Executive": ["Strategic", "Company-wide", "All departments"]
        }

        content_lower = content.lower()
        for dept, keywords in dept_keywords.items():
            for keyword in keywords:
                if keyword.lower() in content_lower:
                    return dept

        return "Strategic"

    def _extract_department_from_context(self, content, entity_id):
        """Extract department from surrounding context"""
        # Find the line with entity_id and surrounding context
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if entity_id in line:
                # Check 10 lines before and after
                context = '\n'.join(lines[max(0, i-10):min(len(lines), i+10)])
                return self._extract_department(context)

        return "Strategic"

    def _extract_priority(self, content):
        """Extract priority from content"""
        content_upper = content.upper()
        if "CRITICAL" in content_upper:
            return "Critical"
        elif "HIGH" in content_upper:
            return "High"
        elif "MEDIUM" in content_upper:
            return "Medium"
        elif "LOW" in content_upper:
            return "Low"
        return "High"  # Default

    def _extract_category(self, name, content):
        """Categorize project based on name and content"""
        name_lower = name.lower()
        content_lower = content.lower()

        categories = {
            "Infrastructure": ["infrastructure", "architecture", "system", "backend", "database"],
            "Automation": ["automation", "script", "workflow", "n8n", "pipeline"],
            "Integration": ["integration", "api", "sync", "connect"],
            "Data": ["data", "scraping", "parsing", "extraction", "migration"],
            "UI/UX": ["dashboard", "ui", "frontend", "design", "interface"],
            "Analytics": ["analytics", "reporting", "metrics", "tracking"],
            "Training": ["training", "onboarding", "learning", "tutorial"],
            "Documentation": ["documentation", "docs", "guide", "readme"],
            "Security": ["security", "auth", "permission", "access"],
            "HR": ["hr", "employee", "talent", "recruitment"],
            "Sales": ["sales", "crm", "client", "business"],
            "Marketing": ["marketing", "social media", "content", "smm"]
        }

        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword in name_lower or keyword in content_lower:
                    return category

        return "Strategic"

    def _categorize_task(self, description):
        """Categorize task based on description"""
        desc_lower = description.lower()

        if any(word in desc_lower for word in ["create", "build", "develop", "implement"]):
            return "Development"
        elif any(word in desc_lower for word in ["research", "analyze", "review"]):
            return "Research"
        elif any(word in desc_lower for word in ["document", "write", "create guide"]):
            return "Documentation"
        elif any(word in desc_lower for word in ["fix", "resolve", "debug"]):
            return "Maintenance"
        elif any(word in desc_lower for word in ["design", "ui", "layout"]):
            return "Design"
        elif any(word in desc_lower for word in ["integrate", "connect", "sync"]):
            return "Integration"
        elif any(word in desc_lower for word in ["test", "verify", "validate"]):
            return "Testing"
        else:
            return "Task"

    def _extract_tags(self, content):
        """Extract relevant tags from content"""
        tags = []

        tag_patterns = {
            "Dropbox": r"\bdropbox\b",
            "GitHub": r"\bgithub\b",
            "VS Code": r"\bvs code\b|\bvscode\b",
            "Claude": r"\bclaude\b",
            "AI Tools": r"\bai tool|\bgemini\b|\bgpt\b",
            "CRM": r"\bcrm\b",
            "Discord": r"\bdiscord\b",
            "Vercel": r"\bvercel\b",
            "Postgres": r"\bpostgres\b|\bpostgresql\b",
            "n8n": r"\bn8n\b",
            "Taxonomy": r"\btaxonomy\b",
            "Entity System": r"\bentit(y|ies)\b",
            "Prompts": r"\bprompt\b",
            "Dashboard": r"\bdashboard\b"
        }

        content_lower = content.lower()
        for tag, pattern in tag_patterns.items():
            if re.search(pattern, content_lower, re.IGNORECASE):
                tags.append(tag)

        return tags[:5]  # Limit to 5 tags

    def _extract_tags_from_description(self, description):
        """Extract tags from description"""
        return self._extract_tags(description)

    def generate_outputs(self):
        """Generate all output files"""
        print(f"\nGenerating output files to: {OUTPUT_DIR}")
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        # 1. All Executive Tasks
        self._write_csv(
            OUTPUT_DIR / "Executive_All_Tasks.csv",
            EXECUTIVE_FIELDS,
            self.all_tasks + self.all_projects + self.all_milestones
        )

        # 2. Projects Only
        self._write_csv(
            OUTPUT_DIR / "Executive_Projects.csv",
            EXECUTIVE_FIELDS,
            self.all_projects
        )

        # 3. Milestones Only
        self._write_csv(
            OUTPUT_DIR / "Executive_Milestones.csv",
            EXECUTIVE_FIELDS,
            self.all_milestones
        )

        # 4. Tasks Only
        self._write_csv(
            OUTPUT_DIR / "Executive_Tasks.csv",
            EXECUTIVE_FIELDS,
            self.all_tasks
        )

        # 5. Connections/Relationships
        self._write_csv(
            OUTPUT_DIR / "Executive_Connections.csv",
            ["From", "To", "Type"],
            self.connections
        )

        # 6. Category Groupings
        self._write_category_summary()

        # 7. Department Groupings
        self._write_department_summary()

        # 8. Hierarchical JSON structure
        self._write_hierarchical_json()

        print("\nGeneration complete!")

    def _write_csv(self, filepath, fieldnames, data):
        """Write data to CSV file"""
        try:
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
                writer.writeheader()
                writer.writerows(data)
            print(f"  [OK] {filepath.name} ({len(data)} entries)")
        except Exception as e:
            print(f"  [ERROR] {filepath.name}: {e}")

    def _write_category_summary(self):
        """Write category groupings"""
        filepath = OUTPUT_DIR / "Executive_Categories.csv"

        rows = []
        for category, entities in sorted(self.categories.items()):
            rows.append({
                "Category": category,
                "Count": len(entities),
                "Entity_IDs": ", ".join(entities[:10])  # Limit display
            })

        self._write_csv(filepath, ["Category", "Count", "Entity_IDs"], rows)

    def _write_department_summary(self):
        """Write department groupings"""
        filepath = OUTPUT_DIR / "Executive_Departments.csv"

        rows = []
        for department, entities in sorted(self.department_mapping.items()):
            rows.append({
                "Department": department,
                "Count": len(entities),
                "Entity_IDs": ", ".join(entities[:10])  # Limit display
            })

        self._write_csv(filepath, ["Department", "Count", "Entity_IDs"], rows)

    def _write_hierarchical_json(self):
        """Write hierarchical structure as JSON"""
        filepath = OUTPUT_DIR / "Executive_Hierarchy.json"

        hierarchy = {
            "projects": [],
            "standalone_milestones": [],
            "standalone_tasks": []
        }

        # Build project hierarchy
        for project in self.all_projects:
            project_node = {
                "id": project["Entity_ID"],
                "name": project["Activity_Name"],
                "department": project["Department"],
                "category": project["Category"],
                "milestones": [],
                "tasks": []
            }

            # Find related milestones
            for mlt in self.all_milestones:
                if mlt["Related_Project"] == project["Entity_ID"]:
                    milestone_node = {
                        "id": mlt["Entity_ID"],
                        "name": mlt["Activity_Name"],
                        "tasks": []
                    }

                    # Find tasks under this milestone
                    for task in self.all_tasks:
                        if task["Related_Milestone"] == mlt["Entity_ID"]:
                            milestone_node["tasks"].append({
                                "id": task["Entity_ID"],
                                "name": task["Activity_Name"],
                                "category": task["Category"]
                            })

                    project_node["milestones"].append(milestone_node)

            # Find direct project tasks (not under milestones)
            for task in self.all_tasks:
                if task["Related_Project"] == project["Entity_ID"] and not task["Related_Milestone"]:
                    project_node["tasks"].append({
                        "id": task["Entity_ID"],
                        "name": task["Activity_Name"],
                        "category": task["Category"]
                    })

            hierarchy["projects"].append(project_node)

        # Standalone milestones
        for mlt in self.all_milestones:
            if not mlt["Related_Project"]:
                hierarchy["standalone_milestones"].append({
                    "id": mlt["Entity_ID"],
                    "name": mlt["Activity_Name"],
                    "department": mlt["Department"]
                })

        # Standalone tasks
        for task in self.all_tasks:
            if not task["Related_Project"] and not task["Related_Milestone"]:
                hierarchy["standalone_tasks"].append({
                    "id": task["Entity_ID"],
                    "name": task["Activity_Name"],
                    "category": task["Category"],
                    "department": task["Department"]
                })

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(hierarchy, f, indent=2, ensure_ascii=False)
            print(f"  [OK] {filepath.name}")
        except Exception as e:
            print(f"  [ERROR] {filepath.name}: {e}")


def main():
    """Main execution"""
    print("=" * 70)
    print("Executive Notes Strategic Task Extraction")
    print("=" * 70)
    print()

    if not EXEC_NOTES_DIR.exists():
        print(f"ERROR: Directory not found: {EXEC_NOTES_DIR}")
        return

    extractor = ExecutiveNotesExtractor()

    # Process all executive note files
    print("Processing executive note files...")
    print("-" * 70)

    total_entities = 0
    for md_file in sorted(EXEC_NOTES_DIR.glob("*_PROCESSED.md")):
        count = extractor.extract_from_file(md_file)
        total_entities += count

    print()
    print("=" * 70)
    print(f"Total entities extracted: {total_entities}")
    print(f"  - Projects: {len(extractor.all_projects)}")
    print(f"  - Milestones: {len(extractor.all_milestones)}")
    print(f"  - Tasks: {len(extractor.all_tasks)}")
    print(f"  - Connections: {len(extractor.connections)}")
    print("=" * 70)
    print()

    # Generate outputs
    extractor.generate_outputs()

    print()
    print("=" * 70)
    print("EXTRACTION COMPLETE")
    print(f"Output directory: {OUTPUT_DIR}")
    print("=" * 70)


if __name__ == "__main__":
    main()
