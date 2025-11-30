# AI Review Instructions for Day 28 Task Categorization

## Objective

Review extracted items and categorize them into:
1. **Tasks (TSK-###)** - Work to be done (active verbs)
2. **Reports (RPT-###)** - Work completed (completed verbs)
3. **Problems (PRB-###)** - Issues/bugs/blockers
4. **Metadata** - Template fields, section headers (to be filtered)

## Classification Rules

### Metadata (Filter Out)
- Field labels: *Priority:**, *Status:**, *Time:**, etc.
- Section headers: *What I worked on:**, *Success Criteria:**, etc.
- Template markers: *Whisper Flow Transcript:**, *Definition of Done:**, etc.
- Instructions/placeholders: "Instructions:", "[Time] - [Activity]"

### Tasks (Active Work)
- Start with action verbs in base/process form (do, doing, create, creating)
- Describe work that needs to be performed
- Examples: "Respond to messages", "Creating design mockups", "Update API"

### Reports (Completed Work)
- Start with completed verbs (created, developed, implemented, sent, updated)
- Describe work that was done
- Examples: "Created new feature", "Sent report", "Updated documentation"

### Problems
- Contain keywords: error, bug, issue, problem, broken, failed, fix, blocked
- Describe something not working or needing repair
- Examples: "API endpoint not working", "Fix authentication bug"

## Process

1. Process batches sequentially (Batch_01.json through Batch_12.json)
2. For each item, determine: Task, Report, Problem, or Metadata
3. Create categorized output with new IDs (TSK/RPT/PRB-###)
4. Match tasks/reports to existing task templates if possible

## Output Format

For each batch, create a categorized JSON file with structure:
```json
{
  "batch_number": 1,
  "tasks": [...],
  "reports": [...],
  "problems": [...],
  "metadata_filtered": [...]
}
```

## Key Insight

The extraction contains:
- Real tasks and outcomes from daily work
- Template field labels and section headers
- Instructional text and placeholders

Use context understanding to separate actual work items from template structure.
