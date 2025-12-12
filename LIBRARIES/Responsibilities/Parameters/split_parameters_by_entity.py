"""
Split Parameters by Related Entities

Purpose: Organize 10,596 parameters across 8 entity types for better cross-referencing
Created: 2025-12-11
Status: Initial version - Phase 1

Entity Types:
- Actions (429)
- Objects (36)
- Processes (428)
- Results (432)
- Tools (75+)
- Products (39)
- Services (7 categories)
- Professions (12+ - already organized)
"""

import json
import os
import re
from datetime import datetime
from collections import defaultdict
from pathlib import Path

# Configuration
BASE_PATH = Path(__file__).parent
SOURCE_FILE = BASE_PATH / "parameters.json"

# Entity library paths
ENTITY_PATHS = {
    'actions': BASE_PATH.parent / "Actions" / "Actions_Master.json",
    'objects': BASE_PATH.parent / "Objects" / "objects.json",
    'processes': BASE_PATH.parent.parent / "Processes" / "Processes_Master.json",
    'results': BASE_PATH.parent.parent / "Results" / "Results_Master.json",
    'tools': BASE_PATH.parent.parent / "LBS_003_Tools" / "tools.json",
    'products': BASE_PATH.parent.parent / "Products" / "Products_Master.json",
    'services': BASE_PATH.parent.parent / "Services" / "services.json",
}

# Output directories
OUTPUT_DIRS = {
    'action': BASE_PATH / "organized_by_action",
    'object': BASE_PATH / "organized_by_object",
    'process': BASE_PATH / "organized_by_process",
    'result': BASE_PATH / "organized_by_result",
    'tool': BASE_PATH / "organized_by_tool",
    'product': BASE_PATH / "organized_by_product",
    'service': BASE_PATH / "organized_by_service",
    'cross_reference': BASE_PATH / "cross_reference",
    'analysis': BASE_PATH / "analysis",
}

# Keyword mappings for classification
ENTITY_KEYWORDS = {
    'action': {
        'communication': ['email', 'message', 'notify', 'communicate', 'contact', 'send', 'reply', 'response'],
        'analysis': ['analyze', 'review', 'assess', 'evaluate', 'measure', 'audit', 'inspect'],
        'creation': ['create', 'design', 'develop', 'build', 'generate', 'produce', 'make'],
        'optimization': ['optimize', 'improve', 'enhance', 'refine', 'streamline', 'upgrade'],
        'management': ['manage', 'organize', 'coordinate', 'supervise', 'oversee', 'administer'],
        'integration': ['integrate', 'connect', 'link', 'sync', 'merge', 'combine'],
        'research': ['research', 'investigate', 'explore', 'study', 'examine'],
        'documentation': ['document', 'record', 'log', 'note', 'catalog', 'archive'],
    },
    'object': {
        'document': ['document', 'file', 'report', 'specification', 'proposal', 'contract'],
        'video': ['video', 'recording', 'footage', 'clip', 'media'],
        'design': ['mockup', 'wireframe', 'prototype', 'layout', 'template', 'graphic'],
        'code': ['code', 'script', 'program', 'function', 'module', 'component'],
        'data': ['data', 'dataset', 'database', 'table', 'record', 'entry'],
        'asset': ['asset', 'resource', 'material', 'content', 'media'],
    },
    'process': {
        'recruitment': ['hiring', 'candidate', 'interview', 'screening', 'onboarding'],
        'sales': ['sales', 'prospect', 'lead', 'deal', 'pipeline', 'conversion'],
        'development': ['development', 'coding', 'programming', 'implementation', 'deployment'],
        'design': ['design', 'creative', 'visual', 'graphics', 'branding'],
        'marketing': ['marketing', 'campaign', 'advertising', 'promotion', 'seo'],
        'support': ['support', 'customer', 'client', 'service', 'helpdesk'],
    },
    'result': {
        'delivery': ['delivered', 'completed', 'shipped', 'deployed', 'launched'],
        'quality': ['quality', 'standard', 'benchmark', 'excellence', 'criteria'],
        'performance': ['performance', 'efficiency', 'speed', 'throughput', 'capacity'],
        'success': ['success', 'achievement', 'goal', 'target', 'objective'],
        'satisfaction': ['satisfaction', 'feedback', 'rating', 'score', 'nps'],
    },
    'tool': {
        'crm': ['crm', 'customer relationship', 'salesforce', 'hubspot'],
        'design': ['figma', 'adobe', 'photoshop', 'illustrator', 'sketch'],
        'development': ['github', 'gitlab', 'vscode', 'ide', 'compiler'],
        'communication': ['slack', 'teams', 'zoom', 'email', 'chat'],
        'analytics': ['analytics', 'google analytics', 'mixpanel', 'amplitude'],
        'project_management': ['jira', 'trello', 'asana', 'monday', 'notion'],
    },
    'product': {
        'application': ['app', 'application', 'software', 'platform'],
        'website': ['website', 'web', 'site', 'portal'],
        'feature': ['feature', 'functionality', 'capability', 'module'],
        'service': ['service', 'offering', 'solution'],
    },
    'service': {
        'consulting': ['consulting', 'advisory', 'guidance', 'consultation'],
        'development': ['development service', 'engineering', 'coding'],
        'design': ['design service', 'creative service'],
        'marketing': ['marketing service', 'advertising', 'promotion'],
    }
}


def load_json(filepath):
    """Load JSON file safely"""
    try:
        if not os.path.exists(filepath):
            print(f"Warning: File not found: {filepath}")
            return None

        with open(filepath, 'r', encoding='utf-8-sig') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None


def create_output_directories():
    """Create all output directories"""
    print("Creating output directories...")
    for dir_name, dir_path in OUTPUT_DIRS.items():
        dir_path.mkdir(exist_ok=True)
        print(f"  Created: {dir_name}/")
    print()


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
    for category, keyword_list in keywords.items():
        for keyword in keyword_list:
            if keyword in param_lower or keyword in type_lower:
                score += 0.1
                matches.append((category, keyword))

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

        if score > 0.0:  # Include all positive matches
            classifications[entity_type] = {
                'score': score,
                'matches': matches,
                'categories': list(set([m[0] for m in matches]))
            }

    return classifications


def process_parameters():
    """Main processing function"""

    print("=" * 80)
    print("PARAMETER ENTITY SPLITTING - Phase 1: Analysis")
    print("=" * 80)
    print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Load source data
    print("Loading source data...")
    params_data = load_json(SOURCE_FILE)

    if not params_data:
        print("ERROR: Could not load parameters.json")
        return

    total_params = len(params_data.get('data', []))
    print(f"  Total parameters: {total_params}")
    print()

    # Sample analysis (first 100 parameters)
    print("Running sample analysis (first 100 parameters)...")
    print("-" * 80)

    sample_size = min(100, total_params)
    sample_data = params_data['data'][:sample_size]

    # Classification statistics
    entity_stats = defaultdict(int)
    multi_category_count = 0
    no_category_count = 0

    sample_results = []

    for i, param in enumerate(sample_data, 1):
        classifications = classify_parameter(param, ENTITY_KEYWORDS)

        # Track statistics
        if len(classifications) == 0:
            no_category_count += 1
        elif len(classifications) > 1:
            multi_category_count += 1

        for entity_type in classifications:
            entity_stats[entity_type] += 1

        # Store result
        sample_results.append({
            'parameter': param.get('Parameters'),
            'type': param.get('Types'),
            'classifications': classifications
        })

        # Progress
        if i % 20 == 0:
            print(f"  Processed: {i}/{sample_size}")

    print()
    print("=" * 80)
    print("SAMPLE ANALYSIS RESULTS")
    print("=" * 80)
    print(f"Sample Size: {sample_size}")
    print()

    print("Entity Type Distribution:")
    for entity_type, count in sorted(entity_stats.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / sample_size) * 100
        print(f"  {entity_type:15s}: {count:3d} ({percentage:5.1f}%)")

    print()
    print("Classification Coverage:")
    print(f"  Parameters with 0 matches: {no_category_count} ({no_category_count/sample_size*100:.1f}%)")
    print(f"  Parameters with 1 match:  {sample_size - multi_category_count - no_category_count}")
    print(f"  Parameters with 2+ matches: {multi_category_count} ({multi_category_count/sample_size*100:.1f}%)")
    print()

    # Save sample results
    sample_output_file = BASE_PATH / "analysis" / "sample_classification_results.json"
    with open(sample_output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'metadata': {
                'analysis_date': datetime.now().isoformat(),
                'sample_size': sample_size,
                'total_parameters': total_params,
                'statistics': {
                    'entity_distribution': dict(entity_stats),
                    'multi_category_count': multi_category_count,
                    'no_category_count': no_category_count
                }
            },
            'sample_results': sample_results[:20]  # Save first 20 for inspection
        }, f, indent=2)

    print(f"Sample results saved: {sample_output_file}")
    print()

    # Recommendations
    print("=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    print()

    if no_category_count > sample_size * 0.2:
        print("[WARNING] HIGH: Over 20% of parameters have no entity matches")
        print("  Recommendation: Expand keyword dictionaries")
        print()

    if multi_category_count > sample_size * 0.5:
        print("[OK] GOOD: Over 50% parameters match multiple entities")
        print("  This indicates good cross-referencing potential")
        print()

    print("Next Steps:")
    print("  1. Review sample_classification_results.json")
    print("  2. Refine keyword dictionaries in ENTITY_KEYWORDS")
    print("  3. Adjust confidence score thresholds")
    print("  4. Run full classification on all 10,596 parameters")
    print()

    print("=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)
    print(f"End Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    # Create output directories
    create_output_directories()

    # Run analysis
    process_parameters()
