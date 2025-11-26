# PMT-077: Employee Activity Analyzer v1.0

**Prompt ID:** PMT-077
**Version:** 1.0
**Department:** System Architecture
**Category:** EXTERNAL_MONITORING
**Date:** 2025-11-21
**Status:** Active
**Parent Prompt:** PMT-074 (Data Architect Master)

---

## Purpose

External monitoring of employee daily file processing and activity patterns. Tracks completeness, detects anomalies, identifies new taxonomy entities, and generates department-specific analytics.

**Core Functions:**
1. **Completeness Tracking**: Monitor 76% → 95%+ target
2. **Pattern Detection**: Identify recurring tasks for template generation
3. **Anomaly Detection**: Flag unusual activities or missing files
4. **Department Analysis**: Department-specific metrics and issues
5. **New Entity Discovery**: Extract potential new tools, actions, responsibilities
6. **Performance Metrics**: Processing time, data quality, coverage

---

## Current State Analysis

### DAILIES Processing Status

**Pipeline**: 18-script system (script_01 to script_18)
**Processing Time**: 12-16 minutes per employee (sequential)
**Current Completeness**: 76% (22/29 employees with valid data)
**Target**: 95%+ completeness

**Problem Areas**:
- LG Department: 5/10 employees missing/corrupt files (Nov 17-18)
- Total gap: 10 employees with issues

---

## Completeness Tracking

### Monitor Daily File Presence

```python
def track_daily_completeness(date_str):
    """
    Track which employees have valid daily files for given date

    Returns completeness percentage and missing employee list
    """
    import os
    from pathlib import Path

    dailies_root = Path(f"DAILIES/{date_str}")

    # Load employee list from TALENTS/
    expected_employees = load_active_employees()  # 29 active

    found_files = []
    missing_files = []
    corrupt_files = []

    for emp in expected_employees:
        daily_file = dailies_root / f"{emp['id']}_daily.md"

        if not daily_file.exists():
            missing_files.append({
                "employee_id": emp['id'],
                "name": emp['name'],
                "department": emp['department'],
                "issue": "file_not_found"
            })
        elif daily_file.stat().st_size == 0:
            corrupt_files.append({
                "employee_id": emp['id'],
                "name": emp['name'],
                "department": emp['department'],
                "issue": "empty_file"
            })
        else:
            found_files.append(emp['id'])

    completeness = len(found_files) / len(expected_employees) * 100

    return {
        "date": date_str,
        "completeness_pct": round(completeness, 1),
        "total_employees": len(expected_employees),
        "valid_files": len(found_files),
        "missing_files": len(missing_files),
        "corrupt_files": len(corrupt_files),
        "missing_list": missing_files,
        "corrupt_list": corrupt_files
    }
```

### Completeness Report

```markdown
## Daily Completeness Report

**Date**: 2025-11-21
**Target**: 95%+

### Overall: 76% ⚠️ BELOW TARGET

**Valid Files**: 22/29 (76%)
**Missing Files**: 5/29 (17%)
**Corrupt Files**: 2/29 (7%)

### Missing Files (5):
1. EMP-012 (Hanan) - LG Department
2. EMP-018 (Yusuf) - LG Department
3. EMP-024 (Sarah) - LG Department
4. EMP-027 (Ahmed) - Finance Department
5. EMP-029 (Maria) - Marketing Department

### Corrupt/Empty Files (2):
1. EMP-015 (Omar) - LG Department (0 bytes)
2. EMP-021 (Fatima) - LG Department (0 bytes)

### Department Breakdown:
- **LG**: 5/10 valid (50%) ❌ CRITICAL
- **AID**: 5/5 valid (100%) ✅
- **DEV**: 4/4 valid (100%) ✅
- **HRM**: 3/3 valid (100%) ✅
- **VID**: 2/2 valid (100%) ✅
- **Finance**: 2/3 valid (67%) ⚠️
- **Marketing**: 1/2 valid (50%) ⚠️

### Root Cause Analysis:
**LG Department Issues (50% failure rate)**:
- Possible automation failure in file generation
- Days-off not tracked (employees may be absent)
- File generation script issues specific to LG

**Recommendations**:
1. Cross-reference with days-off log
2. Check LG department automation scripts
3. Implement file validation in generation process
4. Add alerts for missing files
```

---

## Pattern Detection

### Identify Recurring Tasks

```python
def detect_task_patterns(date_range, min_frequency=5):
    """
    Analyze employee activities to find recurring patterns

    Cluster similar tasks across multiple employees/days
    """
    from collections import Counter
    import pandas as pd

    all_tasks = []

    # Load processed reports for date range
    for date in date_range:
        reports = load_daily_reports(date)
        for report in reports:
            tasks = extract_tasks_from_report(report)
            all_tasks.extend(tasks)

    # Normalize task descriptions
    normalized_tasks = [normalize_text(task) for task in all_tasks]

    # Count frequency
    task_freq = Counter(normalized_tasks)

    # Filter recurring patterns (≥ min_frequency)
    patterns = [
        {
            "task_pattern": task,
            "frequency": count,
            "employees_performing": count_unique_employees(task),
            "departments": get_departments_for_task(task),
            "template_candidate": count >= min_frequency
        }
        for task, count in task_freq.items()
        if count >= min_frequency
    ]

    return sorted(patterns, key=lambda x: x['frequency'], reverse=True)
```

### Pattern Report

```markdown
## Task Pattern Analysis

**Date Range**: 2025-11-15 to 2025-11-21 (7 days)
**Threshold**: ≥5 occurrences

### Top Recurring Patterns (Template Candidates):

1. **"Process CV data from job sites"**
   - Frequency: 23 occurrences
   - Employees: 4 (all HRM department)
   - Departments: HRM
   - **Recommendation**: Create TSK-072_Process_CV_Data_From_Job_Sites
   - Parent Milestone: MLT-010_CV_Screening_Setup

2. **"Review and update daily automation workflows"**
   - Frequency: 18 occurrences
   - Employees: 3 (AID department)
   - Departments: AID
   - **Recommendation**: Create TSK-073_Review_Daily_Automation_Workflows
   - Parent Milestone: MLT-002_Data_Inventory (maintenance)

3. **"Analyze video engagement metrics"**
   - Frequency: 15 occurrences
   - Employees: 2 (VID, SMM)
   - Departments: VID, SMM (cross-department)
   - **Recommendation**: Create TSK-074_Analyze_Video_Engagement_Metrics
   - Parent Milestone: MLT-004_Video_Asset_Creation

### New Template Actions:
- Submit patterns to PMT-075 for validation
- Generate task template JSON structures
- Assign TSK-072, TSK-073, TSK-074 IDs
- Link to appropriate milestones and projects
```

---

## Anomaly Detection

### Flag Unusual Activities

```python
def detect_anomalies(employee_id, date_str):
    """
    Detect unusual patterns in employee daily files
    """
    # Load employee history (last 30 days)
    history = load_employee_history(employee_id, days=30)
    current = load_daily_file(employee_id, date_str)

    anomalies = []

    # 1. Time anomaly (unusual working hours)
    avg_hours = history['avg_hours_logged']
    current_hours = current['hours_logged']

    if current_hours > avg_hours * 1.5:
        anomalies.append({
            "type": "time_anomaly",
            "severity": "medium",
            "message": f"Unusually high hours: {current_hours}h (avg: {avg_hours}h)"
        })

    # 2. Tool anomaly (new tool mentioned)
    historical_tools = set(history['tools_used'])
    current_tools = set(current['tools_used'])
    new_tools = current_tools - historical_tools

    if new_tools:
        anomalies.append({
            "type": "new_tool_detected",
            "severity": "info",
            "message": f"New tools mentioned: {new_tools}",
            "action": "Add to Tools_Master_List.csv"
        })

    # 3. Activity anomaly (unusual task type)
    typical_depts = history['typical_departments']
    current_dept_tasks = current['department_alignment']

    if current_dept_tasks not in typical_depts:
        anomalies.append({
            "type": "cross_department_activity",
            "severity": "info",
            "message": f"Working on {current_dept_tasks} tasks (typical: {typical_depts})"
        })

    # 4. Quality anomaly (very short descriptions)
    if current['avg_task_description_length'] < 20:
        anomalies.append({
            "type": "quality_issue",
            "severity": "low",
            "message": "Task descriptions are very brief (<20 chars avg)"
        })

    return anomalies
```

---

## Department-Specific Analysis

### LG Department Deep Dive

```markdown
## LG Department Analysis

**Period**: 2025-11-17 to 2025-11-21
**Issue**: 50% file completeness (5/10 valid files)

### Investigation Results:

**Missing Files**:
- EMP-012 (Hanan): Missing all 5 days
- EMP-018 (Yusuf): Missing 3/5 days
- EMP-024 (Sarah): Missing 4/5 days
- EMP-015 (Omar): Empty files 2/5 days
- EMP-021 (Fatima): Empty files 2/5 days

**Cross-Reference with Days Off**:
- EMP-012: Confirmed off Nov 18-20 (3 days explained)
- EMP-018: No days-off record (genuine missing data)
- EMP-024: Confirmed off Nov 19-21 (3 days explained)

**Automation Script Check**:
- LG department uses custom file generation script: `Scripts/lg_daily_generator.py`
- Script last modified: 2025-11-10
- **Issue Found**: Script fails silently when employee has no CRM activity
- **Fix**: Add empty file generation with "No CRM activity" note

**Recommendations**:
1. Update `lg_daily_generator.py` to handle zero-activity days
2. Implement days-off cross-referencing in file collection (script_01)
3. Add alerting for missing files (Slack/email notification)
4. Target: 95%+ completeness by 2025-11-28
```

---

## New Entity Discovery

### Extract Potential New Entities

```python
def discover_new_entities(date_range):
    """
    Scan daily files for mentions of unknown tools, actions, responsibilities
    """
    # Load all master lists
    known_tools = load_master_list("Tools")
    known_actions = load_master_list("Actions")
    known_responsibilities = load_master_list("Responsibilities")

    # Scan daily files
    potential_new_tools = []
    potential_new_actions = []
    potential_new_responsibilities = []

    for date in date_range:
        reports = load_daily_reports(date)

        for report in reports:
            # Extract tools mentioned but not in master list
            mentioned_tools = extract_tools_from_text(report['content'])
            for tool in mentioned_tools:
                if not is_in_master_list(tool, known_tools):
                    potential_new_tools.append({
                        "tool_name": tool,
                        "mentioned_by": report['employee_id'],
                        "date": date,
                        "context": get_context_sentence(report['content'], tool)
                    })

            # Extract action verbs
            actions = extract_action_verbs(report['content'])
            for action in actions:
                if not is_in_master_list(action, known_actions):
                    potential_new_actions.append({
                        "action": action,
                        "category": classify_action_category(action),  # A-G
                        "mentioned_by": report['employee_id'],
                        "date": date
                    })

    return {
        "new_tools": deduplicate(potential_new_tools),
        "new_actions": deduplicate(potential_new_actions),
        "new_responsibilities": deduplicate(potential_new_responsibilities)
    }
```

### Discovery Report

```markdown
## New Entity Discovery

**Period**: 2025-11-15 to 2025-11-21
**Source**: Employee daily files

### New Tools Detected (8):

1. **Perplexity AI** (mentioned 5 times)
   - Department: AID
   - Context: "Used Perplexity AI for research"
   - **Action**: Assign TOL-178, add to Tools_Master_List.csv

2. **Gemini Flash 2.0** (mentioned 3 times)
   - Department: AID, DEV
   - Context: "Testing Gemini Flash 2.0 for content generation"
   - **Action**: Check if different from existing TOL-089 (Gemini), assign TOL-179

[...8 total tools]

### New Actions Detected (3):

1. **"Synthesize"** (mentioned 4 times)
   - Category: C (Analysis)
   - Context: "Synthesize research findings"
   - **Action**: Review if different from "Combine" (ACT-134), assign ACT-430

[...3 total actions]

### Recommendations:
- Stage new entities via PMT-076 (Import Validation Pipeline)
- Run duplicate detection (similarity ≥0.6)
- Integrate validated entities into LIBRARIES
```

---

## Performance Metrics Dashboard

```markdown
## DAILIES Processing Metrics

**Week**: 2025-11-15 to 2025-11-21

### Processing Performance:
- **Avg Time per Employee**: 14.2 minutes
- **Total Processing Time**: 7.1 hours (sequential)
- **Projected with Parallelization** (4 workers): 1.8 hours
- **Potential Savings**: 5.3 hours (75%)

### Data Quality:
- **Completeness**: 76% (target: 95%)
- **Avg Report Length**: 3,200 words
- **Entities Extracted per Employee**: 42 (avg)
  - Actions: 12
  - Objects: 8
  - Tools: 5
  - Responsibilities: 17

### Entity Extraction Accuracy:
- **High Confidence**: 68%
- **Medium Confidence**: 24%
- **Low Confidence**: 8%

### Department Performance:
| Department | Completeness | Avg Entities | Quality Score |
|------------|--------------|--------------|---------------|
| AID        | 100%         | 58           | 9.2/10        |
| DEV        | 100%         | 45           | 8.8/10        |
| HRM        | 100%         | 38           | 8.5/10        |
| VID        | 100%         | 42           | 8.7/10        |
| LG         | 50%          | 32           | 7.1/10        |
| Finance    | 67%          | 28           | 8.0/10        |
| Marketing  | 50%          | 35           | 7.8/10        |
```

---

## Workflows

### Weekly Monitoring Workflow

1. **Monday**: Run completeness check for previous week
2. **Tuesday**: Analyze patterns, generate template candidates
3. **Wednesday**: Detect anomalies, investigate issues
4. **Thursday**: Department-specific analysis (focus on low completeness)
5. **Friday**: Discover new entities, prepare import batch
6. **Weekend**: Process improvements, update documentation

### Alerting Rules

- **Critical Alert** (Slack): Completeness <70%
- **Warning Alert** (Email): Department completeness <80%
- **Info Alert** (Log): New tools detected (≥3 mentions)

---

## Integration with Other Prompts

**PMT-075 (Data Integrity)**: Validate discovered entities before import
**PMT-076 (Import Pipeline)**: Stage new entities for integration
**PMT-078 (Cross Entity Search)**: Find related entities for new discoveries

---

## Version History

**v1.0** (2025-11-21)
- Initial version
- Completeness tracking (76% → 95% target)
- Pattern detection for task templates
- Anomaly detection
- Department-specific analysis
- New entity discovery
- Performance metrics

---

**Status:** Active
**Maintained By:** AI & Automation Department

---

**End of Prompt**
