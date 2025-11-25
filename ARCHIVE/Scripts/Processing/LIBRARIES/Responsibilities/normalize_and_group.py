#!/usr/bin/env python3
"""
Normalize and group action+object pairs into variant arrays
Phase 1.2-1.5 of Responsibilities Architecture Merge
"""

import json
import re
from pathlib import Path
from collections import defaultdict

OUTPUT_DIR = Path(r"C:\Users\Dell\Dropbox\Entities\LIBRARIES\Responsibilities")

# Common action variants (base form → all forms)
ACTION_VARIANTS = {
    'enrich': ['enrich', 'enriching', 'enriched', 'enrich list'],
    'scrape': ['scrape', 'scraping', 'scraped'],
    'generate': ['generate', 'generating', 'generated'],
    'extract': ['extract', 'extracting', 'extracted'],
    'create': ['create', 'creating', 'created'],
    'update': ['update', 'updating', 'updated'],
    'discover': ['discover', 'discovering', 'discovered'],
    'research': ['research', 'researching', 'researched'],
    'transcribe': ['transcribe', 'transcribing', 'transcribed'],
    'analyze': ['analyze', 'analyzing', 'analyzed'],
    'prepare': ['prepare', 'preparing', 'prepared'],
    'upload': ['upload', 'uploading', 'uploaded'],
    'export': ['export', 'exporting', 'exported'],
    'review': ['review', 'reviewing', 'reviewed'],
    'configure': ['configure', 'configuring', 'configured'],
    'build': ['build', 'building', 'built'],
    'deploy': ['deploy', 'deploying', 'deployed'],
    'test': ['test', 'testing', 'tested'],
    'validate': ['validate', 'validating', 'validated'],
    'document': ['document', 'documenting', 'documented'],
}

# Common object variants (base form → all forms)
OBJECT_VARIANTS = {
    'leads': ['lead', 'leads', 'lead list', 'lead lists'],
    'emails': ['email', 'emails', 'email list', 'email lists'],
    'contacts': ['contact', 'contacts', 'contact list', 'contact lists'],
    'videos': ['video', 'videos', 'video list'],
    'tutorials': ['tutorial', 'tutorials', 'ai tutorial', 'ai tutorials'],
    'channels': ['channel', 'channels', 'youtube channel', 'youtube channels'],
    'creators': ['creator', 'creators', 'influencer', 'influencers'],
    'domains': ['domain', 'domains', 'company domain', 'company domains'],
    'profiles': ['profile', 'profiles'],
    'data': ['data', 'dataset', 'datasets'],
}

def normalize_action(action):
    """Normalize action to base form"""
    action = action.lower().strip()
    for base, variants in ACTION_VARIANTS.items():
        if action in variants:
            return base
    return action

def normalize_object(obj):
    """Normalize object to base form"""
    obj = obj.lower().strip()

    # Remove common prefixes from step names
    obj = re.sub(r'^(prepare|create|update|configure|build|review|export|upload)\s+', '', obj)

    # Check against known variants
    for base, variants in OBJECT_VARIANTS.items():
        for variant in variants:
            if variant in obj:
                return base

    # Return simplified object
    obj = re.sub(r'\s+(via|in|to|from|for|with)\s+.*$', '', obj)  # Remove context
    return obj.strip()

def main():
    print("=" * 60)
    print("Phase 1.2-1.5: Normalize and Group Variants")
    print("=" * 60)

    # Load unique combinations
    with open(OUTPUT_DIR / "unique_combinations.json", 'r', encoding='utf-8') as f:
        combinations = json.load(f)

    print(f"\nLoaded {len(combinations)} unique combinations")

    # Normalize and group
    normalized_groups = defaultdict(lambda: {
        'action_base': '',
        'object_base': '',
        'action_variants': set(),
        'object_variants': set(),
        'departments': set(),
        'frequency': 0,
        'examples': []
    })

    for combo in combinations:
        action = combo['action']
        obj = combo['object']

        # Normalize
        action_base = normalize_action(action)
        object_base = normalize_object(obj)

        key = f"{action_base}+{object_base}"

        # Group
        group = normalized_groups[key]
        group['action_base'] = action_base
        group['object_base'] = object_base
        group['action_variants'].add(action)
        group['object_variants'].add(obj)
        group['frequency'] += combo['frequency']

        for example in combo['examples']:
            group['departments'].add(example['department'])
            if len(group['examples']) < 3:
                group['examples'].append(example)

    # Convert sets to lists for JSON serialization
    for key, group in normalized_groups.items():
        group['action_variants'] = sorted(list(group['action_variants']))
        group['object_variants'] = sorted(list(group['object_variants']))
        group['departments'] = sorted(list(group['departments']))

    print(f"Normalized down to {len(normalized_groups)} unique action+object groups")

    # Save normalized groups
    output_file = OUTPUT_DIR / "phrase_combinations.json"
    output_data = [
        {
            'id': f"TEMP-{i:03d}",
            'primary_phrase': f"{data['action_base']} {data['object_base']}",
            'action_base': data['action_base'],
            'object_base': data['object_base'],
            'action_variants': data['action_variants'],
            'object_variants': data['object_variants'],
            'departments': data['departments'],
            'frequency': data['frequency'],
            'examples': data['examples']
        }
        for i, (key, data) in enumerate(sorted(normalized_groups.items(), key=lambda x: x[1]['frequency'], reverse=True), 1)
    ]

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    print(f"Saved phrase combinations to: {output_file}")

    # Create action variants map
    action_map = {}
    for group in output_data:
        base = group['action_base']
        if base not in action_map:
            action_map[base] = set()
        action_map[base].update(group['action_variants'])

    action_map = {k: sorted(list(v)) for k, v in sorted(action_map.items())}

    with open(OUTPUT_DIR / "action_variants_map.json", 'w', encoding='utf-8') as f:
        json.dump(action_map, f, indent=2, ensure_ascii=False)
    print(f"Saved action variants map: {len(action_map)} base actions")

    # Create object variants map
    object_map = {}
    for group in output_data:
        base = group['object_base']
        if base not in object_map:
            object_map[base] = set()
        object_map[base].update(group['object_variants'])

    object_map = {k: sorted(list(v)) for k, v in sorted(object_map.items())}

    with open(OUTPUT_DIR / "object_variants_map.json", 'w', encoding='utf-8') as f:
        json.dump(object_map, f, indent=2, ensure_ascii=False)
    print(f"Saved object variants map: {len(object_map)} base objects")

    # Print top 30 normalized groups
    print("\nTop 30 most frequent normalized groups:")
    for i, item in enumerate(output_data[:30], 1):
        dept_str = ', '.join(item['departments'][:2])
        print(f"  {i:2d}. {item['primary_phrase']:35s} ({item['frequency']:2d}x) - {dept_str}")
        print(f"      Actions: {', '.join(item['action_variants'][:3])}")
        print(f"      Objects: {', '.join(item['object_variants'][:2])}")

    print("\n" + "=" * 60)
    print("Phase 1.2-1.5 Complete!")
    print("=" * 60)
    print(f"\nSummary:")
    print(f"  - Original combinations: 244")
    print(f"  - Normalized groups: {len(normalized_groups)}")
    print(f"  - Unique actions: {len(action_map)}")
    print(f"  - Unique objects: {len(object_map)}")

if __name__ == "__main__":
    main()
