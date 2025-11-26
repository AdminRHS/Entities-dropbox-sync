"""
Delegation Mapping System
Creates comprehensive task-to-template mappings and team assignments for Week 4 executive tasks.

Output Files:
1. Task_Template_Mapping.csv - Task-to-template matches with confidence scores
2. Team_Assignment_Matrix.csv - RACI-based role assignments
3. Department_Workload_Analysis.csv - Workload distribution by department
4. Workflow_Clustering.csv - Task grouping by projects and workflows
5. Assignment_Priority_Queue.csv - Priority-sorted assignment queue

Author: AI Assistant
Date: 2025-11-24
"""

import csv
import json
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple

class DelegationMapper:
    def __init__(self):
        self.base_path = Path(r"C:\Users\Dell\Dropbox\ENTITIES")
        self.tasks_file = self.base_path / "DAILIES" / "REPORTS" / "Week_4" / "Executive_Strategic" / "Executive_All_Tasks.csv"
        self.templates_path = self.base_path / "TASK_MANAGERS"
        self.output_dir = self.base_path / "DAILIES" / "REPORTS" / "Week_4" / "Delegation"

        self.tasks = []
        self.templates = {}
        self.mappings = []

        # Keyword matching dictionaries
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

    def load_tasks(self):
        """Load executive tasks from CSV"""
        print("[INFO] Loading executive tasks...")
        with open(self.tasks_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.tasks = list(reader)
        print(f"  [OK] Loaded {len(self.tasks)} tasks")

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

    def calculate_match_score(self, task: Dict, template: Dict) -> Tuple[int, str]:
        """Calculate match score between task and template"""
        score = 0
        reasons = []

        task_name = task.get('Activity_Name', '').lower()
        task_desc = task.get('Full_Description', '').lower()
        task_dept = task.get('Department', '').upper()
        task_category = task.get('Category', '').lower()
        task_tags = task.get('Tags', '').lower()

        template_name = template.get('task_name', '').lower()
        template_dept = template.get('department', '').upper()
        template_action = template.get('action', '').lower()
        template_object = template.get('object', '').lower()
        template_tools = ' '.join(template.get('tools_required', [])).lower()

        # Department match (40 points)
        if task_dept and template_dept and task_dept == template_dept:
            score += 40
            reasons.append(f"Department match ({task_dept})")
        elif task_dept and template_dept:
            # Partial department matching (AI can match with AID, etc.)
            if task_dept in template_dept or template_dept in task_dept:
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
        """Match each task to best templates"""
        print("[INFO] Matching tasks to templates...")

        for task in self.tasks:
            task_id = task.get('Entity_ID', '')
            best_matches = []

            # Score against all templates
            for template_id, template in self.templates.items():
                score, reasoning = self.calculate_match_score(task, template)
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
                'confidence': confidence
            })

        print(f"  [OK] Matched {len(self.mappings)} tasks")

    def write_task_template_mapping(self):
        """Write Task_Template_Mapping.csv"""
        output_file = self.output_dir / "Task_Template_Mapping.csv"

        print("[INFO] Writing Task_Template_Mapping.csv...")

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Task_ID', 'Task_Name', 'Department', 'Category', 'Priority',
                'Matched_Template_ID', 'Match_Confidence', 'Match_Score', 'Match_Reasoning',
                'Estimated_Duration', 'Complexity', 'Required_Skills', 'Required_Tools',
                'Template_Steps_Count', 'Template_Profession'
            ])

            for mapping in self.mappings:
                task = mapping['task']
                top_match = mapping['matches'][0]
                template = top_match['template']

                writer.writerow([
                    task.get('Entity_ID', ''),
                    task.get('Activity_Name', ''),
                    task.get('Department', ''),
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
                    template.get('profession', 'N/A')
                ])

        print(f"  [OK] Created {output_file}")

    def write_team_assignment_matrix(self):
        """Write Team_Assignment_Matrix.csv with RACI assignments"""
        output_file = self.output_dir / "Team_Assignment_Matrix.csv"

        print("[INFO] Writing Team_Assignment_Matrix.csv...")

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Task_ID', 'Task_Name', 'Department', 'Priority',
                'Primary_Role', 'Responsible_Person', 'Accountable_Person',
                'Consulted_Roles', 'Informed_Roles',
                'Assignment_Status', 'Estimated_Duration', 'Required_Skills'
            ])

            for mapping in self.mappings:
                task = mapping['task']
                top_match = mapping['matches'][0]
                template = top_match['template']

                responsibilities = template.get('responsibilities', {})

                writer.writerow([
                    task.get('Entity_ID', ''),
                    task.get('Activity_Name', ''),
                    task.get('Department', ''),
                    task.get('Priority', ''),
                    template.get('profession', 'Specialist'),
                    responsibilities.get('responsible', 'TBD'),
                    responsibilities.get('accountable', 'Department Lead'),
                    ', '.join(responsibilities.get('consulted', [])),
                    ', '.join(responsibilities.get('informed', [])),
                    'Proposed',
                    template.get('estimated_duration', 'TBD'),
                    ', '.join(template.get('skills_required', []))
                ])

        print(f"  [OK] Created {output_file}")

    def write_workload_analysis(self):
        """Write Department_Workload_Analysis.csv"""
        output_file = self.output_dir / "Department_Workload_Analysis.csv"

        print("[INFO] Writing Department_Workload_Analysis.csv...")

        # Aggregate by department
        dept_stats = defaultdict(lambda: {
            'total_tasks': 0,
            'critical_count': 0,
            'high_count': 0,
            'categories': defaultdict(int),
            'total_hours': 0,
            'complexity_scores': []
        })

        for mapping in self.mappings:
            task = mapping['task']
            dept = task.get('Department', 'Unknown')
            priority = task.get('Priority', '')
            category = task.get('Category', 'Other')

            template = mapping['matches'][0]['template']
            duration_str = template.get('estimated_duration', '0')
            complexity = template.get('complexity', 'Medium')

            # Parse duration (e.g., "20-30 minutes", "2-3 hours")
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
                'Department', 'Total_Tasks_Assigned', 'Total_Estimated_Hours',
                'Critical_Priority_Count', 'High_Priority_Count',
                'Average_Complexity', 'Top_Categories',
                'Resource_Status', 'Recommended_Action'
            ])

            for dept, stats in sorted(dept_stats.items()):
                avg_complexity = sum(stats['complexity_scores']) / len(stats['complexity_scores']) if stats['complexity_scores'] else 0
                top_categories = sorted(stats['categories'].items(), key=lambda x: x[1], reverse=True)[:3]
                top_cat_str = ', '.join([f"{cat}({count})" for cat, count in top_categories])

                # Determine resource status
                if stats['total_hours'] > 160:  # More than 1 month of work
                    resource_status = "Overloaded"
                    action = "Consider team expansion or prioritization"
                elif stats['total_hours'] > 80:  # 2-4 weeks
                    resource_status = "High Load"
                    action = "Monitor workload distribution"
                else:
                    resource_status = "Balanced"
                    action = "Current capacity sufficient"

                writer.writerow([
                    dept,
                    stats['total_tasks'],
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
        """Write Workflow_Clustering.csv"""
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

                    dept = mapping['task'].get('Department', '')
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

            # Cluster orphan tasks by department + category
            orphan_clusters = defaultdict(list)
            for mapping in orphan_tasks:
                task = mapping['task']
                dept = task.get('Department', 'Unknown')
                category = task.get('Category', 'Other')
                key = f"{dept}_{category}"
                orphan_clusters[key].append(mapping)

            for cluster_key, mappings_list in sorted(orphan_clusters.items()):
                if len(mappings_list) < 2:  # Skip single-task clusters
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
        """Write Assignment_Priority_Queue.csv"""
        output_file = self.output_dir / "Assignment_Priority_Queue.csv"

        print("[INFO] Writing Assignment_Priority_Queue.csv...")

        # Prepare queue items
        queue_items = []

        for mapping in self.mappings:
            task = mapping['task']
            template = mapping['matches'][0]['template']

            priority = task.get('Priority', 'Medium')
            dept = task.get('Department', '')
            category = task.get('Category', '')

            # Parse duration for quick win detection
            duration_str = template.get('estimated_duration', '')
            is_quick_win = 'minute' in duration_str.lower() or '1 hour' in duration_str.lower()

            # Complexity score
            complexity_map = {'Low': 1, 'Medium': 2, 'High': 3}
            complexity = template.get('complexity', 'Medium')
            complexity_score = complexity_map.get(complexity, 2)

            # Business impact
            if category in ['Infrastructure', 'Critical']:
                business_impact = 'Infrastructure'
            elif 'customer' in task.get('Activity_Name', '').lower():
                business_impact = 'Customer'
            elif priority == 'Critical':
                business_impact = 'Strategic'
            else:
                business_impact = 'Internal'

            # Priority score for sorting
            priority_scores = {'Critical': 4, 'High': 3, 'Medium': 2, 'Low': 1}
            priority_score = priority_scores.get(priority, 2)

            queue_items.append({
                'task': task,
                'template': template,
                'priority_score': priority_score,
                'complexity_score': complexity_score,
                'is_quick_win': is_quick_win,
                'business_impact': business_impact,
                'match_confidence': mapping['confidence']
            })

        # Sort: Priority DESC, Quick Wins first, Complexity ASC
        queue_items.sort(key=lambda x: (
            -x['priority_score'],  # Higher priority first
            -int(x['is_quick_win']),  # Quick wins first
            x['complexity_score']  # Simpler tasks first
        ))

        # Write output
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Queue_Position', 'Task_ID', 'Task_Name', 'Priority',
                'Department', 'Category', 'Blocking_Dependencies',
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
                    task.get('Department', ''),
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
        """Write comprehensive README for delegation system"""
        output_file = self.output_dir / "README.md"

        print("[INFO] Writing README.md...")

        # Calculate statistics
        total_tasks = len(self.mappings)
        high_confidence = sum(1 for m in self.mappings if m['confidence'] == 'High')
        medium_confidence = sum(1 for m in self.mappings if m['confidence'] == 'Medium')
        low_confidence = sum(1 for m in self.mappings if m['confidence'] == 'Low')
        custom_needed = sum(1 for m in self.mappings if m['matches'][0]['template_id'] == 'CUSTOM')

        # Department distribution
        dept_counts = defaultdict(int)
        for mapping in self.mappings:
            dept = mapping['task'].get('Department', 'Unknown')
            dept_counts[dept] += 1

        # Role distribution
        role_counts = defaultdict(int)
        for mapping in self.mappings:
            template = mapping['matches'][0]['template']
            role = template.get('profession', 'Specialist')
            role_counts[role] += 1

        readme_content = f"""# Delegation Mapping System - Week 4

**Generated:** 2025-11-24
**Source:** Executive Strategic Tasks (Week 4)
**Total Tasks Analyzed:** {total_tasks}

---

## Overview

This delegation system maps {total_tasks} executive tasks from Week 4 to existing Task Manager templates, providing comprehensive assignment recommendations, workload analysis, and priority queuing.

### Mapping Success Rate

- **High Confidence Matches:** {high_confidence} tasks ({high_confidence/total_tasks*100:.1f}%)
- **Medium Confidence Matches:** {medium_confidence} tasks ({medium_confidence/total_tasks*100:.1f}%)
- **Low Confidence Matches:** {low_confidence} tasks ({low_confidence/total_tasks*100:.1f}%)
- **Custom Templates Needed:** {custom_needed} tasks ({custom_needed/total_tasks*100:.1f}%)

---

## Generated Files

### 1. [Task_Template_Mapping.csv](Task_Template_Mapping.csv)
**Purpose:** Core mapping between executive tasks and Task Manager templates

**Key Fields:**
- `Task_ID` - Executive task identifier (TSK-###, PRT-###)
- `Matched_Template_ID` - Best matching template (TST-###, PRT-###)
- `Match_Confidence` - High/Medium/Low/None
- `Match_Score` - Numerical confidence (0-100)
- `Match_Reasoning` - Explanation of why this template fits
- `Estimated_Duration` - Time estimate from template
- `Required_Skills` - Skills needed from template
- `Required_Tools` - Tools needed from template

**Usage:** Use this file to understand which template to use for each task and why.

---

### 2. [Team_Assignment_Matrix.csv](Team_Assignment_Matrix.csv)
**Purpose:** RACI-based role assignments for each task

**Key Fields:**
- `Primary_Role` - Main role responsible (from template profession)
- `Responsible_Person` - Executor (from template RACI)
- `Accountable_Person` - Approver/Owner
- `Consulted_Roles` - Stakeholders to consult
- `Informed_Roles` - People to keep informed
- `Assignment_Status` - Current status (Proposed/Assigned/In-Progress/Complete)

**Usage:** Assign tasks to specific team members based on their roles and the RACI structure.

---

### 3. [Department_Workload_Analysis.csv](Department_Workload_Analysis.csv)
**Purpose:** Workload distribution and capacity analysis by department

**Key Fields:**
- `Total_Tasks_Assigned` - Number of tasks per department
- `Total_Estimated_Hours` - Sum of all task durations
- `Critical_Priority_Count` - Number of critical tasks
- `Average_Complexity` - Mean complexity score (1-3)
- `Resource_Status` - Overloaded/High Load/Balanced
- `Recommended_Action` - Suggestions for capacity management

**Department Breakdown:**
{chr(10).join([f"- **{dept}**: {count} tasks" for dept, count in sorted(dept_counts.items(), key=lambda x: -x[1])[:10]])}

**Usage:** Identify overburdened departments and plan resource allocation.

---

### 4. [Workflow_Clustering.csv](Workflow_Clustering.csv)
**Purpose:** Group related tasks into workflows and execution clusters

**Key Fields:**
- `Workflow_Cluster_ID` - Unique cluster identifier (WFC-###)
- `Related_Project_ID` - Parent project (PRT-###)
- `Task_Count` - Number of tasks in cluster
- `Cluster_Type` - Sequential (has milestones) or Parallel
- `Total_Estimated_Hours` - Combined duration
- `Execution_Phase` - Planning/Execution/Review

**Usage:** Understand task dependencies and plan sequential vs. parallel execution.

---

### 5. [Assignment_Priority_Queue.csv](Assignment_Priority_Queue.csv)
**Purpose:** Priority-sorted task queue for systematic assignment

**Sorting Logic:**
1. Priority (Critical > High > Medium > Low)
2. Quick Wins first (tasks <1 hour)
3. Complexity (simpler tasks first within same priority)

**Key Fields:**
- `Queue_Position` - Recommended execution order
- `Priority` - Business priority level
- `Blocking_Dependencies` - Prerequisites (Related_Project)
- `Business_Impact` - Infrastructure/Customer/Strategic/Internal
- `Quick_Win_Flag` - Yes/No for <1hr tasks
- `Match_Confidence` - Template match quality

**Usage:** Start from Queue_Position 1 and work down. Tackle quick wins early for momentum.

---

## Specialist Roles Needed

Based on template profession fields, you need the following specialists:

{chr(10).join([f"- **{role}**: {count} tasks" for role, count in sorted(role_counts.items(), key=lambda x: -x[1])[:12]])}

---

## Delegation Workflow

### Step 1: Review Mappings
1. Open [Task_Template_Mapping.csv](Task_Template_Mapping.csv)
2. Review High Confidence matches (score ≥60) - these are ready to delegate
3. Flag Medium/Low Confidence matches for manual review
4. Identify CUSTOM templates - these need new template creation

### Step 2: Assign to Team Members
1. Open [Team_Assignment_Matrix.csv](Team_Assignment_Matrix.csv)
2. Match `Primary_Role` to your team members
3. Use `Required_Skills` to verify team member capabilities
4. Update `Assigned_To` and `Assignment_Status` columns
5. Notify `Consulted_Roles` and `Informed_Roles`

### Step 3: Plan Capacity
1. Open [Department_Workload_Analysis.csv](Department_Workload_Analysis.csv)
2. Check `Resource_Status` for each department
3. For "Overloaded" departments:
   - Prioritize Critical tasks only
   - Consider hiring or contractor support
   - Defer Low priority tasks
4. Follow `Recommended_Action` for each department

### Step 4: Create Execution Plan
1. Open [Workflow_Clustering.csv](Workflow_Clustering.csv)
2. Identify Sequential clusters (must be done in order)
3. Identify Parallel clusters (can be done simultaneously)
4. Group clusters by `Execution_Phase`
5. Assign clusters to sprint cycles or project phases

### Step 5: Start Execution
1. Open [Assignment_Priority_Queue.csv](Assignment_Priority_Queue.csv)
2. Start with Queue_Position 1
3. Tackle "Quick Win" tasks first (build momentum)
4. Monitor `Blocking_Dependencies` - complete prerequisites first
5. Update status as tasks progress

---

## Key Insights

### High-Value Quick Wins
Filter `Assignment_Priority_Queue.csv` for:
- `Quick_Win_Flag` = Yes
- `Priority` = High or Critical
- `Match_Confidence` = High

These tasks provide immediate value with minimal time investment.

### Strategic Projects
Filter `Workflow_Clustering.csv` for:
- `Cluster_Type` = Sequential
- `Total_Estimated_Hours` > 20

These are major initiatives requiring project management and milestone tracking.

### Capacity Constraints
Check `Department_Workload_Analysis.csv` for:
- `Resource_Status` = Overloaded
- `Total_Estimated_Hours` > 160 (1 person-month)

These departments need immediate capacity planning.

---

## Customization Needed

### Tasks Requiring New Templates ({custom_needed} tasks)
These tasks scored too low to match existing templates. Review them to:
1. Create new Task Templates (TST-###)
2. Expand existing templates with new variations
3. Reclassify as variations of existing templates

**Recommendation:** Focus on creating templates for recurring custom tasks first.

---

## Next Actions

1. **Week 4 Kickoff Meeting**
   - Review [Assignment_Priority_Queue.csv](Assignment_Priority_Queue.csv) with team
   - Assign top 20 high-priority tasks
   - Identify blockers and dependencies

2. **Department Planning**
   - Each department lead reviews [Department_Workload_Analysis.csv](Department_Workload_Analysis.csv)
   - Adjust capacity or priorities as needed
   - Flag impossible deadlines early

3. **Template Development**
   - Create missing templates for {custom_needed} unmatched tasks
   - Improve low-confidence matches with template refinements

4. **Progress Tracking**
   - Update `Assignment_Status` in [Team_Assignment_Matrix.csv](Team_Assignment_Matrix.csv) daily
   - Monitor completion against [Assignment_Priority_Queue.csv](Assignment_Priority_Queue.csv)
   - Adjust priorities based on business needs

---

## Support & Questions

For questions about:
- **Template matching logic:** See `create_delegation_mapping.py` source code
- **RACI assignments:** Review original Task Manager templates in `C:\\Users\\Dell\\Dropbox\\ENTITIES\\TASK_MANAGERS`
- **Workload calculations:** Duration estimates come from template `estimated_duration` fields

---

**Generated by:** create_delegation_mapping.py
**Last Updated:** 2025-11-24
"""

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(readme_content)

        print(f"  [OK] Created {output_file}")

    def run(self):
        """Execute full delegation mapping pipeline"""
        print("=" * 60)
        print("DELEGATION MAPPING SYSTEM")
        print("=" * 60)

        # Create output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Execute pipeline
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
        print("DELEGATION MAPPING COMPLETE")
        print("=" * 60)
        print(f"\nOutput directory: {self.output_dir}")
        print("\nGenerated files:")
        print("  1. Task_Template_Mapping.csv")
        print("  2. Team_Assignment_Matrix.csv")
        print("  3. Department_Workload_Analysis.csv")
        print("  4. Workflow_Clustering.csv")
        print("  5. Assignment_Priority_Queue.csv")
        print("  6. README.md")
        print("\nNext: Review README.md for delegation workflow instructions")

if __name__ == "__main__":
    mapper = DelegationMapper()
    mapper.run()
