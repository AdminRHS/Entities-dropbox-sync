---
category: 00_SEARCH_QUEUE
subcategory: root
type: log
source_id: README
title: README
date: 2025-11-24
status: draft
owner: unknown
related: []
links: []
---

# README

## Summary
- TODO

## Context
- TODO

## Data / Content
# 00_SEARCH_QUEUE: Video Search Assignment System

## Purpose

Manages the assignment and tracking of video search tasks based on weekly reports and research needs.

## Workflow

1. **Weekly Report Analysis** → Identifies research gaps
2. **Search Prompt Generation** → Creates targeted search queries
3. **Search Assignment** → Assigns to employees
4. **Search Execution** → Employee runs searches
5. **Video Discovery** → Results added to VIDEO_QUEUE

## Files

- **Search_Queue_Master.csv** - Active search assignments
- **Search_Prompts/** - Generated search prompts by department
- **Active_Searches/** - In-progress searches
- **Completed_Searches/** - Completed search reports
- **scripts/** - Queue management scripts

## Usage

### Assign a Search Task
```bash
python scripts/assign_search.py "Employee Name" "Department" "Research Topic"
```

### Complete a Search
```bash
python scripts/complete_search.py SEARCH-001 --videos-found 15
```

### Generate Search Prompts
```bash
python scripts/generate_search_prompts.py --from-weekly-report
```


## Findings
- TODO

## Actions / Next Steps
- TODO

## Metrics / Status
- TODO

## Attachments / Links
- TODO

## Change Log
- 2025-11-24 standardization scaffold added
