#!/usr/bin/env python3
"""
Script to generate individual task files from department YAML blocks
"""

import os
import re

# Base directory
BASE_DIR = r"C:\Users\Dell\Dropbox\Nov25\Taxonomy\Framework\Entities\TASK_MANAGERS"

# Template for individual task files
TASK_FILE_TEMPLATE = """# {task_id}: {task_name}

**Department:** {department}
**Status:** {status}
**Reusability:** {reusability}
**Automation Potential:** {automation}

---

## Quick Info

- **Action:** {action}
- **Object:** {object}
- **Tool:** {tool}
- **Estimated Time:** {time}

---

## Full Template

```yaml
{yaml_content}
```

---

## Navigation

- [Back to {department} Tasks](../../Tasks_{dept_code}.md)
- [All Tasks Listing](../../TASKS_LISTING.md)
- [Master Index](../../INDEX.md)

---

**Source:** Extracted from Tasks_{dept_code}.md
**Date:** 2025-11-10
"""

def extract_yaml_blocks(file_path):
    """Extract all YAML blocks from a department file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all YAML blocks
    yaml_pattern = r'```yaml\n(.*?)```'
    yaml_blocks = re.findall(yaml_pattern, content, re.DOTALL)

    return yaml_blocks

def parse_yaml_block(yaml_content):
    """Parse a YAML block to extract key information"""
    info = {}

    # Extract template_id
    match = re.search(r'template_id:\s*(\S+)', yaml_content)
    info['task_id'] = match.group(1) if match else 'UNKNOWN'

    # Extract task_template_name
    match = re.search(r'task_template_name:\s*"([^"]+)"', yaml_content)
    info['task_name'] = match.group(1) if match else 'Unknown Task'

    # Extract status
    match = re.search(r'status:\s*"([^"]+)"', yaml_content)
    info['status'] = match.group(1) if match else 'Active'

    # Extract reusability_score
    match = re.search(r'reusability_score:\s*"([^"]+)"', yaml_content)
    info['reusability'] = match.group(1) if match else 'High'

    # Extract automation ranking
    match = re.search(r'ranking:\s*"([^"]+)"', yaml_content)
    info['automation'] = match.group(1) if match else 'Medium'

    # Extract action
    match = re.search(r'action:\s*"([^"]+)"', yaml_content)
    info['action'] = match.group(1) if match else 'Unknown'

    # Extract object
    match = re.search(r'object:\s*"([^"]+)"', yaml_content)
    info['object'] = match.group(1) if match else 'Unknown'

    # Extract tool
    match = re.search(r'tool:\s*"([^"]+)"', yaml_content)
    info['tool'] = match.group(1) if match else 'Unknown'

    # Calculate total estimated time from steps
    time_pattern = r'estimated_time:\s*"([^"]+)"'
    times = re.findall(time_pattern, yaml_content)
    info['time'] = times[0] if times else 'Variable'

    return info

def create_task_file(yaml_content, dept_name, dept_code):
    """Create an individual task file from YAML content"""
    info = parse_yaml_block(yaml_content)

    # Prepare template variables
    template_vars = {
        'task_id': info['task_id'],
        'task_name': info['task_name'],
        'department': dept_name,
        'status': info['status'],
        'reusability': info['reusability'],
        'automation': info['automation'],
        'action': info['action'],
        'object': info['object'],
        'tool': info['tool'],
        'time': info['time'],
        'yaml_content': yaml_content.strip(),
        'dept_code': dept_code
    }

    # Generate file content
    file_content = TASK_FILE_TEMPLATE.format(**template_vars)

    # Determine file path
    task_dir = os.path.join(BASE_DIR, 'Task_Templates', dept_code)
    file_name = f"{info['task_id']}.md"
    file_path = os.path.join(task_dir, file_name)

    # Write file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(file_content)

    return file_path

def process_department(dept_code, dept_name):
    """Process all tasks for a department"""
    dept_file = os.path.join(BASE_DIR, f'Tasks_{dept_code}.md')

    if not os.path.exists(dept_file):
        print(f"Warning: {dept_file} not found")
        return []

    print(f"Processing {dept_name} ({dept_code})...")

    yaml_blocks = extract_yaml_blocks(dept_file)
    created_files = []

    for yaml_content in yaml_blocks:
        try:
            file_path = create_task_file(yaml_content, dept_name, dept_code)
            created_files.append(file_path)
            print(f"  Created: {os.path.basename(file_path)}")
        except Exception as e:
            print(f"  Error creating file: {e}")

    return created_files

def main():
    """Main execution"""
    departments = [
        ('ADMIN', 'Admin'),
        ('AI', 'AI'),
        ('', 'Content Ops')
        ('DESIGN', 'Design'),
        ('DEV', 'Dev'),
        ('HR', 'HR'),
        ('LG', 'LG'),
        ('OPS', 'Ops'),
        ('SALES', 'Sales'),
        ('VIDEO', 'Video')
    ]

    all_files = []

    for dept_code, dept_name in departments:
        files = process_department(dept_code, dept_name)
        all_files.extend(files)
        print(f"  Total files created for {dept_name}: {len(files)}\n")

    print(f"\n=== SUMMARY ===")
    print(f"Total files created: {len(all_files)}")
    print(f"\nFiles created by department:")

    for dept_code, dept_name in departments:
        dept_files = [f for f in all_files if f'Task_Templates\\{dept_code}\\' in f or f'Task_Templates/{dept_code}/' in f]
        print(f"  {dept_name}: {len(dept_files)} files")

if __name__ == '__main__':
    main()
