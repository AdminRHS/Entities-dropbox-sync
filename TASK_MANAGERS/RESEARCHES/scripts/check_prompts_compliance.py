"""
Check prompts for compliance with updated LIBRARIES and TASK_MANAGERS
Identifies outdated references that need updating
"""
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def get_prompts_dir():
    """Get main PROMPTS directory"""
    base_path = Path(__file__).parent.parent.parent.parent
    return base_path / 'PROMPTS'

def get_researches_prompts_dir():
    """Get RESEARCHES local prompts directory"""
    base_path = Path(__file__).parent.parent
    return base_path / 'PROMPTS'

def get_libraries_dir():
    """Get LIBRARIES directory"""
    base_path = Path(__file__).parent.parent.parent.parent
    return base_path / 'LIBRARIES'

def get_task_managers_dir():
    """Get TASK_MANAGERS directory"""
    base_path = Path(__file__).parent.parent.parent
    return base_path

def find_all_prompts():
    """Find all prompt files"""
    prompts = []

    # Check main PROMPTS directory
    main_prompts_dir = get_prompts_dir()
    if main_prompts_dir.exists():
        prompts.extend(main_prompts_dir.glob('PMT-*.md'))

    # Check RESEARCHES PROMPTS directory
    research_prompts_dir = get_researches_prompts_dir()
    if research_prompts_dir.exists():
        prompts.extend(research_prompts_dir.glob('PMT-*.md'))

    return sorted(prompts)

def extract_references(content):
    """Extract entity references from prompt content"""
    references = {
        'tools': set(),
        'workflows': set(),
        'actions': set(),
        'objects': set(),
        'libraries': set(),
        'departments': set(),
        'phases': set(),
        'paths': set()
    }

    # Tool references (TOOL-XXX-###, TOL-###, old formats)
    tool_patterns = [
        r'TOOL-[A-Z]+-\d+',
        r'TOL-\d+',
        r'TOOL_[A-Z]+_\d+',
    ]
    for pattern in tool_patterns:
        references['tools'].update(re.findall(pattern, content))

    # Workflow references (WRF-###, PROC-###, old formats)
    workflow_patterns = [
        r'WRF-\d+',
        r'PROC-\d+',
        r'WORKFLOW-\d+',
    ]
    for pattern in workflow_patterns:
        references['workflows'].update(re.findall(pattern, content))

    # Action references
    references['actions'].update(re.findall(r'ACT-\d+', content))

    # Object references
    references['objects'].update(re.findall(r'OBJ-\d+', content))

    # Library references
    library_patterns = [
        r'LIBRARIES/[\w/]+',
        r'ENTITIES/LIBRARIES/[\w/]+',
    ]
    for pattern in library_patterns:
        references['libraries'].update(re.findall(pattern, content))

    # Department codes
    dept_patterns = [
        r'\b(AID|DEV|HRM|LGN|DGN|VID|SLS|SMM|FNC|MKT)\b',
        r'Department:\s*([A-Z]{3})',
    ]
    for pattern in dept_patterns:
        references['departments'].update(re.findall(pattern, content))

    # Phase references (check for outdated phase names)
    phase_patterns = [
        r'Phase_\d+_\w+',
        r'Phase \d+:?\s+\w+',
    ]
    for pattern in phase_patterns:
        references['phases'].update(re.findall(pattern, content, re.IGNORECASE))

    # Path references
    path_patterns = [
        r'ENTITIES/[\w/]+',
        r'TASK_MANAGERS/[\w/]+',
        r'RESEARCHES/[\w/]+',
    ]
    for pattern in path_patterns:
        references['paths'].update(re.findall(pattern, content))

    return references

def check_phase_compliance(phases_found):
    """Check if phases use old naming convention"""
    outdated_phases = []
    deprecated_phases = ['Phase_2_Named', 'Phase_3_Analyzed', 'Phase_4_Objects', 'Phase_7_Mapped']

    for phase in phases_found:
        # Check for deprecated phase names
        if any(dep in phase for dep in deprecated_phases):
            outdated_phases.append({
                'phase': phase,
                'reason': 'Deprecated phase name (eliminated or renamed)',
                'suggestion': get_phase_suggestion(phase)
            })
        # Check for old numbering (Phase_6, Phase_7, Phase_8)
        elif any(f'Phase_{i}' in phase or f'Phase {i}' in phase for i in [6, 7, 8]):
            outdated_phases.append({
                'phase': phase,
                'reason': 'Old phase numbering (system now uses Phase_0 through Phase_5)',
                'suggestion': get_phase_suggestion(phase)
            })

    return outdated_phases

def get_phase_suggestion(old_phase):
    """Get suggestion for updated phase name"""
    suggestions = {
        'Phase_2_Named': 'Merged into Phase_1_Transcribed (PMT-004)',
        'Phase_3_Analyzed': 'Merged into Phase_1_Transcribed (PMT-004)',
        'Phase_4_Objects': 'Renamed to Phase_2_Extraction (PMT-007)',
        'Phase_5_Gap_Analysis': 'Now Phase_3_Gap_Analysis',
        'Phase_6_Integration': 'Now Phase_4_Integration',
        'Phase_7_Mapped': 'Renamed to Phase_5_Mapping (PMT-009 Part 3)',
    }

    for old, new in suggestions.items():
        if old in old_phase:
            return new

    return 'Check RESEARCHES/README.md for current phase structure'

def check_path_compliance(paths_found):
    """Check if paths reference old structure"""
    outdated_paths = []

    old_structures = [
        'RESEARCHES/VIDEO_RESEARCHES',
        'RESEARCHES/PROMPTS/Transcription',
        'RESEARCHES/PROMPTS/Analysis',
        'RESEARCHES/PROMPTS/Taxonomy_Integration',
        'RESEARCHES/Video_Processing',
        'RESEARCHES/RESEARCH_PROMPTS',
        'TASK_MANAGERS/TSM-005_Workflows',
        'TASK_MANAGERS/TSM-006_Workflowsm',
    ]

    for path in paths_found:
        for old_struct in old_structures:
            if old_struct in path:
                outdated_paths.append({
                    'path': path,
                    'reason': 'References old directory structure',
                    'suggestion': get_path_suggestion(path)
                })

    return outdated_paths

def get_path_suggestion(old_path):
    """Get suggestion for updated path"""
    suggestions = {
        'RESEARCHES/VIDEO_RESEARCHES': 'RESEARCHES/ (VIDEO_RESEARCHES removed)',
        'RESEARCHES/PROMPTS': 'ENTITIES/PROMPTS/ (consolidated)',
        'RESEARCHES/Video_Processing': 'RESEARCHES/ (integrated)',
        'TSM-005_Workflows': 'TSM-006_Workflows (merged)',
        'TSM-006_Workflowsm': 'TSM-006_Workflows (typo fixed)',
    }

    for old, new in suggestions.items():
        if old in old_path:
            return new

    return 'Check current directory structure'

def analyze_prompt(prompt_path):
    """Analyze a single prompt file"""
    try:
        with open(prompt_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return None

    # Extract references
    references = extract_references(content)

    # Check for issues
    issues = []

    # Check phase compliance
    if references['phases']:
        phase_issues = check_phase_compliance(references['phases'])
        issues.extend([{'type': 'phase', **issue} for issue in phase_issues])

    # Check path compliance
    if references['paths']:
        path_issues = check_path_compliance(references['paths'])
        issues.extend([{'type': 'path', **issue} for issue in path_issues])

    # Check for deprecated prompt references
    if 'PMT-005' in content or 'PMT-006' in content:
        if 'DEPRECATED' not in content and 'deprecated' not in content:
            issues.append({
                'type': 'deprecated_prompt',
                'reason': 'References PMT-005 or PMT-006 (now deprecated)',
                'suggestion': 'PMT-005 and PMT-006 merged into PMT-004. Update reference or add deprecation note.'
            })

    return {
        'path': prompt_path,
        'references': references,
        'issues': issues
    }

def generate_compliance_report():
    """Generate compliance report for all prompts"""
    print("\n" + "="*120)
    print("PROMPT COMPLIANCE CHECK - Libraries & Task Managers")
    print("="*120)
    print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("="*120)

    # Find all prompts
    prompts = find_all_prompts()
    print(f"\nTotal Prompts Found: {len(prompts)}")

    # Analyze each prompt
    results = []
    issues_by_type = defaultdict(list)

    for prompt in prompts:
        result = analyze_prompt(prompt)
        if result and result['issues']:
            results.append(result)
            for issue in result['issues']:
                issues_by_type[issue['type']].append({
                    'prompt': prompt.name,
                    'issue': issue
                })

    # Summary
    print("\n" + "="*120)
    print("SUMMARY")
    print("="*120)

    if not results:
        print("\nAll prompts are compliant! No issues found.")
    else:
        print(f"\n[WARNING] Found {len(results)} prompt(s) with potential issues")
        print(f"   Total Issues: {sum(len(r['issues']) for r in results)}")

        print(f"\nIssue Breakdown:")
        print(f"  - Phase References: {len(issues_by_type['phase'])} issues")
        print(f"  - Path References: {len(issues_by_type['path'])} issues")
        print(f"  - Deprecated Prompts: {len(issues_by_type['deprecated_prompt'])} issues")

    # Detailed report
    if results:
        print("\n" + "="*120)
        print("DETAILED ISSUES")
        print("="*120)

        # Phase issues
        if issues_by_type['phase']:
            print("\n>> PHASE REFERENCE ISSUES:")
            print("-"*120)

            for item in issues_by_type['phase']:
                print(f"\nPrompt: {item['prompt']}")
                print(f"  Issue: {item['issue']['phase']}")
                print(f"  Reason: {item['issue']['reason']}")
                print(f"  Suggestion: {item['issue']['suggestion']}")

        # Path issues
        if issues_by_type['path']:
            print("\n>> PATH REFERENCE ISSUES:")
            print("-"*120)

            for item in issues_by_type['path']:
                print(f"\nPrompt: {item['prompt']}")
                print(f"  Issue: {item['issue']['path']}")
                print(f"  Reason: {item['issue']['reason']}")
                print(f"  Suggestion: {item['issue']['suggestion']}")

        # Deprecated prompt references
        if issues_by_type['deprecated_prompt']:
            print("\n>> DEPRECATED PROMPT REFERENCES:")
            print("-"*120)

            for item in issues_by_type['deprecated_prompt']:
                print(f"\nPrompt: {item['prompt']}")
                print(f"  Reason: {item['issue']['reason']}")
                print(f"  Suggestion: {item['issue']['suggestion']}")

    # Recommendations
    print("\n" + "="*120)
    print("RECOMMENDATIONS")
    print("="*120)

    if results:
        print("\n1. Update phase references to use new 7-phase structure:")
        print("   - Phase_0: Queued")
        print("   - Phase_1: Transcribed (includes analysis)")
        print("   - Phase_2: Extraction (renamed from Phase_4_Objects)")
        print("   - Phase_3: Gap Analysis")
        print("   - Phase_4: Integration")
        print("   - Phase_5: Mapping (renamed from Phase_7_Mapped)")

        print("\n2. Update deprecated prompt references:")
        print("   - PMT-005 (Video Naming) -> Merged into PMT-004")
        print("   - PMT-006 (Video Analysis) -> Merged into PMT-004")

        print("\n3. Update path references to reflect current structure:")
        print("   - RESEARCHES/VIDEO_RESEARCHES -> RESEARCHES/")
        print("   - RESEARCHES/PROMPTS -> ENTITIES/PROMPTS/")
        print("   - TSM-005_Workflows -> TSM-006_Workflows")

        print("\n4. Review and test updated prompts before use")
    else:
        print("\nNo action required - all prompts are up to date!")

    print("\n" + "="*120)

def generate_statistics_report():
    """Generate statistics on prompt references"""
    prompts = find_all_prompts()

    print("\n" + "="*120)
    print("PROMPT REFERENCE STATISTICS")
    print("="*120)

    all_refs = {
        'tools': set(),
        'workflows': set(),
        'actions': set(),
        'objects': set(),
        'departments': set()
    }

    for prompt in prompts:
        result = analyze_prompt(prompt)
        if result:
            for key in all_refs.keys():
                all_refs[key].update(result['references'][key])

    print(f"\nTotal Entity References Found:")
    print(f"  - Tools: {len(all_refs['tools'])} unique references")
    print(f"  - Workflows: {len(all_refs['workflows'])} unique references")
    print(f"  - Actions: {len(all_refs['actions'])} unique references")
    print(f"  - Objects: {len(all_refs['objects'])} unique references")
    print(f"  - Departments: {len(all_refs['departments'])} unique codes")

    if all_refs['departments']:
        print(f"\nDepartments Referenced:")
        for dept in sorted(all_refs['departments']):
            print(f"  - {dept}")

    print("\n" + "="*120)

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'stats':
        generate_statistics_report()
    else:
        generate_compliance_report()
