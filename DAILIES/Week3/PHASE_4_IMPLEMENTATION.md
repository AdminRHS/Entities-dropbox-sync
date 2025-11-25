# Phase 4 Implementation Guide
**Version:** 1.0
**Date:** 2025-11-20
**Purpose:** Complete guide for PMT-070 Phase 4: Task Hierarchy Formation & Granularity Classification

---

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Scripts](#scripts)
4. [Usage Guide](#usage-guide)
5. [Output Format](#output-format)
6. [Configuration](#configuration)
7. [Testing](#testing)
8. [Troubleshooting](#troubleshooting)

---

## Overview

Phase 4 transforms Phase 3 responsibilities into a three-tier task hierarchy:

- **Checklist Items** (< 2 min, atomic actions)
- **Step Templates** (3-10 min, execution units)
- **Task Templates** (30min-4hr, complete deliverables)

### Key Features

1. **Granularity Classification** - Automated tier assignment based on complexity scoring
2. **Bottom-Up Promotion** - Groups 2+ related steps into tasks
3. **Top-Down Decomposition** - Breaks vague tasks into concrete steps
4. **Pattern-Based Tool Inference** - Maps actions to likely tools
5. **Manual Review Workflow** - Flags complex items for validation

### Token Efficiency

Phase 4 adds ~400 tokens to Phase 3 output:
- Phase 3: 1,200 tokens
- Phase 4: 1,600 tokens
- **Total Reduction: 65%** from Phase 2 baseline (4,600 tokens)

---

## Architecture

### Pipeline Flow

```
Phase 3 JSON
    |
    v
[Script 14] Granularity Classifier
    |
    v
[Script 15] Bottom-Up Promoter
    |
    v
[Script 16] Top-Down Decomposer
    |
    v
[Script 17] Checklist Generator
    |
    v
[Script 18] Phase 4 Integrator
    |
    v
Final JSON + Manual Review Report
```

### Data Flow

1. **Input**: `phase_3_structured_daily_{id}.json`
2. **Intermediate**:
   - `phase_4_classified_daily_{id}.json`
   - `phase_4_promoted_daily_{id}.json`
   - `phase_4_decomposed_daily_{id}.json`
   - `phase_4_checklist_daily_{id}.json`
3. **Output**:
   - `phase_4_final_daily_{id}.json`
   - `phase_4_review_daily_{id}.md`

---

## Scripts

### Script 14: Granularity Classifier

**File**: [scripts/script_14_granularity_classifier.py](scripts/script_14_granularity_classifier.py)

**Purpose**: Classify responsibilities into checklist/step/task tiers

**Algorithm**:
```python
granularity_score = (
    verb_complexity * 0.4 +
    object_complexity * 0.3 +
    tool_complexity * 0.2 +
    frequency_impact * 0.1
)

if score < 0.3: tier = "checklist_item"
elif score < 0.7: tier = "step_template"
else: tier = "task_template"
```

**Usage**:
```bash
python scripts/script_14_granularity_classifier.py --employee 228
```

**Key Functions**:
- `classify_responsibility()` - Main classification logic
- `calculate_granularity_score()` - Scoring formula
- `is_atomic_action()` - Detect checklist items
- `is_execution_unit()` - Detect steps
- `is_complete_deliverable()` - Detect tasks

---

### Script 15: Bottom-Up Promoter

**File**: [scripts/script_15_bottom_up_promoter.py](scripts/script_15_bottom_up_promoter.py)

**Purpose**: Group 2+ related step templates into task templates

**Algorithm**:
```python
similarity = (
    same_domain_score * 0.3 +
    sequential_flow_score * 0.3 +
    shared_tools_score * 0.2 +
    common_goal_score * 0.2
)

if similarity >= 0.6 and len(group) >= 2:
    promote_to_task()
```

**Usage**:
```bash
python scripts/script_15_bottom_up_promoter.py
```

**Key Functions**:
- `group_similar_steps()` - Similarity-based grouping
- `calculate_similarity()` - Pairwise similarity scoring
- `should_promote()` - Promotion criteria check
- `create_task_from_steps()` - Task generation

---

### Script 16: Top-Down Decomposer

**File**: [scripts/script_16_top_down_decomposer.py](scripts/script_16_top_down_decomposer.py)

**Purpose**: Decompose vague tasks into concrete step sequences

**Algorithm**:
```python
vagueness_score = (
    has_vague_verb * 0.3 +
    has_abstract_object * 0.2 +
    no_tools_specified * 0.2 +
    skill_level_high * 0.3
)

if vagueness_score >= 0.6:
    decompose_using_pattern()
```

**Decomposition Patterns**:
- `create`: research → design → implement → test → document
- `manage`: assess → plan → execute → monitor → adjust
- `integrate`: review → configure → test → validate → troubleshoot
- `deploy`: review → configure → execute → validate → document
- `develop`: design → implement → test → refine → deploy
- `setup`: plan → configure → test → document

**Usage**:
```bash
python scripts/script_16_top_down_decomposer.py
```

**Key Functions**:
- `calculate_vagueness_score()` - Vagueness detection
- `decompose_task()` - Pattern-based decomposition
- `select_pattern()` - Pattern matching
- `infer_tool()` - Tool inference from patterns

---

### Script 17: Checklist Generator

**File**: [scripts/script_17_checklist_generator.py](scripts/script_17_checklist_generator.py)

**Purpose**: Generate checklist items from atomic responsibilities

**Duration Mapping**:
```python
DURATION_MAP = {
    'click': '10 seconds',
    'open': '30 seconds',
    'save': '15 seconds',
    'upload': '1-2 minutes',
    'download': '1-2 minutes',
    'login': '30 seconds',
    # ... etc
}
```

**Usage**:
```bash
python scripts/script_17_checklist_generator.py
```

**Key Functions**:
- `create_checklist_item()` - Item generation
- `estimate_duration()` - Duration assignment

---

### Script 18: Phase 4 Integrator

**File**: [scripts/script_18_phase4_integrator.py](scripts/script_18_phase4_integrator.py)

**Purpose**: Orchestrate complete Phase 4 pipeline and produce final output

**Features**:
- Run all scripts in sequence
- Validate task hierarchy
- Generate manual review report
- Create final integrated JSON

**Usage**:
```bash
# Run complete pipeline from Phase 3 input
python scripts/script_18_phase4_integrator.py --run-full-pipeline --employee 228

# Or integrate existing Phase 4 data
python scripts/script_18_phase4_integrator.py
```

**Key Functions**:
- `integrate()` - Component integration
- `validate_hierarchy()` - Relationship validation
- `generate_manual_review_report()` - Markdown report

---

## Usage Guide

### Quick Start

**1. Run Complete Pipeline**:
```bash
cd C:\Users\Dell\Dropbox\ENTITIES\DAILIES
python scripts/script_18_phase4_integrator.py --run-full-pipeline --employee 228
```

**2. Check Outputs**:
```
Processed/Phase_4_Output/
├── phase_4_final_daily_228.json
└── phase_4_review_daily_228.md
```

**3. Review Manual Items**:
```bash
# Open review report
notepad Processed/Phase_4_Output/phase_4_review_daily_228.md
```

### Step-by-Step Execution

If you need to run scripts individually:

```bash
# Step 1: Classify
python scripts/script_14_granularity_classifier.py --employee 228

# Step 2: Promote
python scripts/script_15_bottom_up_promoter.py

# Step 3: Decompose
python scripts/script_16_top_down_decomposer.py

# Step 4: Generate Checklists
python scripts/script_17_checklist_generator.py

# Step 5: Integrate
python scripts/script_18_phase4_integrator.py
```

### Processing Multiple Files

```bash
# Process all Phase 3 files
for file in Processed/Phase_3_Output/phase_3_structured_daily_*.json; do
    python scripts/script_18_phase4_integrator.py --run-full-pipeline --input "$file"
done
```

---

## Output Format

### Final JSON Schema

```json
{
  "metadata": {
    "version": "1.0",
    "phase": "phase_4_final",
    "script": "script_18_phase4_integrator.py",
    "employee_id": "228",
    "date": "2025-11-20",
    "processed_date": "2025-11-20 10:52:33",
    "pipeline_version": "PMT-070-P4-v1.0"
  },
  "checklist_items": [
    {
      "checklist_item_id": "CHK-DAY-228-001",
      "item_name": "Open file",
      "item_type": "substep",
      "action": "open",
      "object": "file",
      "tool": "File Explorer",
      "estimated_duration": "30 seconds",
      "source_responsibility": "RESP-001",
      "granularity_score": 0.15,
      "classification_confidence": 0.95
    }
  ],
  "step_templates": [
    {
      "resp_id": "RESP-005",
      "signature": "create_document_with_word",
      "action": "create",
      "objects": ["document"],
      "tools": ["word"],
      "frequency": 3,
      "form_distribution": {"base": 1, "ing": 1, "ed": 1},
      "classification": "ongoing_work",
      "skill_level": "intermediate",
      "granularity_tier": "step_template",
      "granularity_score": 0.45,
      "classification_confidence": 0.85
    }
  ],
  "task_templates": [
    {
      "task_template_id": "TASK-BU-001",
      "task_template_name": "Create Project Documentation",
      "action": "create",
      "object": "documentation",
      "context": "for better discoverability",
      "estimated_duration": "1-2 hours",
      "steps_template": [
        {"step_id": "RESP-005", "step_number": 1},
        {"step_id": "RESP-007", "step_number": 2}
      ],
      "tools_required": ["word", "markdown"],
      "objects_involved": ["document", "readme"],
      "source_responsibilities": ["RESP-005", "RESP-007"],
      "classification": {
        "tier": "task_template",
        "method": "bottom_up",
        "grouped_count": 2,
        "confidence": 0.7
      },
      "requires_manual_review": false
    }
  ],
  "task_decompositions": [
    {
      "task_id": "TASK-001",
      "task_name": "Manage Project Workflow",
      "original_action": "manage",
      "original_object": "workflow",
      "vagueness_score": 0.7,
      "decomposition_pattern": "manage",
      "steps": [
        {
          "step_id": "TASK-001-STEP-01",
          "step_number": 1,
          "step_name": "Assess workflow status",
          "action": "assess",
          "object": "workflow",
          "tool": "Assessment Tool",
          "estimated_duration": "20 minutes"
        }
      ],
      "requires_manual_review": true
    }
  ],
  "statistics": {
    "checklist_items": 5,
    "step_templates": 12,
    "task_templates": 3,
    "tasks_promoted": 2,
    "tasks_decomposed": 1,
    "manual_review_count": 3
  },
  "manual_review_required": {
    "complex_promotions": [
      {
        "task_id": "TASK-BU-003",
        "reason": "Complex promotion: 5 steps grouped",
        "step_count": 5
      }
    ],
    "decompositions": [
      {
        "task_id": "TASK-001",
        "reason": "High vagueness score: 0.75",
        "vagueness_score": 0.75
      }
    ]
  },
  "validation": {
    "hierarchy_valid": true,
    "errors": []
  }
}
```

### Manual Review Report Format

```markdown
# Phase 4 Manual Review Report
**Generated:** 2025-11-20 10:52:33
**Employee:** 228

---

## High Priority

Complex task promotions requiring validation:

- **TASK-BU-003**
  - Reason: Complex promotion: 5 steps grouped
  - Step Count: 5

## Task Decompositions

Vague tasks decomposed into step sequences:

- **TASK-001**
  - Reason: High vagueness score: 0.75
  - Vagueness Score: 0.75

---

**Total Items for Review:** 2
```

---

## Configuration

### config.json (v1.2)

```json
{
  "version": "1.2",
  "paths": {
    "phase_4_output": "./Processed/Phase_4_Output",
    "logs": "../LOG"
  },
  "prompts": {
    "pmt_070_phase_4": "UTILITIES/Daily_Updates/PMT-070_Phase_4_Task_Hierarchy.md"
  },
  "phase_4": {
    "granularity_thresholds": {
      "checklist_item": 0.3,
      "step_template": 0.7,
      "task_template": 1.0
    },
    "vagueness_threshold": 0.6,
    "similarity_threshold": 0.6,
    "min_steps_for_promotion": 2,
    "max_steps_for_task": 8,
    "duration_estimates": {
      "checklist_item": "< 2 minutes",
      "step_template": "3-10 minutes",
      "task_template": "30 minutes - 4 hours"
    },
    "manual_review_triggers": {
      "high_vagueness_score": 0.7,
      "low_confidence": 0.7,
      "complex_promotion": 4
    }
  }
}
```

### Adjusting Thresholds

To modify classification behavior:

1. **Granularity Thresholds**: Adjust tier boundaries
   - Lower checklist_item threshold → More atomic items
   - Higher task_template threshold → Fewer complex tasks

2. **Vagueness Threshold**: Control decomposition trigger
   - Lower threshold → More aggressive decomposition
   - Higher threshold → Only very vague tasks decomposed

3. **Similarity Threshold**: Adjust bottom-up grouping
   - Lower threshold → More aggressive grouping
   - Higher threshold → Stricter grouping

4. **Min Steps for Promotion**: Minimum group size
   - Default: 2 (user-confirmed)
   - Increase to require more evidence of relationship

---

## Testing

### Test Dataset

Use [phase_2_test_verb_forms.md](Processed/Phase_2_Output/phase_2_test_verb_forms.md) as test input.

### Validation Checklist

- [ ] All scripts execute without errors
- [ ] Session logs created in `LOG/` directory
- [ ] Phase 4 output directory created
- [ ] Final JSON validates against schema
- [ ] Manual review report generated
- [ ] Hierarchy validation passes
- [ ] Token count within expected range (~1,600)

### Test Commands

```bash
# Test individual scripts
python scripts/script_14_granularity_classifier.py --input "Processed/Phase_3_Output/phase_3_structured_daily_phase_2_test_verb_forms.json"

python scripts/script_15_bottom_up_promoter.py

python scripts/script_16_top_down_decomposer.py

python scripts/script_17_checklist_generator.py

# Test full pipeline
python scripts/script_18_phase4_integrator.py --run-full-pipeline --input "Processed/Phase_3_Output/phase_3_structured_daily_phase_2_test_verb_forms.json"
```

### Expected Results

For test file with 16 responsibilities:
- **Checklist Items**: 3-8
- **Step Templates**: 6-13
- **Task Templates**: 0-2 (promoted)
- **Decompositions**: 0-1
- **Execution Time**: < 5 seconds (total pipeline)

---

## Troubleshooting

### Common Issues

**Issue**: No Phase 3 input files found

**Solution**:
```bash
# Check Phase 3 output directory
dir Processed\Phase_3_Output

# Run Phase 3 first if needed
python scripts/script_12_phase3_data_structurer.py --employee 228
```

---

**Issue**: Unicode encoding errors

**Solution**: Ensure all output uses `encoding='utf-8'`:
```python
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
```

---

**Issue**: Validation errors in hierarchy

**Check**:
1. ID uniqueness across all tiers
2. Parent-child references exist
3. No circular dependencies
4. Step IDs referenced in tasks exist

**Debug**:
```python
# Check validation results
with open('Processed/Phase_4_Output/phase_4_final_daily_228.json') as f:
    data = json.load(f)
    print(data['validation']['errors'])
```

---

**Issue**: No tasks promoted (bottom-up)

**Explanation**: Test data may not have similar enough steps to group.

**Verify**: Check similarity scores in logs:
```bash
# Look for similarity calculations in session log
cat LOG/session_*_15_bottom_up_promoter.md
```

---

**Issue**: No tasks decomposed (top-down)

**Explanation**: No tasks exceeded vagueness threshold (0.6).

**Verify**: Check vagueness scores:
```python
# Inspect task vagueness scores
tasks = data['classifications']['task_templates']
for task in tasks:
    print(f"{task['resp_id']}: vagueness={task.get('vagueness_score', 0.0)}")
```

---

**Issue**: Session logs not created

**Check**:
1. LOG directory exists: `C:\Users\Dell\Dropbox\ENTITIES\LOG`
2. utils_session_logger.py imported correctly
3. Permissions to write to LOG directory

**Fix**:
```bash
# Create LOG directory if missing
mkdir C:\Users\Dell\Dropbox\ENTITIES\LOG
```

---

### Performance Optimization

**Slow similarity calculations**:
- Use NumPy for vectorized operations
- Cache similarity scores
- Limit pairwise comparisons (consider clustering first)

**Large datasets**:
- Process in batches
- Use parallel processing (update `config.json`)
- Filter low-frequency responsibilities

---

## Session Logging

All Phase 4 scripts automatically log to `ENTITIES/LOG/`:

```
LOG/
├── session_2025-11-20_02-13_phase4_14_granularity_classifier.md
├── session_2025-11-20_09-55_phase4_15_bottom_up_promoter.md
├── session_2025-11-20_10-16_phase4_16_top_down_decomposer.md
├── session_2025-11-20_10-34_phase4_17_checklist_generator.md
└── session_2025-11-20_10-52_phase4_18_phase4_integrator.md
```

Logs older than 30 days are automatically archived to `LOG/archive/{year-month}/`.

---

## Next Steps

### Phase 5 Preview: Task Manager Population

After Phase 4 manual review completes:

1. Approve validated task templates
2. Run [script_13_tm_populator.py](scripts/script_13_tm_populator.py) with `--approve` flag
3. Populate `TASK_MANAGERS/` folder structure
4. Generate employee profiles and department aggregates

**Command**:
```bash
python scripts/script_13_tm_populator.py --employee 228 --approve
```

---

## Version History

**v1.0** - 2025-11-20
- Initial Phase 4 implementation
- 5 pipeline scripts (14-18)
- Three-tier classification system
- Bottom-up promotion (min 2 steps)
- Top-down decomposition (threshold 0.6)
- Pattern-based tool inference
- Automatic session logging
- Manual review workflow

---

**Questions or Issues?**

Refer to:
- [PMT-070_Phase_4_Task_Hierarchy.md](C:/Users/Dell/Dropbox/ENTITIES/PROMPTS/UTILITIES/Daily_Updates/PMT-070_Phase_4_Task_Hierarchy.md) - Complete specifications
- [Session logs](C:/Users/Dell/Dropbox/ENTITIES/LOG/) - Execution history
- [config.json](scripts/config.json) - Configuration settings

**END OF PHASE 4 IMPLEMENTATION GUIDE**
