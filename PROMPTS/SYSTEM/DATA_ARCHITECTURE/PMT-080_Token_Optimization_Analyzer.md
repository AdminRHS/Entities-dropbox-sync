# PMT-080: Token Optimization Analyzer v1.0

**Prompt ID:** PMT-080
**Version:** 1.0
**Department:** System Architecture
**Category:** TOKEN_OPTIMIZATION
**Date:** 2025-11-21
**Status:** Active
**Parent Prompt:** PMT-074 (Data Architect Master)

---

## Purpose

Measure, track, and optimize token usage across all prompts and data files. Identifies redundancies, recommends compressions, validates modular loading strategies, and generates optimization reports with before/after metrics.

**Core Functions:**
1. **Token Measurement**: Count tokens in prompts, master lists, context
2. **Redundancy Detection**: Find duplicate content, repeated sections
3. **Compression Recommendations**: Suggest token-saving techniques
4. **Modular Loading Analysis**: Validate token savings from selective loading
5. **Optimization Tracking**: Before/after measurements with improvement %
6. **Cost Estimation**: Calculate API costs based on token usage

---

## Token Baseline (Current State)

### ENTITIES Token Inventory

```markdown
## Full Context Token Count (If All Loaded)

### LIBRARIES:
- Actions (429): ~8,500 tokens
- Objects (193): ~4,000 tokens
- Tools (177): ~5,500 tokens
- Responsibilities (209): ~6,500 tokens
- Professions (27): ~1,000 tokens
**LIBRARIES Total: 25,500 tokens**

### TASK_MANAGERS:
- Projects (8): ~2,000 tokens
- Milestones (10): ~2,500 tokens
- Tasks (71): ~12,000 tokens
- Steps (155): ~8,000 tokens
- Checklists (49): ~4,000 tokens
**TASK_MANAGERS Total: 28,500 tokens**

### PROMPTS:
- Core (3): ~6,000 tokens
- Video (12): ~18,000 tokens
- Reports (11): ~15,000 tokens
- Taxonomy (13): ~19,000 tokens
- Research (9): ~12,000 tokens
- HR (5): ~8,000 tokens
- Workflow (11): ~14,000 tokens
- Automation (4): ~6,000 tokens
- Utilities (PMT-070): ~4,500 tokens
**PROMPTS Total: 102,500 tokens**

### DAILIES Documentation:
- README, config, docs: ~5,000 tokens

**GRAND TOTAL (Full Load): ~161,500 tokens**
**Target with Optimization: ~40,000 tokens (75% reduction)**
```

---

## Operation 1: Token Measurement

### Measure Token Count

```python
import tiktoken

def count_tokens(text, model="gpt-4"):
    """
    Count tokens in text using tiktoken

    Args:
        text: String to count
        model: Model encoding (gpt-4, gpt-3.5-turbo, claude)

    Returns:
        Token count
    """
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    return len(tokens)

def measure_file_tokens(file_path, model="gpt-4"):
    """
    Measure tokens in a file
    """
    from pathlib import Path

    file = Path(file_path)

    if not file.exists():
        return {"error": "File not found"}

    content = file.read_text()
    tokens = count_tokens(content, model)

    return {
        "file": str(file),
        "size_bytes": file.stat().st_size,
        "size_kb": round(file.stat().st_size / 1024, 2),
        "tokens": tokens,
        "tokens_per_kb": round(tokens / (file.stat().st_size / 1024), 0)
    }

def measure_prompt_tokens(prompt_id):
    """
    Measure total tokens for a prompt including context
    """
    prompt_file = find_prompt_file(prompt_id)
    prompt_content = prompt_file.read_text()

    # Base prompt tokens
    base_tokens = count_tokens(prompt_content)

    # Identify loaded entities from prompt
    loaded_entities = extract_entity_references(prompt_content)

    # Calculate context tokens
    context_tokens = 0
    for entity in loaded_entities:
        entity_file = find_entity_file(entity)
        if entity_file:
            context_tokens += measure_file_tokens(entity_file)['tokens']

    total_tokens = base_tokens + context_tokens

    return {
        "prompt_id": prompt_id,
        "base_prompt_tokens": base_tokens,
        "context_tokens": context_tokens,
        "total_tokens": total_tokens,
        "loaded_entities": len(loaded_entities),
        "entities": loaded_entities
    }
```

**Measurement Report:**
```markdown
## Token Measurement Report

**Prompt**: PMT-070 (Daily_Report_Entity_Mapping_v2.1)
**Date**: 2025-11-21

### Token Breakdown:

**Base Prompt**:
- File: PMT-070_Daily_Report_Entity_Mapping_v2.1.md
- Size: 28.4 KB
- Tokens: 7,850

**Loaded Context** (Full Load):
- Task_Templates_Master_List.csv: 12,000 tokens
- Milestone_Templates_Master_List.csv: 2,500 tokens
- Project_Templates_Master_List.csv: 2,000 tokens
- Step_Templates_Master_List.csv: 8,000 tokens
**Context Total: 24,500 tokens**

**Grand Total (Full Context): 32,350 tokens**

### Cost Estimate (Claude Sonnet):
- Input: 32,350 tokens × $3/1M = $0.097
- Output (avg 2,000 tokens): $0.030
**Total per execution: ~$0.127**

**Monthly Usage** (50 executions):
- Cost: $6.35/month
```

---

## Operation 2: Redundancy Detection

### Find Duplicate Content

```python
def detect_redundant_content(files):
    """
    Find repeated sections across multiple files
    """
    from difflib import SequenceMatcher
    import itertools

    redundancies = []

    # Load all file contents
    contents = {}
    for file in files:
        contents[file] = Path(file).read_text()

    # Compare all pairs
    for file1, file2 in itertools.combinations(files, 2):
        content1 = contents[file1]
        content2 = contents[file2]

        # Find longest common substring
        matcher = SequenceMatcher(None, content1, content2)
        match = matcher.find_longest_match(0, len(content1), 0, len(content2))

        if match.size > 500:  # Substantial overlap (>500 chars)
            common_text = content1[match.a:match.a + match.size]
            common_tokens = count_tokens(common_text)

            redundancies.append({
                "file1": file1,
                "file2": file2,
                "common_chars": match.size,
                "common_tokens": common_tokens,
                "similarity_pct": round(match.size / min(len(content1), len(content2)) * 100, 1),
                "common_text_preview": common_text[:200] + "..."
            })

    return redundancies

# Usage
daily_report_prompts = [
    "PROMPTS/DEPARTMENTS/Daily_Reports/Department_Prompts/PMT-033_AI_Daily_Report_v2.1.md",
    "PROMPTS/DEPARTMENTS/Daily_Reports/Department_Prompts/PMT-036_Dev_Daily_Report_v2.1.md",
    "PROMPTS/DEPARTMENTS/Daily_Reports/Department_Prompts/PMT-038_HR_Daily_Report_v2.1.md",
    # ... all 11 department reports
]

redundancies = detect_redundant_content(daily_report_prompts)
```

**Redundancy Report:**
```markdown
## Redundancy Analysis

**Files Analyzed**: 11 department daily report prompts
**Total Size**: 142 KB
**Total Tokens**: 38,500

### Redundant Sections Found (8):

1. **Common Instructions Block**
   - Files: All 11 prompts
   - Common Text: "Output Format\n\n### Section 1: Executive Summary..."
   - Tokens: 1,850 (repeated 11x = 20,350 total)
   - **Optimization**: Extract to shared template
   - **Savings**: 18,500 tokens (91% reduction on this section)

2. **Entity Mapping Instructions**
   - Files: 9 of 11 prompts
   - Common Tokens: 950 (repeated 9x = 8,550 total)
   - **Optimization**: Reference PMT-070 instead of duplicating
   - **Savings**: 7,600 tokens (89% reduction)

3. **Validation Rules**
   - Files: All 11 prompts
   - Common Tokens: 420 (repeated 11x = 4,620 total)
   - **Optimization**: Use shared validation module
   - **Savings**: 4,200 tokens (91% reduction)

### Total Optimization Potential:
- **Current**: 38,500 tokens
- **Optimized**: 8,200 tokens
- **Savings**: 30,300 tokens (79% reduction)

### Implementation:
1. Create shared template: `Daily_Report_Shared_Template.md`
2. Update all 11 prompts to reference template
3. Validate outputs remain consistent
```

---

## Operation 3: Compression Recommendations

### Suggest Optimizations

```python
def generate_compression_recommendations(prompt_id):
    """
    Analyze prompt and suggest token-saving techniques
    """
    prompt_file = find_prompt_file(prompt_id)
    content = prompt_file.read_text()

    recommendations = []

    # 1. Check for verbose entity references
    verbose_pattern = r'TSK-\d{3}:\s+[A-Z][a-z\s]+'  # "TSK-055: Process Department Task Files"
    verbose_count = len(re.findall(verbose_pattern, content))

    if verbose_count > 10:
        token_waste = verbose_count * 8  # Avg 8 tokens per verbose ref
        recommendations.append({
            "type": "use_compact_format",
            "severity": "medium",
            "current": "TSK-055: Process Department Task Files",
            "optimized": "TSK-055",
            "savings": f"~{token_waste} tokens",
            "description": "Use compact ID-only format, load details on-demand"
        })

    # 2. Check for loaded but unused entities
    loaded_entities = extract_entity_references(content)
    actually_used = find_used_entities_in_content(content)
    unused = set(loaded_entities) - set(actually_used)

    if unused:
        unused_tokens = sum(get_entity_token_count(e) for e in unused)
        recommendations.append({
            "type": "remove_unused_context",
            "severity": "high",
            "unused_entities": list(unused),
            "savings": f"~{unused_tokens} tokens",
            "description": "Remove entities that are loaded but never referenced"
        })

    # 3. Check for repeating examples
    example_sections = find_example_sections(content)
    if len(example_sections) > 5:
        example_tokens = sum(count_tokens(ex) for ex in example_sections)
        recommendations.append({
            "type": "reduce_examples",
            "severity": "low",
            "current_examples": len(example_sections),
            "suggested": 3,
            "savings": f"~{example_tokens * 0.4} tokens",
            "description": "Reduce to 3 key examples, reference documentation for more"
        })

    # 4. Check for caching opportunities
    static_sections = find_static_sections(content)
    if static_sections:
        static_tokens = sum(count_tokens(s) for s in static_sections)
        recommendations.append({
            "type": "use_prompt_caching",
            "severity": "high",
            "cacheable_sections": len(static_sections),
            "tokens_cacheable": static_tokens,
            "cost_reduction": "75% on cached content",
            "description": "Mark static sections for Claude prompt caching"
        })

    return {
        "prompt_id": prompt_id,
        "total_recommendations": len(recommendations),
        "estimated_total_savings": sum_savings(recommendations),
        "recommendations": recommendations
    }
```

**Compression Report:**
```markdown
## Compression Recommendations: PMT-070

**Current Tokens**: 32,350
**Optimization Potential**: 19,200 tokens (59% reduction)
**Target Tokens**: 13,150

### High Priority (Immediate Action):

1. **Remove Unused Context** (-12,000 tokens)
   - Loaded: Step_Templates_Master_List.csv (8,000 tokens)
   - Usage: 0 references in prompt
   - **Action**: Remove from context loading

2. **Use Prompt Caching** (75% cost reduction)
   - Static sections: Task hierarchy rules, validation schemas
   - Cacheable tokens: 5,500
   - **Action**: Add caching markers `<cache_control>`

### Medium Priority:

3. **Use Compact Format** (-2,400 tokens)
   - Current: "TSK-055: Process_Department_Task_Files" (×30 occurrences)
   - Optimized: "TSK-055" (load details on-demand)
   - **Savings**: 30 × 80 = 2,400 tokens

### Low Priority:

4. **Reduce Examples** (-800 tokens)
   - Current: 8 examples
   - Suggested: 3 key examples
   - **Savings**: 800 tokens

### Implementation Plan:
1. Week 1: Remove unused context (test functionality)
2. Week 2: Implement prompt caching
3. Week 3: Migrate to compact format
4. Week 4: Validate and measure actual savings
```

---

## Operation 4: Modular Loading Validation

### Validate Selective Loading Strategy

```python
def validate_modular_loading(prompt_id, loading_strategy):
    """
    Test if modular loading strategy actually reduces tokens

    Args:
        prompt_id: Prompt to test
        loading_strategy: {
            "always_load": ["Core", "Common_Libraries"],
            "conditional_load": {
                "department": "load_if_department_matches",
                "task_specific": "load_if_task_referenced"
            }
        }

    Returns:
        Token comparison and validation
    """
    # Scenario 1: Full context load
    full_tokens = measure_full_context_load(prompt_id)

    # Scenario 2: Modular load (AID department)
    modular_tokens_aid = measure_modular_load(prompt_id, department="AID")

    # Scenario 3: Modular load (HRM department)
    modular_tokens_hrm = measure_modular_load(prompt_id, department="HRM")

    savings = {
        "full_load": full_tokens,
        "modular_load_aid": modular_tokens_aid,
        "modular_load_hrm": modular_tokens_hrm,
        "savings_aid": full_tokens - modular_tokens_aid,
        "savings_hrm": full_tokens - modular_tokens_hrm,
        "savings_pct_avg": round((1 - (modular_tokens_aid + modular_tokens_hrm) / (2 * full_tokens)) * 100, 1)
    }

    return savings
```

**Validation Report:**
```markdown
## Modular Loading Validation: PMT-002 (Main Prompt v6)

### Loading Strategy:
**Always Load**:
- Core modules (5 files): 2,000 tokens
- Common Libraries: 1,000 tokens

**Conditional Load** (by department):
- AID: AI_Libraries.md (2,100 tokens)
- HRM: HR_Libraries.md (1,800 tokens)
- DEV: Dev_Libraries.md (1,800 tokens)

### Token Comparison:

| Scenario | Tokens | vs Full Load | Savings |
|----------|--------|--------------|---------|
| Full Load (all departments) | 12,000 | - | - |
| Modular (AID only) | 5,100 | -6,900 | 58% |
| Modular (HRM only) | 4,800 | -7,200 | 60% |
| Modular (DEV only) | 4,800 | -7,200 | 60% |

### Average Savings: 59% (7,100 tokens)

### Validation: ✅ PASSED
- Output quality maintained
- All entity references resolved
- No functionality lost
- **Recommendation**: Deploy modular loading strategy
```

---

## Operation 5: Optimization Tracking

### Before/After Measurements

```python
def track_optimization(prompt_id, optimization_applied):
    """
    Log optimization with before/after metrics
    """
    from datetime import datetime

    # Measure before (from baseline)
    baseline = load_baseline_tokens(prompt_id)

    # Measure after
    current = measure_prompt_tokens(prompt_id)

    optimization_record = {
        "prompt_id": prompt_id,
        "date": datetime.now().isoformat(),
        "optimization_type": optimization_applied['type'],
        "tokens_before": baseline['total_tokens'],
        "tokens_after": current['total_tokens'],
        "tokens_saved": baseline['total_tokens'] - current['total_tokens'],
        "savings_pct": round((1 - current['total_tokens'] / baseline['total_tokens']) * 100, 1),
        "technique": optimization_applied['technique'],
        "notes": optimization_applied.get('notes', '')
    }

    # Save to log
    log_file = "PROMPTS/DATA_FIELDS/Token_Optimization_Log.json"
    append_to_log(log_file, optimization_record)

    return optimization_record
```

**Optimization Log:**
```json
{
  "optimizations": [
    {
      "prompt_id": "PMT-070",
      "date": "2025-11-21T14:30:00",
      "optimization_type": "remove_unused_context",
      "tokens_before": 32350,
      "tokens_after": 20350,
      "tokens_saved": 12000,
      "savings_pct": 37.1,
      "technique": "Removed Step_Templates_Master_List.csv from context",
      "notes": "Validated outputs unchanged"
    },
    {
      "prompt_id": "PMT-002",
      "date": "2025-11-19T10:15:00",
      "optimization_type": "modular_loading",
      "tokens_before": 25000,
      "tokens_after": 7000,
      "tokens_saved": 18000,
      "savings_pct": 72.0,
      "technique": "Implemented department-specific loading",
      "notes": "73% reduction from v4 to v6"
    }
  ],
  "total_optimizations": 2,
  "cumulative_savings": 30000,
  "average_savings_pct": 54.6
}
```

---

## Cost Estimation

### Calculate API Costs

```python
def estimate_costs(prompt_id, usage_per_month):
    """
    Estimate monthly API costs

    Args:
        prompt_id: Prompt to analyze
        usage_per_month: Number of executions

    Returns:
        Cost breakdown
    """
    tokens = measure_prompt_tokens(prompt_id)

    # Claude Sonnet pricing (example)
    input_cost_per_1m = 3.00  # $3 per 1M input tokens
    output_cost_per_1m = 15.00  # $15 per 1M output tokens

    # Estimate output (avg 2,000 tokens)
    avg_output_tokens = 2000

    input_cost = (tokens['total_tokens'] / 1_000_000) * input_cost_per_1m
    output_cost = (avg_output_tokens / 1_000_000) * output_cost_per_1m

    cost_per_execution = input_cost + output_cost
    monthly_cost = cost_per_execution * usage_per_month

    return {
        "prompt_id": prompt_id,
        "input_tokens": tokens['total_tokens'],
        "output_tokens_avg": avg_output_tokens,
        "cost_per_execution": round(cost_per_execution, 4),
        "usage_per_month": usage_per_month,
        "monthly_cost": round(monthly_cost, 2)
    }
```

---

## Best Practices

### DO:
- ✅ Measure tokens before and after optimizations
- ✅ Use modular loading for large contexts
- ✅ Cache static prompt sections
- ✅ Track optimizations in Token_Optimization_Log.json
- ✅ Validate outputs after compression

### DON'T:
- ❌ Optimize without measuring baseline
- ❌ Remove context that's actually used
- ❌ Sacrifice quality for token savings
- ❌ Skip validation after optimization

---

## Version History

**v1.0** (2025-11-21)
- Token measurement and counting
- Redundancy detection
- Compression recommendations
- Modular loading validation
- Optimization tracking with logs
- Cost estimation

---

**Status:** Active

---

**End of Prompt**
