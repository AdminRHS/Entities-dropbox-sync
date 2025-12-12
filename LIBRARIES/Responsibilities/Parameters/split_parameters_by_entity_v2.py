#!/usr/bin/env python3
"""
Parameter Entity Splitting - Version 2 (Enhanced)
Loads actual entity libraries to improve classification accuracy
"""

import json
import os
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Base paths
BASE_PATH = Path(r"c:\Users\Dell\Dropbox\ENTITIES\LIBRARIES")
PARAMS_PATH = BASE_PATH / "Responsibilities" / "Parameters"
OUTPUT_BASE = PARAMS_PATH

# Entity library paths
ACTIONS_PATH = BASE_PATH / "Responsibilities" / "Actions" / "Master" / "actions_master.json"
OBJECTS_PATH = BASE_PATH / "Responsibilities" / "Objects" / "object_types.json"
TOOLS_PATH = BASE_PATH / "Archive" / "Legacy_Root_Files" / "tools.json"

def load_json(filepath):
    """Load JSON file with proper encoding"""
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        return json.load(f)

def extract_action_keywords(actions_data):
    """Extract keywords from Actions library"""
    keywords = set()

    # Extract base action verbs
    for action in actions_data.get('actions', []):
        action_verb = action.get('action', '')
        if action_verb:
            keywords.add(action_verb.lower())

            # Add process and result forms
            forms = action.get('forms', {})
            for process_form in forms.get('processes', []):
                keywords.add(process_form.lower())
            for result_form in forms.get('results', []):
                keywords.add(result_form.lower())

    return keywords

def extract_object_keywords(objects_data):
    """Extract keywords from Objects library"""
    keywords = set()

    # Extract object types from all professions
    for profession_group in objects_data:
        for object_group in profession_group.get('object_types', []):
            # Add main object name
            object_name = object_group.get('object', '')
            if object_name:
                keywords.add(object_name.lower())

            # Add object types
            for obj_type in object_group.get('types', []):
                keywords.add(obj_type.lower())

    return keywords

def extract_tool_keywords(tools_data):
    """Extract keywords from Tools library"""
    keywords = set()

    for tool_entry in tools_data:
        tool_name = tool_entry.get('Tools', '')
        if tool_name:
            keywords.add(tool_name.lower())
            # Add variations
            keywords.add(tool_name.replace(' ', '').lower())  # Remove spaces

    return keywords

def load_all_entity_keywords():
    """Load keywords from all entity libraries"""
    print("\nLoading entity libraries...")

    entity_keywords = {
        'action': set(),
        'object': set(),
        'process': set(),
        'result': set(),
        'tool': set(),
        'product': set(),
        'service': set()
    }

    # Load Actions
    if ACTIONS_PATH.exists():
        print(f"  Loading Actions from: {ACTIONS_PATH.name}")
        actions_data = load_json(ACTIONS_PATH)
        entity_keywords['action'] = extract_action_keywords(actions_data)
        print(f"    Extracted {len(entity_keywords['action'])} action keywords")

    # Load Objects
    if OBJECTS_PATH.exists():
        print(f"  Loading Objects from: {OBJECTS_PATH.name}")
        objects_data = load_json(OBJECTS_PATH)
        entity_keywords['object'] = extract_object_keywords(objects_data)
        print(f"    Extracted {len(entity_keywords['object'])} object keywords")

    # Load Tools
    if TOOLS_PATH.exists():
        print(f"  Loading Tools from: {TOOLS_PATH.name}")
        tools_data = load_json(TOOLS_PATH)
        entity_keywords['tool'] = extract_tool_keywords(tools_data)
        print(f"    Extracted {len(entity_keywords['tool'])} tool keywords")

    # Add manual process keywords (from original keywords)
    entity_keywords['process'].update([
        'recruitment', 'hiring', 'onboarding', 'training',
        'sales', 'prospecting', 'lead generation', 'conversion',
        'development', 'coding', 'testing', 'deployment',
        'design', 'prototyping', 'wireframing', 'mockup',
        'marketing', 'campaign', 'advertising', 'promotion',
        'workflow', 'pipeline', 'funnel', 'process', 'procedure'
    ])
    print(f"    Manual process keywords: {len(entity_keywords['process'])}")

    # Add manual result keywords
    entity_keywords['result'].update([
        'delivered', 'completed', 'achieved', 'outcome', 'result',
        'output', 'deliverable', 'milestone', 'success', 'performance',
        'quality', 'metric', 'kpi', 'target', 'goal',
        'satisfaction', 'rate', 'score', 'percentage', 'ratio'
    ])
    print(f"    Manual result keywords: {len(entity_keywords['result'])}")

    # Add manual product keywords
    entity_keywords['product'].update([
        'application', 'app', 'website', 'platform', 'system',
        'software', 'tool', 'feature', 'component', 'module',
        'dashboard', 'interface', 'portal', 'product'
    ])
    print(f"    Manual product keywords: {len(entity_keywords['product'])}")

    # Add manual service keywords
    entity_keywords['service'].update([
        'consulting', 'advisory', 'service', 'support',
        'development service', 'design service', 'marketing service',
        'training service', 'maintenance', 'hosting'
    ])
    print(f"    Manual service keywords: {len(entity_keywords['service'])}")

    return entity_keywords

def calculate_confidence_score(parameter_text, parameter_type, keywords):
    """
    Calculate confidence score for parameter matching
    Returns score between 0.0 and 1.0
    """
    score = 0.0
    matches = []

    param_lower = parameter_text.lower()
    type_lower = parameter_type.lower() if parameter_type else ""

    # Check keyword matches
    for keyword in keywords:
        if keyword in param_lower or keyword in type_lower:
            score += 0.1
            matches.append(keyword)

    # Cap at 1.0
    score = min(score, 1.0)

    return score, matches

def classify_parameter(param_entry, all_keywords):
    """
    Classify parameter across all entity types
    Returns dictionary of entity_type -> (score, matches)
    """
    param_text = param_entry.get('Parameters', '')
    param_type = param_entry.get('Types', '')

    classifications = {}

    for entity_type, keywords in all_keywords.items():
        score, matches = calculate_confidence_score(param_text, param_type, keywords)

        if score > 0.0:
            classifications[entity_type] = {
                'score': score,
                'matches': matches
            }

    return classifications

def create_output_directories():
    """Create output directory structure"""
    print("\nCreating output directories...")

    dirs = [
        'organized_by_action',
        'organized_by_object',
        'organized_by_process',
        'organized_by_result',
        'organized_by_tool',
        'organized_by_product',
        'organized_by_service',
        'cross_reference',
        'analysis'
    ]

    for dir_name in dirs:
        dir_path = OUTPUT_BASE / dir_name
        dir_path.mkdir(exist_ok=True)
        print(f"  Created: {dir_name}/")

def run_sample_analysis(params_data, all_keywords, sample_size=100):
    """Run analysis on a sample of parameters"""
    print(f"\nRunning sample analysis (first {sample_size} parameters)...")
    print("-" * 80)

    sample_data = params_data['data'][:sample_size]

    # Statistics
    entity_stats = defaultdict(int)
    no_category_count = 0
    multi_category_count = 0

    results = []

    for i, param in enumerate(sample_data, 1):
        if i % 20 == 0:
            print(f"  Processed: {i}/{sample_size}")

        classifications = classify_parameter(param, all_keywords)

        # Update statistics
        if len(classifications) == 0:
            no_category_count += 1
        elif len(classifications) > 1:
            multi_category_count += 1

        for entity_type in classifications:
            entity_stats[entity_type] += 1

        # Store result
        if i <= 20:  # Store first 20 for detailed inspection
            results.append({
                'parameter': param.get('Parameters', ''),
                'type': param.get('Types', ''),
                'classifications': classifications
            })

    # Print results
    print("\n" + "=" * 80)
    print("SAMPLE ANALYSIS RESULTS (v2 - Enhanced with actual entity libraries)")
    print("=" * 80)
    print(f"Sample Size: {sample_size}")
    print()
    print("Entity Type Distribution:")

    # Sort by count
    sorted_stats = sorted(entity_stats.items(), key=lambda x: x[1], reverse=True)
    for entity_type, count in sorted_stats:
        percentage = (count / sample_size) * 100
        print(f"  {entity_type:15}: {count:3} ({percentage:5.1f}%)")

    print()
    print("Classification Coverage:")
    has_category = sample_size - no_category_count
    has_category_pct = (has_category / sample_size) * 100
    no_category_pct = (no_category_count / sample_size) * 100
    multi_category_pct = (multi_category_count / sample_size) * 100

    print(f"  Parameters with matches:   {has_category} ({has_category_pct:.1f}%)")
    print(f"  Parameters with NO match:  {no_category_count} ({no_category_pct:.1f}%)")
    print(f"  Parameters with 2+ matches: {multi_category_count} ({multi_category_pct:.1f}%)")

    # Save detailed results
    output_file = OUTPUT_BASE / 'analysis' / 'sample_classification_results_v2.json'
    output_data = {
        'metadata': {
            'version': 'v2 (Enhanced)',
            'analysis_date': datetime.now().isoformat(),
            'sample_size': sample_size,
            'total_parameters': len(params_data['data'])
        },
        'statistics': {
            'entity_distribution': dict(sorted_stats),
            'coverage': {
                'with_matches': has_category,
                'no_matches': no_category_count,
                'multi_matches': multi_category_count
            }
        },
        'first_20_detailed_results': results,
        'keyword_counts': {
            entity_type: len(keywords)
            for entity_type, keywords in all_keywords.items()
        }
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"\nSample results saved: {output_file}")

    # Print recommendations
    print("\n" + "=" * 80)
    print("IMPROVEMENTS vs v1")
    print("=" * 80)

    if no_category_pct < 40:
        print("[OK] GOOD: Unmapped rate improved to", f"{no_category_pct:.1f}%")
    else:
        print("[WARNING] Still high unmapped rate:", f"{no_category_pct:.1f}%")

    if multi_category_pct > 20:
        print("[OK] GOOD: Multi-category coverage increased to", f"{multi_category_pct:.1f}%")

    print("\nKeyword Library Statistics:")
    for entity_type, keywords in all_keywords.items():
        print(f"  {entity_type:15}: {len(keywords):4} keywords")

    return has_category_pct, no_category_pct

def main():
    """Main execution"""
    print("=" * 80)
    print("PARAMETER ENTITY SPLITTING - v2 (Enhanced)")
    print("=" * 80)
    print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Create directories
    create_output_directories()

    # Load entity keywords from actual libraries
    all_keywords = load_all_entity_keywords()

    # Load parameters
    print("\nLoading parameters data...")
    params_file = PARAMS_PATH / "parameters.json"
    params_data = load_json(params_file)
    total_params = len(params_data['data'])
    print(f"  Total parameters: {total_params}")

    # Run sample analysis
    coverage_pct, unmapped_pct = run_sample_analysis(params_data, all_keywords, sample_size=100)

    print("\n" + "=" * 80)
    print("NEXT STEPS")
    print("=" * 80)
    print("1. Compare v2 results with v1 results")
    print("2. Review sample_classification_results_v2.json")
    print("3. Add more process/result/product/service keyword sources")
    print("4. Consider running full classification if coverage > 60%")

    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE (v2)")
    print("=" * 80)
    print(f"End Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == '__main__':
    main()
