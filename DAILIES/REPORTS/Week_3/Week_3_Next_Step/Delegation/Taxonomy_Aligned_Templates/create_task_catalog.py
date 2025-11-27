import json
import os
import csv
from collections import defaultdict

def create_catalog():
    """Create comprehensive catalog of all task templates"""

    # Paths
    templates_dir = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_3\Week_3_Next_Step\Delegation\Taxonomy_Aligned_Templates\Task_Templates'
    output_dir = r'C:\Users\Dell\Dropbox\ENTITIES\DAILIES\REPORTS\Week_3\Week_3_Next_Step\Delegation\Taxonomy_Aligned_Templates'

    # Collect all task templates
    templates = []
    files = [f for f in os.listdir(templates_dir) if f.endswith('.json') and f.startswith('TST-')]

    print(f"Processing {len(files)} task template files...")

    for filename in sorted(files):
        filepath = os.path.join(templates_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                template = json.load(f)

                # Safely extract fields with defaults
                metadata = template.get('metadata', {})
                execution = template.get('execution', {})
                assignment = template.get('assignment', {})
                migration = template.get('migration_notes', {})

                templates.append({
                    'task_template_id': template.get('task_template_id', 'Unknown'),
                    'task_name': metadata.get('task_name', 'Unknown'),
                    'department': metadata.get('department', 'Unknown'),
                    'category': metadata.get('category', 'Task'),
                    'priority': metadata.get('priority', 'Medium'),
                    'complexity': metadata.get('complexity', 'Medium'),
                    'estimated_duration': metadata.get('estimated_duration', 'TBD'),
                    'business_impact': metadata.get('business_impact', 'Medium'),
                    'quick_win': execution.get('quick_win', False),
                    'matched_template': execution.get('matched_template', 'CUSTOM'),
                    'assigned_to': assignment.get('assigned_to', 'TBD'),
                    'original_id': migration.get('original_id', 'Unknown'),
                    'filename': filename
                })
        except Exception as e:
            print(f"Warning: Skipping {filename}: {e}")

    print(f"Loaded {len(templates)} templates")

    # Create CSV catalog
    csv_path = os.path.join(output_dir, 'Task_Template_Catalog.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        fieldnames = [
            'task_template_id', 'task_name', 'department', 'category',
            'priority', 'complexity', 'estimated_duration', 'business_impact',
            'quick_win', 'matched_template', 'assigned_to', 'original_id', 'filename'
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(templates)

    print(f"CSV catalog created: {csv_path}")

    # Create statistics
    stats = {
        'total_templates': len(templates),
        'by_department': defaultdict(int),
        'by_category': defaultdict(int),
        'by_priority': defaultdict(int),
        'by_complexity': defaultdict(int),
        'quick_wins': 0,
        'by_template_type': defaultdict(int)
    }

    for t in templates:
        stats['by_department'][t['department']] += 1
        stats['by_category'][t['category']] += 1
        stats['by_priority'][t['priority']] += 1
        stats['by_complexity'][t['complexity']] += 1
        if t['quick_win']:
            stats['quick_wins'] += 1
        stats['by_template_type'][t['matched_template']] += 1

    # Convert defaultdicts to regular dicts
    stats['by_department'] = dict(stats['by_department'])
    stats['by_category'] = dict(stats['by_category'])
    stats['by_priority'] = dict(stats['by_priority'])
    stats['by_complexity'] = dict(stats['by_complexity'])
    stats['by_template_type'] = dict(stats['by_template_type'])

    # Save statistics
    stats_path = os.path.join(output_dir, 'Task_Template_Statistics.json')
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)

    print(f"Statistics created: {stats_path}")

    # Create markdown index
    md_content = """# Task Template Catalog and Index

**Generated:** November 26, 2025
**Total Templates:** {total}
**Source:** Week 3 Task Mapping (TSK-### to TST-### conversion)

---

## Quick Statistics

### By Department
{dept_stats}

### By Category
{cat_stats}

### By Priority
{pri_stats}

### By Complexity
{comp_stats}

### Quick Wins
- **Total Quick Win Tasks:** {quick_wins}
- **Percentage:** {qw_pct:.1f}%

---

## Template Index

### High Priority Tasks ({high_count})

{high_tasks}

### Medium Priority Tasks ({med_count})

{med_tasks}

### Low Priority Tasks ({low_count})

{low_tasks}

---

## Department Breakdown

{dept_breakdown}

---

## Category Breakdown

{cat_breakdown}

---

## Usage

**Find a task by ID:**
```
Search for TST-### in this file or Task_Template_Catalog.csv
```

**Find tasks by department:**
```
Use Department Breakdown section below
```

**Find quick wins:**
```
Filter Task_Template_Catalog.csv where quick_win = true
```

**Access template file:**
```
All templates in: Task_Templates/TST-###_Name.json
```

---

## Files

- **[Task_Template_Catalog.csv](Task_Template_Catalog.csv)** - Searchable CSV of all templates
- **[Task_Template_Statistics.json](Task_Template_Statistics.json)** - Complete statistics
- **[Task_Templates/](Task_Templates/)** - All 426 JSON template files
- **[_GENERATION_SUMMARY.json](Task_Templates/_GENERATION_SUMMARY.json)** - Generation details

---

**Last Updated:** November 26, 2025
"""

    # Generate department stats table
    dept_stats_lines = []
    for dept, count in sorted(stats['by_department'].items(), key=lambda x: x[1], reverse=True):
        dept_stats_lines.append(f"- **{dept}**: {count} tasks")
    dept_stats = "\n".join(dept_stats_lines)

    # Generate category stats table
    cat_stats_lines = []
    for cat, count in sorted(stats['by_category'].items(), key=lambda x: x[1], reverse=True):
        cat_stats_lines.append(f"- **{cat}**: {count} tasks")
    cat_stats = "\n".join(cat_stats_lines)

    # Generate priority stats
    pri_stats_lines = []
    for pri in ['High', 'Medium', 'Low']:
        count = stats['by_priority'].get(pri, 0)
        pri_stats_lines.append(f"- **{pri}**: {count} tasks")
    pri_stats = "\n".join(pri_stats_lines)

    # Generate complexity stats
    comp_stats_lines = []
    for comp in ['High', 'Medium', 'Low']:
        count = stats['by_complexity'].get(comp, 0)
        comp_stats_lines.append(f"- **{comp}**: {count} tasks")
    comp_stats = "\n".join(comp_stats_lines)

    # High priority tasks
    high_tasks_list = [t for t in templates if t['priority'] == 'High']
    high_tasks_lines = []
    for t in high_tasks_list[:50]:  # First 50
        high_tasks_lines.append(f"- **{t['task_template_id']}**: {t['task_name']} ({t['department']} - {t['category']})")
    if len(high_tasks_list) > 50:
        high_tasks_lines.append(f"\n_...and {len(high_tasks_list) - 50} more (see CSV catalog)_")
    high_tasks = "\n".join(high_tasks_lines) if high_tasks_lines else "_No high priority tasks_"

    # Medium priority tasks
    med_tasks_list = [t for t in templates if t['priority'] == 'Medium']
    med_tasks_lines = []
    for t in med_tasks_list[:30]:  # First 30
        med_tasks_lines.append(f"- **{t['task_template_id']}**: {t['task_name']} ({t['department']})")
    if len(med_tasks_list) > 30:
        med_tasks_lines.append(f"\n_...and {len(med_tasks_list) - 30} more (see CSV catalog)_")
    med_tasks = "\n".join(med_tasks_lines) if med_tasks_lines else "_No medium priority tasks_"

    # Low priority tasks
    low_tasks_list = [t for t in templates if t['priority'] == 'Low']
    low_tasks_lines = []
    for t in low_tasks_list[:20]:  # First 20
        low_tasks_lines.append(f"- **{t['task_template_id']}**: {t['task_name']} ({t['department']})")
    if len(low_tasks_list) > 20:
        low_tasks_lines.append(f"\n_...and {len(low_tasks_list) - 20} more (see CSV catalog)_")
    low_tasks = "\n".join(low_tasks_lines) if low_tasks_lines else "_No low priority tasks_"

    # Department breakdown
    dept_breakdown_lines = []
    for dept in sorted(stats['by_department'].keys()):
        dept_tasks = [t for t in templates if t['department'] == dept]
        dept_breakdown_lines.append(f"### {dept} ({len(dept_tasks)} tasks)\n")
        for t in dept_tasks[:20]:
            dept_breakdown_lines.append(f"- {t['task_template_id']}: {t['task_name']}")
        if len(dept_tasks) > 20:
            dept_breakdown_lines.append(f"\n_...and {len(dept_tasks) - 20} more_\n")
        dept_breakdown_lines.append("")
    dept_breakdown = "\n".join(dept_breakdown_lines)

    # Category breakdown
    cat_breakdown_lines = []
    for cat in sorted(stats['by_category'].keys()):
        cat_tasks = [t for t in templates if t['category'] == cat]
        cat_breakdown_lines.append(f"### {cat} ({len(cat_tasks)} tasks)\n")
        for t in cat_tasks[:15]:
            cat_breakdown_lines.append(f"- {t['task_template_id']}: {t['task_name']} ({t['department']})")
        if len(cat_tasks) > 15:
            cat_breakdown_lines.append(f"\n_...and {len(cat_tasks) - 15} more_\n")
        cat_breakdown_lines.append("")
    cat_breakdown = "\n".join(cat_breakdown_lines)

    # Format markdown
    md_formatted = md_content.format(
        total=stats['total_templates'],
        dept_stats=dept_stats,
        cat_stats=cat_stats,
        pri_stats=pri_stats,
        comp_stats=comp_stats,
        quick_wins=stats['quick_wins'],
        qw_pct=(stats['quick_wins'] / stats['total_templates'] * 100),
        high_count=len(high_tasks_list),
        high_tasks=high_tasks,
        med_count=len(med_tasks_list),
        med_tasks=med_tasks,
        low_count=len(low_tasks_list),
        low_tasks=low_tasks,
        dept_breakdown=dept_breakdown,
        cat_breakdown=cat_breakdown
    )

    # Save markdown index
    md_path = os.path.join(output_dir, 'TASK_TEMPLATE_INDEX.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_formatted)

    print(f"Markdown index created: {md_path}")

    # Print summary
    print("\n" + "="*60)
    print("CATALOG CREATION COMPLETE")
    print("="*60)
    print(f"Total Templates: {stats['total_templates']}")
    print(f"\nDepartments:")
    for dept, count in sorted(stats['by_department'].items(), key=lambda x: x[1], reverse=True):
        print(f"  {dept}: {count}")
    print(f"\nCategories:")
    for cat, count in sorted(stats['by_category'].items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat}: {count}")
    print(f"\nQuick Wins: {stats['quick_wins']} ({stats['quick_wins'] / stats['total_templates'] * 100:.1f}%)")

    return stats

if __name__ == "__main__":
    create_catalog()
