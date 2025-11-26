#!/usr/bin/env python3
"""
extract_tasks_batch.py - Batch Task Extraction Script

Purpose: Extract tasks, actions, objects, tools from collected employee files
         using MAIN_PROMPT_v6.md methodology with AI assistance.

Milestone: MLT-003 (Entity Extraction)
Time Savings: 60 min manual → 10 min automated (50 min saved)

Usage:
    python3 extract_tasks_batch.py [--date YYYY-MM-DD] [--ai-provider claude|openai]

Examples:
    python3 extract_tasks_batch.py
    python3 extract_tasks_batch.py --date 2025-11-25
    python3 extract_tasks_batch.py --ai-provider openai
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
import anthropic
import openai

# ============================================================================
# Configuration
# ============================================================================

DROPBOX_ROOT = Path.home() / "Library/CloudStorage/Dropbox"
WORKSPACE_ROOT = DROPBOX_ROOT / "ENTITIES/DAILIES/Daily_Processing"
PROMPTS_ROOT = DROPBOX_ROOT / "ENTITIES/PROMPTS/Core"

# AI Provider settings
DEFAULT_AI_PROVIDER = "claude"  # claude or openai
CLAUDE_MODEL = "claude-sonnet-4-5-20250929"
OPENAI_MODEL = "gpt-4-turbo-preview"

# Batch processing settings
BATCH_SIZE = 5  # Process N files at once
MAX_TOKENS = 4096

# ============================================================================
# MAIN_PROMPT_v6 Extraction Template
# ============================================================================

EXTRACTION_PROMPT_TEMPLATE = """You are an entity extraction assistant. Extract structured task information from employee daily files.

**Output Format (from MAIN_PROMPT_v6.md line 42):**
- Tasks with MLT-### (Milestones), TST-### (Task Templates)
- Actions: ACT-### (verbs like Create, Update, Generate, Analyze)
- Objects: OBJ-### (nouns like Report, Design, Video, Lead List)
- Tools: TOL-### (software/platforms like Figma, Claude, LinkedIn)
- Skills: SKL-### (ability combinations)
- Professions: PRF-### (job roles)
- Departments: DPT-### (organizational units)

**Employee Context:**
- Name: {employee_name}
- Department: {department}
- File: {filename}

**File Content:**
```
{content}
```

**Extract and output as JSON:**
```json
{{
  "employee": "{employee_name}",
  "department": "{department}",
  "file": "{filename}",
  "tasks": [
    {{
      "task_name": "ACTION_OBJECT_TOOL",
      "description": "Full description",
      "action": {{"code": "ACT-XXX", "name": "Action verb"}},
      "object": {{"code": "OBJ-XXX", "name": "Deliverable"}},
      "tool": {{"code": "TOL-XXX", "name": "Tool used"}},
      "profession": {{"code": "PRF-XXX", "name": "Best fit profession"}},
      "department": {{"code": "DPT-XXX", "name": "Department"}},
      "skills": ["skill 1", "skill 2"],
      "priority": "high|medium|low",
      "status": "completed|planned|in_progress",
      "estimated_duration_minutes": 30
    }}
  ],
  "unique_actions": [
    {{"code": "ACT-XXX", "name": "Action"}}
  ],
  "unique_objects": [
    {{"code": "OBJ-XXX", "name": "Object"}}
  ],
  "unique_tools": [
    {{"code": "TOL-XXX", "name": "Tool"}}
  ]
}}
```

Extract all tasks mentioned, whether completed or planned. Focus on actionable work items.
"""

# ============================================================================
# AI Provider Functions
# ============================================================================

def extract_with_claude(content, employee_name, department, filename):
    """Extract tasks using Claude API."""
    try:
        client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

        prompt = EXTRACTION_PROMPT_TEMPLATE.format(
            employee_name=employee_name,
            department=department,
            filename=filename,
            content=content
        )

        message = client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=MAX_TOKENS,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        response_text = message.content[0].text

        # Extract JSON from response
        json_start = response_text.find('{')
        json_end = response_text.rfind('}') + 1

        if json_start >= 0 and json_end > json_start:
            json_text = response_text[json_start:json_end]
            return json.loads(json_text)
        else:
            return None

    except Exception as e:
        print(f"  ⚠️  Claude API error: {e}")
        return None

def extract_with_openai(content, employee_name, department, filename):
    """Extract tasks using OpenAI API."""
    try:
        client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

        prompt = EXTRACTION_PROMPT_TEMPLATE.format(
            employee_name=employee_name,
            department=department,
            filename=filename,
            content=content
        )

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a task extraction assistant. Always respond with valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=MAX_TOKENS
        )

        response_text = response.choices[0].message.content

        # Extract JSON
        json_start = response_text.find('{')
        json_end = response_text.rfind('}') + 1

        if json_start >= 0 and json_end > json_start:
            json_text = response_text[json_start:json_end]
            return json.loads(json_text)
        else:
            return None

    except Exception as e:
        print(f"  ⚠️  OpenAI API error: {e}")
        return None

def extract_tasks_from_file(file_path, ai_provider="claude"):
    """Extract tasks from a single collected file."""
    # Parse filename: DEPT_Employee_Name_filename.md
    filename = file_path.name
    parts = filename.replace('.md', '').split('_')

    if len(parts) < 3:
        return None

    department_code = parts[0]
    employee_parts = parts[1:-1]
    employee_name = ' '.join(employee_parts)
    original_filename = parts[-1] + '.md'

    # Read content
    try:
        content = file_path.read_text()
    except Exception as e:
        print(f"  ⚠️  Could not read {filename}: {e}")
        return None

    # Skip empty files
    if not content.strip():
        return None

    # Extract using AI
    if ai_provider == "claude":
        result = extract_with_claude(content, employee_name, department_code, original_filename)
    elif ai_provider == "openai":
        result = extract_with_openai(content, employee_name, department_code, original_filename)
    else:
        print(f"  ⚠️  Unknown AI provider: {ai_provider}")
        return None

    return result

# ============================================================================
# Batch Processing
# ============================================================================

def batch_extract_tasks(date_str=None, ai_provider=DEFAULT_AI_PROVIDER, dry_run=False, limit=None):
    """
    Extract tasks from all collected files in batches.

    Args:
        date_str: Date string in YYYY-MM-DD format (default: today)
        ai_provider: AI provider to use (claude or openai)
        dry_run: If True, only print what would be done
        limit: Maximum number of files to process (for testing)

    Returns:
        dict: Extraction statistics
    """
    if not date_str:
        date_str = datetime.now().strftime('%Y-%m-%d')

    print(f"{'[DRY RUN] ' if dry_run else ''}Task Extraction - Batch Processing")
    print(f"Date: {date_str}")
    print(f"AI Provider: {ai_provider}")
    print("=" * 60)

    # Check workspace
    workspace = WORKSPACE_ROOT / f"{date_str}_Collection"
    collection_dir = workspace / "01_Collected_Files"
    extraction_dir = workspace / "02_Extracted_Tasks"

    if not workspace.exists():
        print(f"❌ Workspace not found: {workspace}")
        print("   Run collect_daily_files.py first!")
        return None

    if not collection_dir.exists() or not list(collection_dir.glob("*.md")):
        print(f"❌ No collected files found in: {collection_dir}")
        return None

    # Create extraction directory
    if not dry_run:
        extraction_dir.mkdir(exist_ok=True)

    # Get all collected files
    collected_files = sorted(collection_dir.glob("*.md"))

    # Apply limit for testing
    if limit:
        collected_files = collected_files[:limit]
        print(f"⚠️  Processing limited to {limit} files for testing\n")

    total_files = len(collected_files)
    print(f"Files to process: {total_files}\n")

    # Check API key
    if not dry_run:
        if ai_provider == "claude" and not os.environ.get("ANTHROPIC_API_KEY"):
            print("❌ ANTHROPIC_API_KEY environment variable not set!")
            print("   Set it with: export ANTHROPIC_API_KEY='your-key-here'")
            return None
        elif ai_provider == "openai" and not os.environ.get("OPENAI_API_KEY"):
            print("❌ OPENAI_API_KEY environment variable not set!")
            print("   Set it with: export OPENAI_API_KEY='your-key-here'")
            return None

    # Statistics
    stats = {
        'total_files': total_files,
        'processed': 0,
        'extracted': 0,
        'total_tasks': 0,
        'failed': 0,
        'errors': [],
        'extractions': []
    }

    # Process in batches
    for i, file_path in enumerate(collected_files, 1):
        print(f"[{i}/{total_files}] Processing: {file_path.name}")

        if dry_run:
            print(f"  → Would extract tasks using {ai_provider}")
            stats['processed'] += 1
            continue

        # Extract tasks
        result = extract_tasks_from_file(file_path, ai_provider)

        if result and result.get('tasks'):
            task_count = len(result['tasks'])
            print(f"  ✅ Extracted {task_count} tasks")

            # Save extraction
            output_filename = file_path.stem + '_extracted.json'
            output_path = extraction_dir / output_filename

            with open(output_path, 'w') as f:
                json.dump(result, f, indent=2)

            stats['extracted'] += 1
            stats['total_tasks'] += task_count
            stats['extractions'].append({
                'file': file_path.name,
                'tasks': task_count,
                'output': output_filename
            })
        else:
            print(f"  ⚠️  No tasks extracted or error occurred")
            stats['failed'] += 1
            stats['errors'].append(file_path.name)

        stats['processed'] += 1

    # Summary
    print("\n" + "=" * 60)
    print(f"{'[DRY RUN] ' if dry_run else ''}EXTRACTION COMPLETE")
    print(f"Files Processed: {stats['processed']}/{total_files}")
    print(f"Successful Extractions: {stats['extracted']}")
    print(f"Total Tasks Extracted: {stats['total_tasks']}")
    print(f"Failed: {stats['failed']}")

    if not dry_run and stats['extracted'] > 0:
        avg_tasks = stats['total_tasks'] / stats['extracted']
        print(f"Average Tasks per Employee: {avg_tasks:.1f}")
        print(f"\nExtractions saved to: {extraction_dir}")

        # Save extraction summary
        summary_file = extraction_dir / "_extraction_summary.json"
        with open(summary_file, 'w') as f:
            json.dump(stats, f, indent=2)
        print(f"Summary saved: {summary_file}")

        # Update processing log
        log_file = workspace / "06_Processing_Log.md"
        if log_file.exists():
            update_log(log_file, stats)

    return stats

def update_log(log_file, stats):
    """Update processing log with extraction results."""
    content = log_file.read_text()

    update_text = f"""
## MLT-003: Entity Extraction Progress

### Completed: {datetime.now().strftime('%H:%M')}

- **Files Processed:** {stats['processed']}
- **Successful Extractions:** {stats['extracted']}
- **Total Tasks Extracted:** {stats['total_tasks']}
- **Failed:** {stats['failed']}
- **Average Tasks per Employee:** {stats['total_tasks'] / max(stats['extracted'], 1):.1f}

"""

    content += update_text
    log_file.write_text(content)

# ============================================================================
# CLI Interface
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Extract tasks from collected employee files using AI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Extract tasks for today using Claude
  python3 extract_tasks_batch.py

  # Extract for specific date
  python3 extract_tasks_batch.py --date 2025-11-25

  # Use OpenAI instead of Claude
  python3 extract_tasks_batch.py --ai-provider openai

  # Test with first 5 files only
  python3 extract_tasks_batch.py --limit 5

  # Dry run
  python3 extract_tasks_batch.py --dry-run

Environment Variables:
  ANTHROPIC_API_KEY - Required for Claude (default provider)
  OPENAI_API_KEY    - Required for OpenAI provider
        """
    )

    parser.add_argument(
        '--date',
        help='Date in YYYY-MM-DD format (default: today)',
        default=None
    )

    parser.add_argument(
        '--ai-provider',
        choices=['claude', 'openai'],
        default=DEFAULT_AI_PROVIDER,
        help=f'AI provider to use (default: {DEFAULT_AI_PROVIDER})'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview what would be done without calling API'
    )

    parser.add_argument(
        '--limit',
        type=int,
        help='Limit number of files to process (for testing)',
        default=None
    )

    args = parser.parse_args()

    # Run extraction
    stats = batch_extract_tasks(
        date_str=args.date,
        ai_provider=args.ai_provider,
        dry_run=args.dry_run,
        limit=args.limit
    )

    if stats is None:
        return 1

    if stats['extracted'] == 0 and not args.dry_run:
        print("\n⚠️  WARNING: No tasks were extracted!")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())
