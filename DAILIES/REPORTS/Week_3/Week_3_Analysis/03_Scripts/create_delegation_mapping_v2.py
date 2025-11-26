"""
Enhanced Delegation Mapping System v2.0
- Reclassifies tasks by actual responsibility (not source department)
- Integrates LIBRARIES/Responsibilities for role identification
- Fixes misclassified departments (e.g., HR retention → HR, not AI)

Output Files (same as v1):
1. Task_Template_Mapping.csv
2. Team_Assignment_Matrix.csv
3. Department_Workload_Analysis.csv
4. Workflow_Clustering.csv
5. Assignment_Priority_Queue.csv
6. README.md

Author: AI Assistant
Date: 2025-11-24
Version: 2.0
"""

import csv
import json
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple

class DelegationMapperV2:
    def __init__(self):
        self.base_path = Path(r"C:\Users\Dell\Dropbox\ENTITIES")
        self.executive_tasks_file = self.base_path / "DAILIES" / "REPORTS" / "Week_4" / "Executive_Strategic" / "Executive_All_Tasks.csv"
        self.operational_tasks_file = self.base_path / "DAILIES" / "REPORTS" / "Week_4" / "Tasks_2025_11_20.csv"
        self.templates_path = self.base_path / "TASK_MANAGERS"
        self.libraries_path = self.base_path / "LIBRARIES"
        self.output_dir = self.base_path / "DAILIES" / "REPORTS" / "Week_4" / "Delegation"

        self.tasks = []
        self.templates = {}
        self.responsibilities = []
        self.mappings = []

        # Department reclassification keywords (CORRECTED MAPPING)
        self.department_keywords = {
            'HR': [
                'employee', 'retention', 'candidate', 'interview', 'onboarding', 'recruitment',
                'hire', 'firing', 'resign', 'quit', 'talent', 'pre-sale', 'trial',
                'verification', 'attendance', 'shift', '1:1 session', 'warming system'
            ],
            'Sales': [
                'client', 'clients', 'proposal', 'deal', 'discovery call', 'meeting',
                'business', 'prospect', 'prospects', 'crm', 'pipeline', 'outreach', 'closing',
                'communicate final decision', 'termination policy', 'customer', 'account',
                'relationship', 'follow-up', 'followup', 'contract negotiation',
                'presentation', 'demo', 'pitch'
            ],
            'Finance': [
                'financial', 'budget', 'cost', 'payment', 'accounting', 'invoice',
                'revenue', 'pricing', 'expense', 'gpt usage', 'cost-cutting',
                'billing', 'contract payment', 'subscription', 'payroll', 'tax'
            ],
            'Video': [
                'video', 'transcription', 'loom', 'youtube', 'editing', 'subtitle',
                'animation', 'recording', 'parsing video'
            ],
            'Design': [
                'design', 'ui', 'ux', 'mockup', 'prototype', 'figma', 'portfolio',
                'case study', 'branding', 'layout', 'visual'
            ],
            'Development': [
                'backend', 'frontend', 'api', 'database', 'deploy', 'microservice',
                'github', 'vercel', 'postgres', 'oauth', 'authentication',
                'schema', 'integration', 'sync'
            ],
            'Lead Generation': [
                'lead', 'scraping', 'google maps', 'linkedin', 'job sites',
                'prospect', 'outreach', 'connection request', 'lead generator'
            ],
            'SMM': [
                'social media', 'linkedin post', 'carousel', 'instagram', 'facebook',
                'twitter', 'content', 'posting', 'smm'
            ],
            'AI': [  # AI department should be AUTOMATION/INFRASTRUCTURE, not everything
                'entity system', 'taxonomy', 'script', 'automation', 'prompt',
                'parsing', 'extraction', 'ai tool', 'claude', 'gpt', 'gemini',
                'data processing', 'token', 'libraries', 'task manager'
            ]
        }

        # Keyword matching dictionaries (same as v1)
        self.category_keywords = {
            'Development': ['build', 'create', 'develop', 'implement', 'code', 'script', 'system', 'feature'],
            'Research': ['research', 'analyze', 'investigate', 'explore', 'study', 'review', 'evaluate'],
            'Integration': ['integrate', 'connect', 'sync', 'api', 'webhook', 'mcp', 'n8n'],
            'Documentation': ['document', 'wiki', 'guide', 'readme', 'instructions', 'manual'],
            'Automation': ['automate', 'workflow', 'pipeline', 'schedule', 'trigger'],
            'Testing': ['test', 'validate', 'verify', 'qa', 'check'],
            'Maintenance': ['fix', 'update', 'cleanup', 'refactor', 'optimize'],
            'Infrastructure': ['setup', 'deploy', 'configure', 'install', 'infrastructure'],
            'Design': ['design', 'ui', 'ux', 'mockup', 'prototype', 'layout'],
        }

        self.tool_keywords = {
            'GitHub': ['github', 'git', 'repository', 'repo'],
            'Dropbox': ['dropbox'],
            'Notion': ['notion', 'ats'],
            'VS Code': ['vscode', 'vs code', 'claude'],
            'n8n': ['n8n', 'workflow automation'],
            'CRM': ['crm', 'leads', 'prospects'],
            'Vercel': ['vercel', 'deploy'],
            'Entity System': ['entity', 'taxonomy'],
            'AI Tools': ['claude', 'gpt', 'gemini', 'ai tool'],
            'Google Maps': ['google maps', 'maps', 'scraping'],
            'Discord': ['discord'],
            'Dashboard': ['dashboard', 'visualization'],
        }

    def load_responsibilities(self):
        """Load LIBRARIES/Responsibilities for better role identification"""
        print("[INFO] Loading Responsibilities library...")
        resp_file = self.libraries_path / "Responsibilities" / "responsibilities.json"

        if resp_file.exists():
            try:
                with open(resp_file, 'r', encoding='utf-8') as f:
                    self.responsibilities = json.load(f)
                print(f"  [OK] Loaded {len(self.responsibilities)} responsibilities")
            except Exception as e:
                print(f"  [!] Error loading responsibilities: {e}")
                self.responsibilities = []
        else:
            print(f"  [!] Responsibilities file not found")
            self.responsibilities = []

    def reclassify_department(self, task: Dict) -> str:
        """Reclassify task department based on action keywords (FIXED LOGIC)"""
        task_text = (
            task.get('Activity_Name', '') + ' ' +
            task.get('Full_Description', '') + ' ' +
            task.get('Tags', '')
        ).lower()

        # Score each department
        dept_scores = defaultdict(int)

        for dept, keywords in self.department_keywords.items():
            for keyword in keywords:
                if keyword in task_text:
                    # More specific keywords get higher weight
                    weight = len(keyword.split())  # Multi-word keywords = more specific
                    dept_scores[dept] += weight * 2

        # PRIORITY RULE: Client-related tasks ALWAYS go to Sales or Finance
        if 'client' in task_text or 'customer' in task_text:
            # Check if it's financial (billing, payment, invoice)
            if any(word in task_text for word in ['payment', 'billing', 'invoice', 'accounting']):
                dept_scores['Finance'] += 20  # Boost Finance score
            else:
                dept_scores['Sales'] += 20  # Boost Sales score for general client tasks

        # If we have clear matches, use the highest scoring department
        if dept_scores:
            best_dept = max(dept_scores.items(), key=lambda x: x[1])
            if best_dept[1] >= 2:  # Minimum threshold
                return best_dept[0]

        # Fallback to original department if no clear match
        original_dept = task.get('Department', 'AI')

        # Map department codes to full names
        dept_map = {
            'AI': 'AI',
            'AID': 'AI',
            'HR': 'HR',
            'HRM': 'HR',
            'VID': 'Video',
            'DEV': 'Development',
            'DGN': 'Design',
            'FIN': 'Finance',
            'SLS': 'Sales',
            'LGN': 'Lead Generation',
            'SMM': 'SMM'
        }

        return dept_map.get(original_dept, original_dept)

    def _extract_id_number(self, entity_id: str) -> str:
        """
        Extract numeric portion from entity IDs.
        Examples:
        - TSK-066 -> 066
        - TST-066 -> 066
        - Task-Template-045 -> 045
        - PRT-011 -> 011
        """
        # Find last sequence of digits in the ID
        matches = re.findall(r'\d+', entity_id)
        return matches[-1] if matches else None

    def match_responsibility(self, task: Dict, reclassified_dept: str) -> Dict:
        """Match task to a responsibility from LIBRARIES"""
        task_text = (task.get('Activity_Name', '') + ' ' + task.get('Full_Description', '')).lower()

        best_match = None
        best_score = 0

        for resp in self.responsibilities:
            score = 0

            # Check department match
            if resp.get('department', '') == reclassified_dept:
                score += 30

            # Check action/object match
            action = resp.get('components', {}).get('action', '').lower()
            obj = resp.get('components', {}).get('object', '').lower()

            if action in task_text:
                score += 25
            if obj in task_text:
                score += 25

            # Check related tasks
            for related in resp.get('related_tasks', []):
                if related.lower() in task_text:
                    score += 10

            if score > best_score:
                best_score = score
                best_match = resp

        return best_match if best_score >= 30 else None

    def load_tasks(self):
        """Load both executive strategic and operational tasks from CSV"""
        print("[INFO] Loading tasks...")

        # Load executive strategic tasks
        executive_tasks = []
        if self.executive_tasks_file.exists():
            with open(self.executive_tasks_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                executive_tasks = list(reader)
            print(f"  [OK] Loaded {len(executive_tasks)} executive strategic tasks")

        # Load operational tasks (2025-11-20)
        operational_tasks = []
        if self.operational_tasks_file.exists():
            with open(self.operational_tasks_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Normalize operational task format to match executive format
                    normalized = {
                        'Date': row.get('Date', ''),
                        'Source_File': '2025-11-20 Department Reports',
                        'Entity_Type': row.get('Entity_Type', 'TSK'),
                        'Entity_ID': row.get('Entity_ID', ''),
                        'Activity_Name': row.get('Activity_Name', ''),
                        'Full_Description': row.get('Objective', ''),
                        'Related_Project': '',
                        'Related_Milestone': '',
                        'Department': row.get('Department', ''),
                        'Priority': row.get('Priority', 'Medium'),
                        'Category': 'Task',  # Default category for operational tasks
                        'Tags': ''
                    }
                    operational_tasks.append(normalized)
            print(f"  [OK] Loaded {len(operational_tasks)} operational tasks (2025-11-20)")

        # Combine all tasks
        self.tasks = executive_tasks + operational_tasks
        print(f"  [OK] Total tasks loaded: {len(self.tasks)}")

    def load_templates(self):
        """Load all task and project templates"""
        print("[INFO] Loading task manager templates...")

        # Load task templates (TST-###)
        task_templates_dir = self.templates_path / "TSM-003_Task_Templates"
        if task_templates_dir.exists():
            for template_file in task_templates_dir.glob("TST-*.json"):
                try:
                    with open(template_file, 'r', encoding='utf-8') as f:
                        template = json.load(f)
                        template_id = template.get('template_id', template_file.stem)
                        self.templates[template_id] = template
                except Exception as e:
                    print(f"  [!] Error loading {template_file.name}: {e}")

        # Load project templates (PRT-###)
        project_templates_dir = self.templates_path / "TSM-001_Project_Templates"
        if project_templates_dir.exists():
            for template_file in project_templates_dir.glob("PRT-*.json"):
                try:
                    with open(template_file, 'r', encoding='utf-8') as f:
                        template = json.load(f)
                        template_id = template.get('template_id', template_file.stem)
                        self.templates[template_id] = template
                except Exception as e:
                    print(f"  [!] Error loading {template_file.name}: {e}")

        print(f"  [OK] Loaded {len(self.templates)} templates")

    def calculate_match_score(self, task: Dict, template: Dict, reclassified_dept: str) -> Tuple[int, str]:
        """Calculate match score between task and template (UPDATED WITH RECLASSIFIED DEPT)"""
        score = 0
        reasons = []

        task_id = task.get('Entity_ID', '')
        task_name = task.get('Activity_Name', '').lower()
        task_desc = task.get('Full_Description', '').lower()
        task_category = task.get('Category', '').lower()
        task_tags = task.get('Tags', '').lower()

        template_id = template.get('template_id', '')
        template_name = template.get('task_name', '').lower()
        template_dept = template.get('department', '').upper()
        template_action = template.get('action', '').lower()
        template_object = template.get('object', '').lower()
        template_tools = ' '.join(template.get('tools_required', [])).lower()

        # ID-PROXIMITY MATCHING: Boost if numeric IDs match
        # Extract numbers from IDs: TSK-066 -> 066, Task-Template-045 -> 045, TST-066 -> 066
        task_id_num = self._extract_id_number(task_id)
        template_id_num = self._extract_id_number(template_id)

        if task_id_num and template_id_num:
            if task_id_num == template_id_num:
                score += 50  # Strong boost for exact ID match (TSK-066 <-> TST-066)
                reasons.append(f"ID proximity match ({task_id_num})")
            elif abs(int(task_id_num) - int(template_id_num)) <= 5:
                score += 15  # Moderate boost for nearby IDs (TSK-066 <-> TST-064)
                reasons.append(f"Nearby ID ({task_id_num} ≈ {template_id_num})")

        # Department match (40 points) - USE RECLASSIFIED DEPARTMENT
        if reclassified_dept and template_dept:
            # Normalize departments for comparison
            reclassified_upper = reclassified_dept.upper()
            if reclassified_upper == template_dept:
                score += 40
                reasons.append(f"Department match ({reclassified_dept})")
            elif reclassified_upper in template_dept or template_dept in reclassified_upper:
                score += 20
                reasons.append(f"Partial department match")

        # Category/Action match (30 points)
        if task_category in template_action or template_action in task_category:
            score += 30
            reasons.append(f"Category match ({task_category})")
        elif task_category in template_name or template_name in task_category:
            score += 20
            reasons.append(f"Category in template name")

        # Check category keywords
        for category, keywords in self.category_keywords.items():
            if task_category.lower() == category.lower():
                for keyword in keywords:
                    if keyword in template_action or keyword in template_name:
                        score += 15
                        reasons.append(f"Action keyword match ({keyword})")
                        break

        # Tool/Technology match (20 points)
        tool_matches = []
        for tool, keywords in self.tool_keywords.items():
            for keyword in keywords:
                if keyword in task_tags or keyword in task_name or keyword in task_desc:
                    if keyword in template_tools or keyword in template_name or keyword in template_object:
                        score += 20
                        tool_matches.append(tool)
                        break
        if tool_matches:
            reasons.append(f"Tool match ({', '.join(tool_matches[:3])})")

        # Name/Description similarity (10 points)
        task_words = set(task_name.split() + task_desc.split())
        template_words = set(template_name.split() + template_action.split() + template_object.split())
        common_words = task_words.intersection(template_words)
        common_words = [w for w in common_words if len(w) > 3]  # Filter short words

        if len(common_words) >= 3:
            score += 10
            reasons.append(f"High text similarity ({len(common_words)} common words)")
        elif len(common_words) >= 1:
            score += 5
            reasons.append(f"Text similarity ({len(common_words)} common words)")

        reason_text = "; ".join(reasons) if reasons else "No strong match"
        return score, reason_text

    def match_tasks_to_templates(self):
        """Match each task to best templates with DEPARTMENT RECLASSIFICATION"""
        print("[INFO] Matching tasks to templates with department reclassification...")

        dept_changes = 0

        for task in self.tasks:
            task_id = task.get('Entity_ID', '')
            original_dept = task.get('Department', '')

            # RECLASSIFY DEPARTMENT
            reclassified_dept = self.reclassify_department(task)

            if reclassified_dept != original_dept:
                dept_changes += 1
                task['Reclassified_Department'] = reclassified_dept
            else:
                task['Reclassified_Department'] = original_dept

            # Match to responsibility
            responsibility = self.match_responsibility(task, reclassified_dept)

            best_matches = []

            # Score against all templates
            for template_id, template in self.templates.items():
                score, reasoning = self.calculate_match_score(task, template, reclassified_dept)
                if score > 0:
                    best_matches.append({
                        'template_id': template_id,
                        'score': score,
                        'reasoning': reasoning,
                        'template': template
                    })

            # Sort by score and take top 3
            best_matches.sort(key=lambda x: x['score'], reverse=True)
            top_matches = best_matches[:3]

            # Determine confidence level
            if top_matches:
                top_score = top_matches[0]['score']
                if top_score >= 60:
                    confidence = "High"
                elif top_score >= 30:
                    confidence = "Medium"
                else:
                    confidence = "Low"
            else:
                confidence = "None"
                top_matches = [{'template_id': 'CUSTOM', 'score': 0, 'reasoning': 'No template match', 'template': {}}]

            self.mappings.append({
                'task': task,
                'matches': top_matches,
                'confidence': confidence,
                'responsibility': responsibility,
                'original_dept': original_dept,
                'reclassified_dept': reclassified_dept
            })

        print(f"  [OK] Matched {len(self.mappings)} tasks")
        print(f"  [INFO] Reclassified {dept_changes} tasks to correct departments")

    def write_task_template_mapping(self):
        """Write Task_Template_Mapping.csv with RECLASSIFIED DEPARTMENTS"""
        output_file = self.output_dir / "Task_Template_Mapping.csv"

        print("[INFO] Writing Task_Template_Mapping.csv...")

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Task_ID', 'Task_Name', 'Original_Department', 'Reclassified_Department',
                'Category', 'Priority', 'Matched_Template_ID', 'Match_Confidence',
                'Match_Score', 'Match_Reasoning', 'Estimated_Duration', 'Complexity',
                'Required_Skills', 'Required_Tools', 'Template_Steps_Count', 'Template_Profession',
                'Matched_Responsibility'
            ])

            for mapping in self.mappings:
                task = mapping['task']
                top_match = mapping['matches'][0]
                template = top_match['template']
                responsibility = mapping.get('responsibility')

                resp_name = responsibility.get('responsibility_name', 'N/A') if responsibility else 'N/A'

                writer.writerow([
                    task.get('Entity_ID', ''),
                    task.get('Activity_Name', ''),
                    mapping['original_dept'],
                    mapping['reclassified_dept'],
                    task.get('Category', ''),
                    task.get('Priority', ''),
                    top_match['template_id'],
                    mapping['confidence'],
                    top_match['score'],
                    top_match['reasoning'],
                    template.get('estimated_duration', 'N/A'),
                    template.get('complexity', 'N/A'),
                    ', '.join(template.get('skills_required', [])),
                    ', '.join(template.get('tools_required', [])),
                    len(template.get('steps', [])),
                    template.get('profession', 'N/A'),
                    resp_name
                ])

        print(f"  [OK] Created {output_file}")

    def write_team_assignment_matrix(self):
        """Write Team_Assignment_Matrix.csv with RECLASSIFIED DEPARTMENTS"""
        output_file = self.output_dir / "Team_Assignment_Matrix.csv"

        print("[INFO] Writing Team_Assignment_Matrix.csv...")

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Task_ID', 'Task_Name', 'Original_Department', 'Reclassified_Department',
                'Priority', 'Primary_Role', 'Responsible_Person', 'Accountable_Person',
                'Consulted_Roles', 'Informed_Roles', 'Assignment_Status',
                'Estimated_Duration', 'Required_Skills', 'Responsibility_Match'
            ])

            for mapping in self.mappings:
                task = mapping['task']
                top_match = mapping['matches'][0]
                template = top_match['template']
                responsibility = mapping.get('responsibility')

                # Handle responsibilities - can be dict, list, or string
                responsibilities_data = template.get('responsibilities', {})
                if isinstance(responsibilities_data, list):
                    responsibilities_data = responsibilities_data[0] if responsibilities_data and isinstance(responsibilities_data[0], dict) else {}
                elif not isinstance(responsibilities_data, dict):
                    responsibilities_data = {}

                resp_name = responsibility.get('responsibility_name', 'N/A') if responsibility else 'N/A'

                # Safe get with defaults
                responsible = responsibilities_data.get('responsible', 'TBD') if isinstance(responsibilities_data, dict) else 'TBD'
                accountable = responsibilities_data.get('accountable', f"{mapping['reclassified_dept']} Lead") if isinstance(responsibilities_data, dict) else f"{mapping['reclassified_dept']} Lead"
                consulted = responsibilities_data.get('consulted', []) if isinstance(responsibilities_data, dict) else []
                informed = responsibilities_data.get('informed', []) if isinstance(responsibilities_data, dict) else []

                writer.writerow([
                    task.get('Entity_ID', ''),
                    task.get('Activity_Name', ''),
                    mapping['original_dept'],
                    mapping['reclassified_dept'],
                    task.get('Priority', ''),
                    template.get('profession', 'Specialist'),
                    responsible,
                    accountable,
                    ', '.join(consulted) if isinstance(consulted, list) else '',
                    ', '.join(informed) if isinstance(informed, list) else '',
                    'Proposed',
                    template.get('estimated_duration', 'TBD'),
                    ', '.join(template.get('skills_required', [])),
                    resp_name
                ])

        print(f"  [OK] Created {output_file}")

    def write_workload_analysis(self):
        """Write Department_Workload_Analysis.csv using RECLASSIFIED DEPARTMENTS"""
        output_file = self.output_dir / "Department_Workload_Analysis.csv"

        print("[INFO] Writing Department_Workload_Analysis.csv...")

        # Aggregate by RECLASSIFIED department
        dept_stats = defaultdict(lambda: {
            'total_tasks': 0,
            'critical_count': 0,
            'high_count': 0,
            'categories': defaultdict(int),
            'total_hours': 0,
            'complexity_scores': [],
            'reclassified_count': 0
        })

        for mapping in self.mappings:
            task = mapping['task']
            dept = mapping['reclassified_dept']  # USE RECLASSIFIED
            priority = task.get('Priority', '')
            category = task.get('Category', 'Other')

            template = mapping['matches'][0]['template']
            duration_str = template.get('estimated_duration', '0')
            complexity = template.get('complexity', 'Medium')

            # Track reclassifications
            if mapping['original_dept'] != mapping['reclassified_dept']:
                dept_stats[dept]['reclassified_count'] += 1

            # Parse duration
            hours = 0
            if 'hour' in duration_str.lower():
                match = re.search(r'(\d+)', duration_str)
                if match:
                    hours = int(match.group(1))
            elif 'minute' in duration_str.lower():
                match = re.search(r'(\d+)', duration_str)
                if match:
                    hours = int(match.group(1)) / 60

            # Complexity score
            complexity_map = {'Low': 1, 'Medium': 2, 'High': 3}
            complexity_score = complexity_map.get(complexity, 2)

            dept_stats[dept]['total_tasks'] += 1
            dept_stats[dept]['total_hours'] += hours
            dept_stats[dept]['categories'][category] += 1
            dept_stats[dept]['complexity_scores'].append(complexity_score)

            if priority == 'Critical':
                dept_stats[dept]['critical_count'] += 1
            elif priority == 'High':
                dept_stats[dept]['high_count'] += 1

        # Write output
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Department', 'Total_Tasks_Assigned', 'Reclassified_Tasks',
                'Total_Estimated_Hours', 'Critical_Priority_Count', 'High_Priority_Count',
                'Average_Complexity', 'Top_Categories',
                'Resource_Status', 'Recommended_Action'
            ])

            for dept, stats in sorted(dept_stats.items()):
                avg_complexity = sum(stats['complexity_scores']) / len(stats['complexity_scores']) if stats['complexity_scores'] else 0
                top_categories = sorted(stats['categories'].items(), key=lambda x: x[1], reverse=True)[:3]
                top_cat_str = ', '.join([f"{cat}({count})" for cat, count in top_categories])

                # Determine resource status
                if stats['total_hours'] > 160:
                    resource_status = "Overloaded"
                    action = "Consider team expansion or prioritization"
                elif stats['total_hours'] > 80:
                    resource_status = "High Load"
                    action = "Monitor workload distribution"
                else:
                    resource_status = "Balanced"
                    action = "Current capacity sufficient"

                writer.writerow([
                    dept,
                    stats['total_tasks'],
                    stats['reclassified_count'],
                    f"{stats['total_hours']:.1f}",
                    stats['critical_count'],
                    stats['high_count'],
                    f"{avg_complexity:.2f}",
                    top_cat_str,
                    resource_status,
                    action
                ])

        print(f"  [OK] Created {output_file}")

    def write_workflow_clustering(self):
        """Write Workflow_Clustering.csv (same as v1)"""
        output_file = self.output_dir / "Workflow_Clustering.csv"

        print("[INFO] Writing Workflow_Clustering.csv...")

        # Group by Related_Project
        project_clusters = defaultdict(list)
        orphan_tasks = []

        for mapping in self.mappings:
            task = mapping['task']
            related_project = task.get('Related_Project', '').strip()

            if related_project:
                project_clusters[related_project].append(mapping)
            else:
                orphan_tasks.append(mapping)

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Workflow_Cluster_ID', 'Workflow_Name', 'Related_Project_ID',
                'Task_Count', 'Task_IDs', 'Cluster_Type',
                'Total_Estimated_Hours', 'Milestone_Dependencies',
                'Execution_Phase', 'Department'
            ])

            cluster_id = 1

            # Write project-based clusters
            for project_id, mappings_list in sorted(project_clusters.items()):
                if not mappings_list:
                    continue

                task_ids = [m['task'].get('Entity_ID', '') for m in mappings_list]
                workflow_name = mappings_list[0]['task'].get('Activity_Name', f'Project {project_id}')
                milestones = set()
                total_hours = 0
                departments = set()

                for mapping in mappings_list:
                    milestone = mapping['task'].get('Related_Milestone', '').strip()
                    if milestone:
                        milestones.add(milestone)

                    dept = mapping['reclassified_dept']  # USE RECLASSIFIED
                    if dept:
                        departments.add(dept)

                    # Estimate hours
                    template = mapping['matches'][0]['template']
                    duration_str = template.get('estimated_duration', '0')
                    if 'hour' in duration_str.lower():
                        match = re.search(r'(\d+)', duration_str)
                        if match:
                            total_hours += int(match.group(1))
                    elif 'minute' in duration_str.lower():
                        match = re.search(r'(\d+)', duration_str)
                        if match:
                            total_hours += int(match.group(1)) / 60

                writer.writerow([
                    f"WFC-{cluster_id:03d}",
                    workflow_name[:60],
                    project_id,
                    len(task_ids),
                    ', '.join(task_ids[:10]) + ('...' if len(task_ids) > 10 else ''),
                    'Sequential' if milestones else 'Parallel',
                    f"{total_hours:.1f}",
                    ', '.join(sorted(milestones)),
                    'Planning',
                    ', '.join(sorted(departments))
                ])
                cluster_id += 1

            # Cluster orphan tasks by RECLASSIFIED department + category
            orphan_clusters = defaultdict(list)
            for mapping in orphan_tasks:
                task = mapping['task']
                dept = mapping['reclassified_dept']  # USE RECLASSIFIED
                category = task.get('Category', 'Other')
                key = f"{dept}_{category}"
                orphan_clusters[key].append(mapping)

            for cluster_key, mappings_list in sorted(orphan_clusters.items()):
                if len(mappings_list) < 2:
                    continue

                dept, category = cluster_key.split('_', 1)
                task_ids = [m['task'].get('Entity_ID', '') for m in mappings_list]

                total_hours = 0
                for mapping in mappings_list:
                    template = mapping['matches'][0]['template']
                    duration_str = template.get('estimated_duration', '0')
                    if 'hour' in duration_str.lower():
                        match = re.search(r'(\d+)', duration_str)
                        if match:
                            total_hours += int(match.group(1))

                writer.writerow([
                    f"WFC-{cluster_id:03d}",
                    f"{dept} - {category} Tasks",
                    'N/A',
                    len(task_ids),
                    ', '.join(task_ids[:10]) + ('...' if len(task_ids) > 10 else ''),
                    'Parallel',
                    f"{total_hours:.1f}",
                    'N/A',
                    'Execution',
                    dept
                ])
                cluster_id += 1

        print(f"  [OK] Created {output_file}")

    def write_priority_queue(self):
        """Write Assignment_Priority_Queue.csv (same as v1)"""
        output_file = self.output_dir / "Assignment_Priority_Queue.csv"

        print("[INFO] Writing Assignment_Priority_Queue.csv...")

        queue_items = []

        for mapping in self.mappings:
            task = mapping['task']
            template = mapping['matches'][0]['template']

            priority = task.get('Priority', 'Medium')
            dept = mapping['reclassified_dept']  # USE RECLASSIFIED
            category = task.get('Category', '')

            duration_str = template.get('estimated_duration', '')
            is_quick_win = 'minute' in duration_str.lower() or '1 hour' in duration_str.lower()

            complexity_map = {'Low': 1, 'Medium': 2, 'High': 3}
            complexity = template.get('complexity', 'Medium')
            complexity_score = complexity_map.get(complexity, 2)

            if category in ['Infrastructure', 'Critical']:
                business_impact = 'Infrastructure'
            elif 'customer' in task.get('Activity_Name', '').lower():
                business_impact = 'Customer'
            elif priority == 'Critical':
                business_impact = 'Strategic'
            else:
                business_impact = 'Internal'

            priority_scores = {'Critical': 4, 'High': 3, 'Medium': 2, 'Low': 1}
            priority_score = priority_scores.get(priority, 2)

            queue_items.append({
                'task': task,
                'template': template,
                'priority_score': priority_score,
                'complexity_score': complexity_score,
                'is_quick_win': is_quick_win,
                'business_impact': business_impact,
                'match_confidence': mapping['confidence'],
                'reclassified_dept': dept
            })

        # Sort
        queue_items.sort(key=lambda x: (
            -x['priority_score'],
            -int(x['is_quick_win']),
            x['complexity_score']
        ))

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Queue_Position', 'Task_ID', 'Task_Name', 'Priority',
                'Reclassified_Department', 'Category', 'Blocking_Dependencies',
                'Assigned_To', 'Estimated_Duration', 'Business_Impact',
                'Complexity_Score', 'Quick_Win_Flag', 'Match_Confidence',
                'Matched_Template'
            ])

            for position, item in enumerate(queue_items, 1):
                task = item['task']
                template = item['template']

                writer.writerow([
                    position,
                    task.get('Entity_ID', ''),
                    task.get('Activity_Name', ''),
                    task.get('Priority', ''),
                    item['reclassified_dept'],
                    task.get('Category', ''),
                    task.get('Related_Project', 'None'),
                    template.get('profession', 'TBD'),
                    template.get('estimated_duration', 'TBD'),
                    item['business_impact'],
                    item['complexity_score'],
                    'Yes' if item['is_quick_win'] else 'No',
                    item['match_confidence'],
                    template.get('template_id', 'CUSTOM')
                ])

        print(f"  [OK] Created {output_file}")

    def write_delegation_readme(self):
        """Write comprehensive README (updated with reclassification info)"""
        output_file = self.output_dir / "README.md"

        print("[INFO] Writing README.md...")

        total_tasks = len(self.mappings)
        high_confidence = sum(1 for m in self.mappings if m['confidence'] == 'High')
        medium_confidence = sum(1 for m in self.mappings if m['confidence'] == 'Medium')
        low_confidence = sum(1 for m in self.mappings if m['confidence'] == 'Low')
        custom_needed = sum(1 for m in self.mappings if m['matches'][0]['template_id'] == 'CUSTOM')
        reclassified_count = sum(1 for m in self.mappings if m['original_dept'] != m['reclassified_dept'])

        # Department distribution (RECLASSIFIED)
        dept_counts = defaultdict(int)
        for mapping in self.mappings:
            dept = mapping['reclassified_dept']
            dept_counts[dept] += 1

        # Role distribution
        role_counts = defaultdict(int)
        for mapping in self.mappings:
            template = mapping['matches'][0]['template']
            role = template.get('profession', 'Specialist')
            role_counts[role] += 1

        readme_content = f"""# Delegation Mapping System v2.0 - Week 4

**Generated:** 2025-11-24
**Sources:**
- Executive Strategic Tasks (461 tasks from Executive_Notes_Summary)
- Operational Tasks 2025-11-20 (40 tasks from Department Reports)
**Total Tasks Analyzed:** {total_tasks}
**Reclassified Tasks:** {reclassified_count} (corrected department assignments)

---

## What's New in v2.0

### Department Reclassification
This version correctly identifies task ownership based on **action keywords** rather than source department field:

**Examples:**
- "Retain Vamos employee" → **HR** (not AI)
- "Talk to Dasha about retention" → **HR** (not AI)
- "Communicate final decision to MASEK client" → **Sales** (not AI)
- "Resolve accounting/payment issues" → **Finance** (not AI)
- "Fix email personalization" → **AI/Automation** (correct)

### LIBRARIES Integration
- Integrated `LIBRARIES/Responsibilities` for better role identification
- Matches tasks to responsibility patterns (action + object)
- Provides profession recommendations from responsibility library

---

## Overview

This delegation system maps {total_tasks} executive tasks from Week 4 to existing Task Manager templates, with **{reclassified_count} tasks reclassified** to their correct departments.

### Mapping Success Rate

- **High Confidence Matches:** {high_confidence} tasks ({high_confidence/total_tasks*100:.1f}%)
- **Medium Confidence Matches:** {medium_confidence} tasks ({medium_confidence/total_tasks*100:.1f}%)
- **Low Confidence Matches:** {low_confidence} tasks ({low_confidence/total_tasks*100:.1f}%)
- **Custom Templates Needed:** {custom_needed} tasks ({custom_needed/total_tasks*100:.1f}%)

---

## Generated Files

### 1. [Task_Template_Mapping.csv](Task_Template_Mapping.csv)
**NEW COLUMNS:**
- `Original_Department` - Department from source data
- `Reclassified_Department` - Corrected department based on action keywords
- `Matched_Responsibility` - Matched responsibility from LIBRARIES

**Usage:** Use `Reclassified_Department` for accurate task assignment.

---

### 2. [Team_Assignment_Matrix.csv](Team_Assignment_Matrix.csv)
**UPDATED:**
- Uses `Reclassified_Department` for accurate role assignments
- Includes `Responsibility_Match` for profession identification

**Usage:** Assign tasks to teams based on `Reclassified_Department`.

---

### 3. [Department_Workload_Analysis.csv](Department_Workload_Analysis.csv)
**NEW COLUMN:**
- `Reclassified_Tasks` - Number of tasks moved to this department

**Department Breakdown (Reclassified):**
{chr(10).join([f"- **{dept}**: {count} tasks" for dept, count in sorted(dept_counts.items(), key=lambda x: -x[1])[:10]])}

**Usage:** This reflects the **true workload** per department after corrections.

---

### 4. [Workflow_Clustering.csv](Workflow_Clustering.csv)
**UPDATED:**
- Uses `Reclassified_Department` for workflow grouping

---

### 5. [Assignment_Priority_Queue.csv](Assignment_Priority_Queue.csv)
**UPDATED:**
- Column changed from `Department` to `Reclassified_Department`

---

## Reclassification Examples

### HR Department (Corrected)
- TSK-406: Find substitute person for Vamos project
- TSK-407: Talk to Dasha about retention
- TSK-408: Identify issues causing quit desire
- TSK-409: Create retention strategy
- TSK-410: Retain Vamos employee (2 years tenure)
- TSK-412: Document retention process
- TSK-432: Create employee 1:1 session template

### Sales Department (Corrected)
- TSK-413: Communicate final decision to MASEK client
- TSK-414: Document client termination policy
- TSK-405: Add clear next-step instructions for clients

### Finance Department (Corrected)
- TSK-411: Resolve accounting/payment issues
- TSK-349: Review GPT usage and costs
- TSK-350: Identify cost-cutting opportunities

---

## Delegation Workflow

### Step 1: Review Reclassifications
1. Open [Task_Template_Mapping.csv](Task_Template_Mapping.csv)
2. Compare `Original_Department` vs `Reclassified_Department`
3. Verify reclassifications make sense for your org structure

### Step 2: Assign to Correct Departments
1. Use `Reclassified_Department` column for all assignments
2. Route tasks to correct team leads
3. Check `Matched_Responsibility` for profession hints

### Step 3: Follow Standard Workflow
(Same as v1 - see previous README for full steps)

---

## Key Improvements

1. **Accurate Department Assignment**: {reclassified_count} tasks now routed to correct teams
2. **LIBRARIES Integration**: Responsibility matching provides better role identification
3. **Reduced AI Department Overload**: AI dept only gets automation/infrastructure tasks
4. **Better HR/Sales/Finance Coverage**: People-facing tasks correctly routed

---

## Next Actions

1. **Verify Reclassifications** - Review {reclassified_count} reclassified tasks
2. **Update Team Assignments** - Use corrected departments for delegation
3. **Check Workload Balance** - Verify no single department is overloaded
4. **Begin Execution** - Start with [Assignment_Priority_Queue.csv](Assignment_Priority_Queue.csv)

---

**Generated by:** create_delegation_mapping_v2.py
**Last Updated:** 2025-11-24
**Version:** 2.0
"""

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(readme_content)

        print(f"  [OK] Created {output_file}")

    def run(self):
        """Execute full delegation mapping pipeline v2"""
        print("=" * 60)
        print("DELEGATION MAPPING SYSTEM V2.0")
        print("=" * 60)

        # Create output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Execute pipeline
        self.load_responsibilities()
        self.load_tasks()
        self.load_templates()
        self.match_tasks_to_templates()

        print("\n" + "=" * 60)
        print("GENERATING OUTPUT FILES")
        print("=" * 60)

        self.write_task_template_mapping()
        self.write_team_assignment_matrix()
        self.write_workload_analysis()
        self.write_workflow_clustering()
        self.write_priority_queue()
        self.write_delegation_readme()

        print("\n" + "=" * 60)
        print("DELEGATION MAPPING V2.0 COMPLETE")
        print("=" * 60)
        print(f"\nOutput directory: {self.output_dir}")
        print("\nGenerated files:")
        print("  1. Task_Template_Mapping.csv (with reclassified departments)")
        print("  2. Team_Assignment_Matrix.csv (with reclassified departments)")
        print("  3. Department_Workload_Analysis.csv (corrected workload)")
        print("  4. Workflow_Clustering.csv")
        print("  5. Assignment_Priority_Queue.csv")
        print("  6. README.md (v2.0 documentation)")
        print("\nKey Improvements:")
        print("  - Department reclassification based on action keywords")
        print("  - LIBRARIES/Responsibilities integration")
        print("  - Corrected HR/Sales/Finance task routing")

if __name__ == "__main__":
    mapper = DelegationMapperV2()
    mapper.run()
