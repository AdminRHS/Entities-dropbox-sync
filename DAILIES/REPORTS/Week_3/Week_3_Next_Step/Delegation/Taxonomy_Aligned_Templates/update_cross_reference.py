import json
import os

def update_cross_reference():
    """Update cross-reference mapping with complete task template list"""

    # Paths
    templates_dir = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_3\Week_3_Next_Step\Delegation\Taxonomy_Aligned_Templates\Task_Templates'
    workflows_dir = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_3\Week_3_Next_Step\Delegation\Taxonomy_Aligned_Workflows'
    output_path = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_3\Week_3_Next_Step\Delegation\Taxonomy_Aligned_Templates\Template_Cross_Reference_Map.json'

    # Get all task template IDs
    task_files = [f for f in os.listdir(templates_dir) if f.endswith('.json') and f.startswith('TST-')]
    task_ids = sorted([f.split('_')[0] for f in task_files])

    print(f"Found {len(task_ids)} task templates")

    # Get workflow to task mappings
    workflow_files = [f for f in os.listdir(workflows_dir) if f.endswith('.json') and f.startswith('WRF-')]

    workflow_task_mapping = {}
    milestone_task_mapping = {}

    for filename in sorted(workflow_files):
        filepath = os.path.join(workflows_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            workflow = json.load(f)
            wrf_id = workflow.get('workflow_id', 'Unknown')
            task_list = workflow.get('tasks', {}).get('task_ids', [])
            workflow_task_mapping[wrf_id] = task_list

            # Also track milestone -> tasks
            related_project = workflow.get('related_project', {})
            if related_project:
                milestone_id = related_project.get('milestone_dependencies')
                if milestone_id:
                    if milestone_id not in milestone_task_mapping:
                        milestone_task_mapping[milestone_id] = []
                    milestone_task_mapping[milestone_id].extend(task_list)

    print(f"Loaded {len(workflow_files)} workflows")
    print(f"Mapped {len(milestone_task_mapping)} milestones to tasks")

    # Build comprehensive cross-reference
    cross_reference = {
        "metadata": {
            "created_date": "2025-11-26",
            "last_updated": "2025-11-26",
            "description": "Complete cross-reference mapping for all TAX-002 templates from Week 3",
            "total_projects": 10,
            "total_milestones": 11,
            "total_task_templates": len(task_ids),
            "total_workflows": len(workflow_files),
            "version": "2.0"
        },
        "hierarchy": {
            "PRT (Projects)": {
                "count": 10,
                "ids": [
                    "PRT-005", "PRT-009", "PRT-010", "PRT-011", "PRT-012",
                    "PRT-013", "PRT-014", "PRT-015", "PRT-016", "PRT-017"
                ],
                "contains": "MLT (Milestones)",
                "description": "Top-level project templates"
            },
            "MLT (Milestones)": {
                "count": 11,
                "ids": [
                    "MLT-030", "MLT-031", "MLT-032", "MLT-033", "MLT-034",
                    "MLT-035", "MLT-036", "MLT-037", "MLT-038", "MLT-039"
                ],
                "contains": "TST (Task Templates)",
                "belongs_to": "PRT (Projects)",
                "description": "Milestone templates derived from planning workflows"
            },
            "TST (Task Templates)": {
                "count": len(task_ids),
                "ids": task_ids,
                "contains": "STT (Step Templates)",
                "belongs_to": "MLT (Milestones)",
                "description": "Task templates converted from TSK-### format"
            },
            "WRF (Workflows)": {
                "count": len(workflow_files),
                "planning_phase": "WRF-001 to WRF-010 (10 workflows)",
                "execution_phase": "WRF-011 to WRF-050 (40 workflows)",
                "references": "PRT, MLT, TST",
                "description": "Workflow definitions linking tasks together"
            }
        },
        "project_milestone_mapping": {
            "PRT-005": ["MLT-030"],
            "PRT-009": ["MLT-031"],
            "PRT-010": ["MLT-032"],
            "PRT-011": ["MLT-033"],
            "PRT-012": ["MLT-034"],
            "PRT-013": ["MLT-035"],
            "PRT-014": ["MLT-036"],
            "PRT-015": ["MLT-037"],
            "PRT-016": ["MLT-038"],
            "PRT-017": ["MLT-039"]
        },
        "workflow_project_mapping": {
            "WRF-001": "PRT-005",
            "WRF-002": "PRT-009",
            "WRF-003": "PRT-010",
            "WRF-004": "PRT-011",
            "WRF-005": "PRT-012",
            "WRF-006": "PRT-013",
            "WRF-007": "PRT-014",
            "WRF-008": "PRT-015",
            "WRF-009": "PRT-016",
            "WRF-010": "PRT-017"
        },
        "workflow_task_mapping": workflow_task_mapping,
        "milestone_task_mapping": milestone_task_mapping,
        "task_statistics": {
            "total_tasks": len(task_ids),
            "first_task": task_ids[0] if task_ids else None,
            "last_task": task_ids[-1] if task_ids else None,
            "tasks_in_workflows": sum(len(tasks) for tasks in workflow_task_mapping.values()),
            "tasks_per_workflow_avg": round(sum(len(tasks) for tasks in workflow_task_mapping.values()) / len(workflow_task_mapping), 1) if workflow_task_mapping else 0
        },
        "files_created": {
            "task_templates": f"Task_Templates/ ({len(task_ids)} TST-###.json files)",
            "milestone_templates": "Milestone_Templates/ (11 MLT-###.json files)",
            "project_templates": "Project_Templates/ (10 PRT-###.json files)",
            "workflows": f"Taxonomy_Aligned_Workflows/ ({len(workflow_files)} WRF-###.json files)",
            "documentation": [
                "TASK_TEMPLATE_INDEX.md",
                "Task_Template_Catalog.csv",
                "Task_Template_Statistics.json",
                "VALIDATION_REPORT.json",
                "INTEGRATION_README.md"
            ]
        },
        "usage_guide": {
            "find_task_by_id": "Use TASK_TEMPLATE_INDEX.md or Task_Template_Catalog.csv",
            "find_workflow_for_task": "Search workflow_task_mapping for task ID",
            "find_milestone_for_task": "Search milestone_task_mapping for task ID",
            "find_project_for_milestone": "Use project_milestone_mapping",
            "browse_all_tasks": "See hierarchy.TST.ids for complete list"
        }
    }

    # Save updated cross-reference
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(cross_reference, f, indent=2, ensure_ascii=False)

    print(f"\nCross-reference updated: {output_path}")

    # Print summary
    print("\n" + "="*60)
    print("CROSS-REFERENCE UPDATE COMPLETE")
    print("="*60)
    print(f"Task Templates: {len(task_ids)}")
    print(f"Workflows: {len(workflow_files)}")
    print(f"Milestones: {len(milestone_task_mapping)}")
    print(f"Projects: 10")
    print(f"\nTasks in workflows: {cross_reference['task_statistics']['tasks_in_workflows']}")
    print(f"Avg tasks per workflow: {cross_reference['task_statistics']['tasks_per_workflow_avg']}")

    return cross_reference

if __name__ == "__main__":
    update_cross_reference()
